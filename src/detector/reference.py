from detector.image_processing import grayscale, histogram


class Reference:

    def __init__(self, image, bins=256, y_start=0, y_end=0, x_start=0, x_end=0):
        grey = grayscale(image, y_start, y_end, x_start, x_end)
        self.__h_ref, self.__b_ref = histogram(grey, bins)
        self.__bins = bins
        self.__image = grey
        self.__matching_times = 0
        self.__last_y = 0
        self.__last_x = 0

    def get_histogram(self):
        return self.__h_ref, self.__b_ref

    def get_bins(self):
        return self.__bins

    def get_image(self):
        return self.__image

    def set_location(self, y, x):
        self.__last_y = y
        self.__last_x = x

    def get_location(self):
        return self.__last_y, self.__last_x

    def increase_matching(self):
        self.__matching_times += 1

    def get_matching_times(self):
        return self.__matching_times



