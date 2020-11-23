from numpy import zeros, uint8
from numba import njit
import cv2
import numpy as np

# The ROI of the target image, that should be matched
y_start, y_end = 930, 35
x_start, x_end = 1084, 630

# The debug item number text settings
thickness = 2
font_scale = 1
font_face = cv2.FONT_HERSHEY_SIMPLEX

# The number of key points which should match between
# a target and reference image before the detector
# accept the item
min_acceptable_matches = 10

# The number of times a reference should be found before
# we decide a final location
max_matching_times = 5


def indicate_matches(frame, references, labels, page):
    # loop through the references
    for i in range(0, len(references)):
        # Get current reference
        reference = references[i]

        # If the reference was found within the frame
        if reference.get_matching_times() >= max_matching_times:
            # Get the reference location
            y, x = reference.get_location()

            # Write the matching reference's iteration number at the location
            # it was matched within the frame image
            cv2.putText(frame, f'{i}', (int(x), int(y)), color=reference.get_color(),
                        fontFace=font_face, thickness=thickness, fontScale=font_scale)

            # if the page is still active
            if page.is_active:
                # color the reference's label border and text
                color = reference.get_color_for_tkinter()
                labels[i].configure(bg=color, fg=color)


# Executed after running the frame check
def after_frame_check(frame, args):
    # get reference, page, and labels from the option argument
    references = args['references']
    page = args['page']
    labels = page.item_labels
    # draw match indications
    indicate_matches(frame, references, labels, page)


# Used to grayscale and match a frame against the given references
def frame_check(frame, args, n_frame, current_duration):
    frame_gray = grayscale(frame, y_start, y_end, x_start, x_end)

    references = args['references']
    ground_truth = args['ground_truth']
    ground_truth_data = ground_truth.get_data()
    frame_ground_truth = None
    for data in ground_truth_data:
        if data['time'] >= current_duration:
            frame_ground_truth = ground_truth_data[n_frame]
            break

    if frame_ground_truth is None:
        return

    any_to_detect = False
    for reference in references:
        if reference.get_matching_times() < max_matching_times:
            any_to_detect = True
            break

    if not any_to_detect:
        return

    orb = cv2.ORB_create(nfeatures=10000)
    features2, des2 = orb.detectAndCompute(frame_gray, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING2)

    i = 0
    for reference in references:

        item_data = frame_ground_truth['items'][i]
        item_truth = len(item_data) > 0
        detection_truth = False

        # continue to the next iteration of the loop
        # if the reference's matching times exceeded
        # the specified max matching times
        if reference.get_matching_times() >= max_matching_times:
            detection_truth = True
        else:
            query_img = reference.get_image()
            features1, des1 = orb.detectAndCompute(query_img, None)
            matches = bf.knnMatch(des1, des2, k=2)

            # Nearest neighbour ratio test to find good matches
            good = []
            good_without_lists = []
            matches = [match for match in matches if len(match) == 2]
            for m, n in matches:
                if m.distance < 0.8 * n.distance:
                    good.append([m])
                    good_without_lists.append(m)

            if len(good) >= min_acceptable_matches:
                detection_truth = True
                dst_pts = np.float32([features2[m.trainIdx].pt for m in good_without_lists]).reshape(-1, 1, 2)
                reference.set_location(dst_pts[2][0][1], dst_pts[2][0][0])
                reference.increase_matching()
            #else:
            #    print('Not enough good matches are found - {}/{}'.format(len(good), min_matches))
        ground_truth.increase_by(item_truth, detection_truth)
        i += 1

@njit
def grayscale(image, y_start=0, y_end=0, x_start=0, x_end=0):
    new_image = zeros(image.shape, uint8)
    __WR, __WG, __WB = 0.299, 0.587, 0.114

    for y in range(y_start, image.shape[0]-y_end):
        for x in range(x_start, image.shape[1]-x_end):
            i = (__WB * image[y, x, 0]) + \
                (__WG * image[y, x, 1]) + \
                (__WR * image[y, x, 2])
            for c in range(image.shape[2]):
                new_image[y, x, c] = i
    return new_image