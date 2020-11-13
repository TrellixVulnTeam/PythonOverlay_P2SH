from numpy import zeros, uint8
from numba.typed import List
from numba import njit
from simple_math.mat import percent_out_of, absolute


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


@njit
def histogram(image, bins=256):
    b, h = List(), List()
    [b.append(i / bins) for i in range(0, bins)]
    [h.append(len([image[y, x] for y in range(image.shape[0])
              for x in range(image.shape[1])
              if i <= image[y, x, 0] <= i + 0.9])) for i in range(0, bins)]
    return h, b


@njit
def histogram_match(h1, h2, a=0.1):
    bins = len(h1)
    match = True
    for n in range(0, bins):
        p1 = percent_out_of(bins, h1[n])
        p2 = percent_out_of(bins, h2[n])
        diff = absolute(p2 - p1)
        if diff > a:
            match = False
            break
    return match


@njit
def histogram_reference_match(image, ref, h_ref, b_ref, bins=256, a=0.1, y_start=0, y_end=0, x_start=0, x_end=0):
    # Define return y
    _y, _x, temp_image = -1, -1, zeros(ref.shape, uint8)
    match = False

    for y in range(y_start, image.shape[0]-ref.shape[0]-y_end):
        for x in range(x_start, image.shape[1]-ref.shape[1]-x_end):

            for ky in range(ref.shape[0]):
                for kx in range(ref.shape[1]):
                    for c in range(image.shape[2]):
                        temp_image[ky, kx, c] = image[y + ky, x + kx, c]

            h_temp, b_temp = histogram(temp_image, bins)
            match = histogram_match(h_temp, h_ref, a)

            if match:
                h_ref, b_ref = h_temp, b_temp
                _y, _x = y, x
                break
        if match:
            break
    return match, h_ref, b_ref, _y, _x

