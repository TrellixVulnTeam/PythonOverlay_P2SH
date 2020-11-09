from threading import Thread
from numba.typed import List
from cv2 import waitKey, imshow
from.Detect import process, match, to_binary, blob_analysis, _to_binary
from.DetectionMethod import DetectionMethod


class DetectionReference:

    # Used to determine the area where
    # the reference was found
    min_x, max_x, min_y, max_y = 0, 0, 0, 0

    # Returns true if the reference has
    # been found within the image it was
    # given through the detect method
    match = False

    # The number of threads currently
    # detecting for this reference
    __number_of_threads = 0

    # Number of active threads allowed
    # detecting for this reference
    max_threads = 2

    # The class constructor.
    # Requires an image and a ROI
    def __init__(self, image, roi):
        self.image = to_binary(image, 0, 0, 0, 0)
        self.height = image.shape[0]
        self.width = image.shape[1]
        self.roi = roi

    def async_detect(self, other, method=DetectionMethod.TEMPLATE_MATCHING):
        # cache the number of active threads
        self.__number_of_threads += 1

        # create a new thread with the detect method
        thread = Thread(target=self.detect, args=(other, method))
        # start the thread
        thread.start()

    def detect(self, other, method=DetectionMethod.TEMPLATE_MATCHING):

        if method == DetectionMethod.TEMPLATE_MATCHING:
            self.__template_matching(other)
        elif method == DetectionMethod.BLOB_ANALYSIS:
            self.__blob_analysis(other)

        # Decrease to indicate a thread is done
        # executing this method
        self.__number_of_threads -= 1

    def __template_matching(self, other):
        # Create numba list, that can be used to pass to numba methods
        coordinates = List()

        # Get the binary image and the coordinates as array
        # using the current image, binary reference and a ROI
        binary, coordinates_array = process(other=other, binary_reference=self.image,
                                            y_start=self.roi.y_start, y_end=self.roi.y_end,
                                            x_start=self.roi.x_start, x_end=self.roi.x_end)

        if len(coordinates_array) > 0:
            # Append the coordinates from the array to the list
            [coordinates.append(coordinate) for coordinate in coordinates_array]

            # Check if the binary reference match the binary at the coordinates found
            result = match(binary=binary, binary_reference=self.image, coordinates=coordinates)

            # Check if the returning array has a length greater than zero
            any_matches = len(result) > 0
            if any_matches:
                # save the min and max positions and set match equal true
                self.min_x, self.min_y = result[0][1], result[0][0]
                self.max_x, self.max_y = result[0][1] + self.width, result[0][0] + self.height
                self.match = True

    def __blob_analysis(self, other):
        y_ranges, x_ranges = List(), List()
        [y_ranges.append(r) for r in self.roi.y_ranges]
        [x_ranges.append(r) for r in self.roi.x_ranges]
        binary = _to_binary(image=other, y_ranges=y_ranges, x_ranges=x_ranges)
        binary = blob_analysis(binary, y_start=self.roi.y_start, y_end=self.roi.y_end,
                                       x_start=self.roi.x_start, x_end=self.roi.x_end)
        #imshow('blob', binary)
        #waitKey(0)

    # Used to check if the reference
    # has reached it maximum thread checks
    def can_detect(self):
        return self.__number_of_threads < self.max_threads

    # Used to get the top left corner
    def get_top_left(self):
        return self.min_x, self.min_y

    # Used to get the bottom right corner
    def get_bottom_right(self):
        return self.max_x, self.max_y

