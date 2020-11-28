"""
    The detector file depends on numpy, numba, cv2 and key values from GT reader.
    Its purpose is to serve a couple of more complicated methods used to detect
    item references against target images and calculate a detection result
"""
from numpy import zeros, uint8, float32
from numba import njit
from cv2 import putText, ORB_create, BFMatcher, NORM_HAMMING2, FONT_HERSHEY_SIMPLEX
from detector.gt_reader import TIME_KEY, ITEMS_KEY


# Keys used to access arguments specified within args
ARGS_REF_KEY = 'references'
ARGS_PAGE_KEY = 'page'
ARGS_ROI_KEY = 'roi'
ARGS_GT_KEY = 'ground_truth'

# The debug item number text settings
thickness = 2
font_scale = 1
font_face = FONT_HERSHEY_SIMPLEX

# The number of key points which should match between
# a target and reference image before the detector
# accept the item
min_acceptable_matches = 10

# The number of features the orb object can find within
# the given image
ORB_N_FEATURES = 10000

# The number of times a reference should be found before
# we decide a final location
MAX_MATCHING_TIMES = 5


def indicate_matches(frame, references, labels, page):
    """
        Indicates at the given frame where the references were found,
        and highlight matching page labels
    """

    # loop through the references
    for i in range(0, len(references)):
        # Get current reference
        reference = references[i]

        # If the reference was found within the frame
        if reference.get_matching_times() >= MAX_MATCHING_TIMES:
            # Get the reference location
            y, x = reference.get_location()

            # Write the matching reference's iteration number at the location
            # it was matched within the frame image
            putText(frame, f'{i}', (int(x), int(y)), color=reference.get_color(),
                    fontFace=font_face, thickness=thickness, fontScale=font_scale)

            # if the page is still active
            if page.is_active:
                # color the reference's label border and text
                color = reference.get_color_for_tkinter()
                labels[i].configure(bg=color, fg=color)


def after_frame_check(frame, args):
    """
        Used to specify functionality that should happen
        after the frame detection check
    """
    # get reference, page from args
    references = args[ARGS_REF_KEY]
    page = args[ARGS_PAGE_KEY]
    # draw match indications
    indicate_matches(frame, references, page.item_labels, page)


# Used to match a frame against the given references
def frame_check(frame, args, n_frame, gt_check, current_duration):
    """
        Used to specify functionality that should happen
        after the frame detection check.
    """

    # get references and ground truth from args
    references = args[ARGS_REF_KEY]
    ground_truth = args[ARGS_GT_KEY]

    # check if there are any references we have not found
    # enough times, to conclude it is bought
    any_to_detect = False
    for reference in references:
        if reference.get_matching_times() < MAX_MATCHING_TIMES:
            any_to_detect = True
            break

    # if all references are detected, stop the method at this line
    if not any_to_detect:
        return

    # get the specified roi
    roi = args[ARGS_ROI_KEY]

    # grayscale the given frame
    frame_gray = grayscale(frame, y_start=roi[0], y_end=roi[1], x_start=roi[2], x_end=roi[3])

    # find a ground truth iteration that match
    # the current inspecting frame
    frame_ground_truth = None
    if gt_check:
        # get the formatted ground truth data
        ground_truth_data = ground_truth.get_data()

        # find the iteration that match the given duration
        for data in ground_truth_data:
            if data[TIME_KEY] >= current_duration:
                frame_ground_truth = ground_truth_data[n_frame]
                break

    # create an opencv orb object looking for n features
    orb = ORB_create(nfeatures=ORB_N_FEATURES)

    # compute unique key points within the grayscale frame
    features2, des2 = orb.detectAndCompute(frame_gray, None)

    # create an opencv bf matcher object using the NORM_HAMMING method
    bf = BFMatcher(NORM_HAMMING2)

    # loop through all references
    for i in range(0, len(references)):
        # get the current reference
        reference = references[i]
        # expect the detection truth to be false
        detection_truth = False
        detection_position = None

        # continue to the next iteration of the loop
        # if the reference's matching times exceeded
        # the specified max matching times
        if reference.get_matching_times() >= MAX_MATCHING_TIMES:
            detection_truth = True
            detection_position = reference.get_location()
        else:

            # get the reference grayscale image
            query_img = reference.get_image()

            # compute unique key points within the reference grayscale image
            features1, des1 = orb.detectAndCompute(query_img, None)

            # match the current key points found between the frame and reference
            matches = bf.knnMatch(des1, des2, k=2)

            # Nearest neighbour ratio test to find good matches
            good = []
            good_without_lists = []
            matches = [match for match in matches if len(match) == 2]
            for m, n in matches:
                if m.distance < 0.8 * n.distance:
                    good.append([m])
                    good_without_lists.append(m)

            # if the number of good matches is greater than
            # minimum acceptable matches
            if len(good) >= min_acceptable_matches:
                detection_truth = True
                # get an array of the matched positions
                dst_pts = float32([features2[m.trainIdx].pt for m in good_without_lists]).reshape(-1, 1, 2)
                # save the second as the last matched location
                detection_position = (dst_pts[0][0][1], dst_pts[0][0][0])
                reference.set_location(detection_position[0], detection_position[1])
                # increase the number of times this references was found
                reference.increase_matching()

        # if we got ground truth data for this frame, save the detection result
        if frame_ground_truth is not None:
            # get the ground truth items array
            item_data = frame_ground_truth[ITEMS_KEY][i]

            # if the item array length is greater than zero
            # it contains an item
            item_truth = len(item_data) > 0

            # used to determine if the detection
            # was at the correct location
            within_roi_truth = False
            # however, this is only necessary, if
            # we expect there should be an item
            if item_truth and detection_truth:
                # get position and size
                x, y, w, h = item_data[0], item_data[1], item_data[2], item_data[3]
                # check if the detection position
                # was within the ground truth position
                within_roi_truth = (
                        y <= detection_position[0] <= y + h and
                        x <= detection_position[1] <= x + w
                )
                
            # increase the GT object by the item and detection truth
            ground_truth.increase_by(item_truth, detection_truth, within_roi_truth)


# Use the njit tag from numba on this method to optimize the execution
@njit
def grayscale(image, y_start=0, y_end=0, x_start=0, x_end=0):
    """
       Returns a grayscale version of the given image using the
       specified region of interest
    """

    # create an empty image with the same size as the one given
    new_image = zeros(image.shape, uint8)

    # declare temp grayscale const.
    __WR, __WG, __WB = 0.299, 0.587, 0.114

    # loop through the image's height
    for y in range(y_start, image.shape[0] - y_end):
        # loop through the image's width
        for x in range(x_start, image.shape[1] - x_end):
            # calculate the intensity
            i = (__WB * image[y, x, 0]) + \
                (__WG * image[y, x, 1]) + \
                (__WR * image[y, x, 2])
            # add the intensity to the color channels
            for c in range(image.shape[2]):
                new_image[y, x, c] = i

    # return the grayscale image
    return new_image
