from numba import njit
from numpy import zeros
from numpy import uint8


@njit
def process(other, binary_reference, y_start, y_end, x_start, x_end, t=50):
    # Define an empty image with one color channel
    binary = __empty_image(other, color_channels=1)

    # Define y, and x range
    y_range, x_range = range(y_start, other.shape[0] - y_end), \
                       range(x_start, other.shape[1] - x_end)

    # threshold the image
    [__set_threshold(binary, other, y, x, t) for y in y_range for x in x_range]

    # get matching coordinates
    matching_pixel = binary_reference[0, 0, 0]
    coordinates = [(y, x) for y in y_range for x in x_range if binary[y, x, 0] == matching_pixel]

    # return binary image and matching
    # coordinates to the caller
    return binary, coordinates


@njit
def match(binary, binary_reference, coordinates):
    # Define y, and x range
    y_range, x_range = range(binary_reference.shape[0]), \
                       range(binary_reference.shape[1])

    binary_array = [binary_reference[y, x, 0] for y in y_range for x in x_range]

    # check if any of the matching coordinates
    # match the binary array of pixels
    res = [(c) for c in coordinates if
           [binary[c[0] + y, c[1] + x, 0] for y in y_range for x in x_range] == binary_array]

    # return the min and max range if
    # a match was found
    return res


@njit
def to_binary(image, y_start, y_end, x_start, x_end, t=70):
    # Define an empty image with one color channel
    binary = __empty_image(image, color_channels=1)

    # Define y, and x range
    y_range, x_range = range(y_start, image.shape[0] - y_end), \
                       range(x_start, image.shape[1] - x_end)

    # threshold the image
    [__set_threshold(binary, image, y, x, t) for y in y_range for x in x_range]

    # return the binary image to the caller
    return binary

@njit
def _to_binary(image, y_ranges, x_ranges, t=70):
    # Define an empty image with one color channel
    binary = __empty_image(image, color_channels=1)

    # Define y, and x ranges
    _y_ranges = [range(r[0], image.shape[0] - r[1]) for r in y_ranges]
    _x_ranges = [range(r[0], image.shape[1] - r[1]) for r in x_ranges]

    # threshold the image
    [[__set_threshold(binary, image, y, x, t) for y in y_range for x in x_range]
        for y_range in _y_ranges for x_range in _x_ranges]

    # return the binary image to the caller
    return binary


@njit
def blob_analysis(binary, y_start, y_end, x_start, x_end):
    # Define y, and x range
    y_range, x_range = range(y_start, binary.shape[0] - y_end), \
                       range(x_start, binary.shape[1] - x_end)

    label = 10
    for y in y_range:
        for x in x_range:
            if binary[y, x] == 255:
                __fire_grass(binary, y, x, label)
                label += 10
    print(label)
    return binary


@njit
def __fire_grass(image, y, x, label):
    image[y, x] = label

    y_list = [y]
    x_list = [x]

    conditions = [False] * 8
    coordinates = [(0,0)] * 8
    #blob = Blob(y, x, label)
    #blob.yx.append((y, x))
    # Loop while the length of the y list
    # is greater than zero
    while len(y_list) > 0:

        y = y_list.pop(0)
        x = x_list.pop(0)

        conditions[0] = y > 0
        coordinates[0] = ((y - 1), x)  # top

        conditions[1] = x > 0
        coordinates[1] = (y, (x - 1))  # left

        conditions[2] = x < image.shape[1] - 1
        coordinates[2] = (y, (x + 1))  # right

        conditions[3] = y < image.shape[0] - 1
        coordinates[3] = ((y + 1), x)  # bottom

        conditions[4] = y < image.shape[0] - 1 and x > 0
        coordinates[4] = ((y + 1), (x - 1))  # bottom-left

        conditions[5] = y < image.shape[0] - 1 and x < image.shape[1] - 1
        coordinates[5] = ((y + 1), (x + 1))  # bottom-right

        conditions[6] = y > 0 and x > 0
        coordinates[6] = ((y - 1), (x - 1))  # top-left

        conditions[7] = y < image.shape[0] - 1 and x < image.shape[1] - 1
        coordinates[7] = ((y + 1), (x + 1))  # top-right

        i = 0
        for coordinate in coordinates:
            if conditions[i] and image[coordinate[0], coordinate[1]] == 255:
                image[coordinate[0], coordinate[1]] = label
                y_list.append(coordinate[0])
                x_list.append(coordinate[1])
                i += 1
        """
        if y > 0 and image[top[0], top[1]] == 255:
            image[top[0], top[1]] = label
            y_list.append(top[0])
            x_list.append(top[1])
            #blob.y_list.append(top.y)
            #blob.x_list.append(top.x)
            #blob.yx.append((top.y, top.x))

        if y < image.shape[0] - 1 and image[bottom[0], bottom[1]] == 255:
            image[bottom[0], bottom[1]] = label
            y_list.append(bottom[0])
            x_list.append(bottom[1])
            #blob.y_list.append(bottom.y)
            #blob.x_list.append(bottom.x)
            #blob.yx.append((bottom.y, bottom.x))

        if x > 0 and image[left[0], left[1]] == 255:
            image[left[0], left[1]] = label
            y_list.append(left[0])
            x_list.append(left[1])
            #blob.y_list.append(left.y)
            #blob.x_list.append(left.x)
            #blob.yx.append((left.y, left.x))

        if x < image.shape[1] - 1 and image[right[0], right[1]] == 255:
            image[right[0], right[1]] = label
            y_list.append(right[0])
            x_list.append(right[1])
            #blob.y_list.append(right.y)
            #blob.x_list.append(right.x)
            #blob.yx.append((right.y, right.x))
    #return blob
"""

@njit
def __set_threshold(binary, image, y, x, t):
    # threshold the image based on intensity
    binary[y, x, 0] = 0 if __get_intensity(image, y, x) < t else 255


@njit
def __get_intensity(image, y, x):
    # returns the value of (w_r*r + w_g*g + w_b*b)
    return (0.114 * image[y, x, 0]) + (0.587 * image[y, x, 1]) + (0.299 * image[y, x, 2])


@njit
def __empty_image(image, color_channels=1):
    # specify the empty image's size
    size = (image.shape[0], image.shape[1], color_channels)
    # return an empty image to the caller
    return zeros(size, uint8)
