from numpy import zeros, uint8
from numba import njit


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



