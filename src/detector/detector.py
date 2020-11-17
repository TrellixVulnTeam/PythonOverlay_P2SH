from detector.image_processing import grayscale
import cv2
import numpy as np

# The ROI of the target image, that should be matched
y_start, y_end = 930, 35
x_start, x_end = 1084, 630


# The acceptable deviation between histogram matches
acceptable_deviation = 0.08


# The match rectangles border color
rect_border_color = (150, 0, 0)
# And its border thickness
rect_border_thickness = 5


# The number of times a reference should be found before
# we decide a final location
max_matching_times = 1

# https://stackoverflow.com/questions/51591456/can-i-use-rgb-in-tkinter
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


# Executed after running the frame check
def after_frame_check(frame, args):

    references = args['references']
    page = args['page']
    labels = page.item_labels

    # loop through the references
    i = 0
    for reference in references:
        if reference.get_matching_times() >= max_matching_times:
            y, x = reference.get_location()
            # draw a rectangle around the matching area using the reference's size
            p1, p2 = (int(x), int(y)), (int(x + 10), int(y + 10))
            cv2.putText(frame, f'{i}', p1, color=reference.get_color(), fontFace=cv2.FONT_HERSHEY_SIMPLEX, thickness=2, fontScale=1)
            #cv2.rectangle(frame, p1, p2, color=reference.get_color(), thickness=rect_border_thickness)
            if page.is_active:
                labels[i].configure(bg=_from_rgb(reference.get_color()))
        i += 1


# Used to grayscale and match a frame against the given references
def frame_check(frame, args):
    min_matches = 10
    frame_gray = grayscale(frame, y_start, y_end, x_start, x_end)

    references = args['references']

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

    for reference in references:

        # continue to the next iteration of the loop
        # if the reference's matching times exceeded
        # the specified max matching times
        if reference.get_matching_times() >= max_matching_times:
            continue

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

        if len(good) >= min_matches:
            dst_pts = np.float32([features2[m.trainIdx].pt for m in good_without_lists]).reshape(-1, 1, 2)
            reference.set_location(dst_pts[2][0][1], dst_pts[2][0][0])
            reference.increase_matching()
        #else:
        #    print('Not enough good matches are found - {}/{}'.format(len(good), min_matches))


