import unittest
from simple_math import mat
from numba.typed import List


class MatTestCase(unittest.TestCase):

    def test_absolute(self):
        a = mat.absolute(-1)
        self.assertEqual(a, 1)

    def test_absolutes(self):
        array = mat.absolutes(List([-1, -2, -3]))
        self.assertEqual(array, [1, 2, 3])

    def test_min_value(self):
        m = mat.min_value(List([-1, -2, 4, 2]))
        self.assertEqual(m, -2)

    def test_max_value(self):
        m = mat.max_value(List([-1, -2, 4, 2]))
        self.assertEqual(m, 4)

    def test_summation(self):
        m = mat.summation(List([1, 1, 1, 1]))
        self.assertEqual(m, 4)

    def test_is_even(self):
        self.assertEqual(mat.is_even(2), True)
        self.assertEqual(mat.is_even(4), True)
        self.assertEqual(mat.is_even(5), False)

    def test_is_odd(self):
        self.assertEqual(mat.is_odd(1), True)
        self.assertEqual(mat.is_odd(3), True)
        self.assertEqual(mat.is_odd(4), False)

    def test_dot_product(self):
        d = mat.dot_product(List([1, 2, 3, 4]), List([-1, -2, 4, 2]))
        self.assertEqual(d, 15)

    def test_vector_length(self):
        l = mat.vector_length(List([12, 22, 3333, 4214]))
        self.assertEqual(l, 5372.83100422859)

    def test_square_root(self):
        sqrt = mat.square_root(3)
        self.assertEqual(sqrt, 1.7320508075688772)

    def test_mean(self):
        m = mat.mean(List([1, 2, 3, 4]))
        self.assertEqual(m, 2.5)

    def test_percent_out_of(self):
        p = mat.percent_out_of(100, 50)
        self.assertEqual(p, 0.5)

    def test_standard_deviation(self):
        d = mat.standard_deviation(List([1, 2, 3, 4]))
        self.assertEqual(d, 1.118033988749895)


if __name__ == '__main__':
    unittest.main()
