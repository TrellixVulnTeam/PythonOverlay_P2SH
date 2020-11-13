from numba import njit
from numba.typed import List


@njit
def is_even(n):
    return n % 2 == 0


@njit
def is_odd(n):
    return n % 2 == 1


@njit
def absolute(n):
    if n < 0:
        n = -n
    return n


@njit
def absolutes(array):
    return [absolute(i) for i in array]


@njit
def dot_product(v1, v2):
    s = 0
    for i in range(len(v1)):
        s += v1[i] * v2[i]
    return s


@njit
def vector_length(v1):
    s = 0
    for i in range(len(v1)):
        s += v1[i] ** 2
    return abs(square_root(s))


# https://ourcodeworld.com/articles/read/884/how-to-get-the-square-root-of-a-number-without-using-the-sqrt-function-in-c
@njit
def square_root(n):
    sqrt = n / 2
    temp = 0

    while sqrt != temp:
        temp = sqrt
        sqrt = (n / temp + temp) / 2;
    return sqrt


@njit
def summation(array):
    s = 0
    for i in array:
        s += i
    return s


@njit
def max_value(array):
    m = array[0]
    for a in array:
        if a > m:
            m = a
    return m


@njit
def max_index(array):
    i, index = 0, 0
    m = array[i]
    for a in array:
        if a > m:
            m = a
            i = index
        index += 1

    return index


@njit
def min_value(array):
    m = array[0]
    for a in array:
        if a < m:
            m = a
    return m


@njit
def mean(array):
    return summation(array) / len(array)


@njit
def percent_out_of(total, n):
    return (total - n) / total


@njit
def standard_deviation(array):
    m = mean(array)
    s = List()
    [s.append((a - m) ** 2) for a in array]
    return square_root(summation(s) / len(array))
