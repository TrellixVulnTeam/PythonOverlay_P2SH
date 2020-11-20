from detector.image_processing import grayscale


class Reference:

    def __init__(self, image, y_start=0, y_end=0, x_start=0, x_end=0, color=(150, 0, 0)):
        self.__image = grayscale(image, y_start, y_end, x_start, x_end)
        self.__color = color
        self.__matching_times = 0
        self.__last_y = 0
        self.__last_x = 0

    def get_color(self):
        return self.__color

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



