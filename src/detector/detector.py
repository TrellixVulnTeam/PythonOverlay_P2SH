from cv2 import rectangle
from detector.image_processing import grayscale, histogram_reference_match


# The ROI of the target image, that should be matched
y_start, y_end = 930, 45
x_start, x_end = 1084, 638


# The acceptable deviation between histogram matches
acceptable_deviation = 0.04


# The match rectangles border color
rect_border_color = (150, 0, 0)
# And its border thickness
rect_border_thickness = 2


# The number of times a reference should be found before
# we decide a final location
max_matching_times = 1


# Executed after running the frame check
def after_frame_check(frame, references):
    # loop through the references
    for reference in references:
        if reference.get_matching_times() >= max_matching_times:
            ref_image = reference.get_image()
            y, x = reference.get_location()
            # draw a rectangle around the matching area using the reference's size
            p1, p2 = (x, y), (x + ref_image.shape[1], y + ref_image.shape[0])
            rectangle(frame, p1, p2, color=rect_border_color, thickness=rect_border_thickness)


# Used to grayscale and match a frame against the given references
def frame_check(frame, references):
    # grayscale the given frame at the ROI
    frame_gray = grayscale(frame, y_start, y_end, x_start, x_end)

    # loop through the references
    for reference in references:

        # continue to the next iteration of the loop
        # if the reference's matching times exceeded
        # the specified max matching times
        if reference.get_matching_times() >= max_matching_times:
            continue

        # get the reference's image data
        ref_image, bins = reference.get_image(), reference.get_bins()
        h_ref, b_ref = reference.get_histogram()
        # test the current reference against the grayscale frame
        match, h_temp, b_temp, y, x = histogram_reference_match(frame_gray, ref_image, h_ref, b_ref, bins,
                                                                acceptable_deviation, y_start, y_end, x_start, x_end)

        # if there is a match between the frame and current reference
        if match:
            # increase matching times
            reference.increase_matching()
            # and save matching location
            reference.set_location(y, x)

