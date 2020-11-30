"""
    The reference depends on the grayscale method from the detector
"""
from detector.detector import grayscale


class Reference:
    """
        The reference is used to specify an object which primarily consist of an item image,
        with a couple of properties used to indicate whether or not the reference has been
        found within a target image
    """

    def __init__(self, image, roi=(0, 0, 0, 0), color=(150, 0, 0), min_acceptable_matches=10):
        self.min_acceptable_matches = min_acceptable_matches
        # Ensure to grayscale the given image at the ROI
        self.__image = grayscale(image, roi[0], roi[1], roi[2], roi[3])
        # Allow the reference to have its own indication color.
        # Primarily used for debugging.
        self.__color = color
        # Indicates the number of times the references has been
        # matched within a target image
        self.__matching_times = 0
        # The last x and y position the reference has been matched
        # at within a target image
        self.__last_y = 0
        self.__last_x = 0

    def get_color(self):
        """
            Returns the reference's specified color
        """
        return self.__color

    def get_image(self):
        """
           Returns the reference's grayscale image
        """
        return self.__image

    def set_location(self, y_position, x_position):
        """
           Set the x and y position of the
           reference's last matched location
        """
        self.__last_y = y_position
        self.__last_x = x_position

    def get_location(self):
        """
            Returns the last matched location as a tuple (y, x)
        """
        return self.__last_y, self.__last_x

    def increase_matching(self):
        """
           Increase the current number of matching times
        """
        self.__matching_times += 1

    def decrease_matching(self):
        """
           Increase the current number of matching times
        """
        self.__matching_times -= 1

    def reset_matching(self):
        """
           Reset the current number of matching times
        """
        self.__matching_times = 0

    def get_matching_times(self):
        """
           Returns the current number of matching times
        """
        return self.__matching_times

    def get_color_for_tkinter(self):
        """
            https://stackoverflow.com/questions/51591456/can-i-use-rgb-in-tkinter
            Translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % self.__color
