import unittest
import random

from collections_filter_1 import collections_filter_1


# from experiment, it was found that collections_filter_1 get as input a list of lists and a value,
# and return list of lists from input, containing this value
# some glass box test added after formatting the function

class TestCollectionsFilter1(unittest.TestCase):
    """
    A unittest test case for the 'collections_filter_1' function.

    This test case covers a variety of scenarios to ensure the correctness of the 'collections_filter_1' function,
    which is expected to take a list of lists, iterables, or sets or strings, along with a value, and return a list of
    collections from the input that contain the specified value.

    It contains tests and assertion tests.
    """

    def test_0(self):
        """tests empty list"""
        self.assertEqual(collections_filter_1([], 0), [])

    def test_1(self):
        """tests 1 element list"""
        self.assertEqual(collections_filter_1([[1]], 1), [[1]])

    def test_11(self):
        """tests 1 element list no match"""
        self.assertEqual(collections_filter_1([[1]], 2), [])

    def test_12(self):
        """tests list with empty lists"""
        self.assertEqual(collections_filter_1([[], [], [], []], 5), [])

    def test_2(self):
        """tests some lists"""
        self.assertEqual(collections_filter_1([[1, 0, 10, 4, 2], [1, 5], [-5, 1, 2]], 2), [[1, 0, 10, 4, 2], [-5, 1, 2]])

    def test_3(self):
        """tests some lists with no match"""
        self.assertEqual(collections_filter_1([[1.0], [0.0], [10.0], [4.0, 5], [2.0, 6, 7]], 648), [])

    def test_4(self):
        """tests some list"""
        self.assertEqual(collections_filter_1([[100.0, -4], [346, 0, 7, 2, 10, -4], [0, 2], [7, 10, 100.0, 346]], 2),
                         [[346, 0, 7, 2, 10, -4], [0, 2]])

    def test_6(self):
        """tests two big lists with numbers"""
        self.assertEqual(
            collections_filter_1([[5, 1, 7, 4, -8, 0, 1, -1, 1, 1, 1, -500, 0, 3, 89, 22, 2, 0, -5, -4, 0, 2, 7,
                                 10, 100.0, 346, 1, 0, 10, 4, 2, 1.1e10, 5e-10, 5e5, 9e-20, -7e16, 8e100, 6, 2,
                                 7, 4453, 854678457, 23, 7, 5, 8, 2, 1, 1, -634, -7457, -6346346, 23, 56, 634],
                                [-7e+16, -6346346, -7457, -634, -500, -8, -5, -4, -1, 0, 0, 0, 0, 0, 9e-20,
                                 5e-10, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7, 7, 7, 8,
                                 9, 10, 10, 22, 23, 23, 56, 89, 100.0, 346, 634, 4453, 500000.0, 854678457,
                                 11000000000.0, 8e+100]], 9),
            [[-7e+16, -6346346, -7457, -634, -500, -8, -5, -4, -1, 0, 0, 0, 0, 0, 9e-20, 5e-10, 1, 1, 1, 1,
              1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 10, 10, 22, 23, 23, 56, 89,
              100.0, 346, 634, 4453, 500000.0, 854678457, 11000000000.0, 8e+100]])

    def test_7(self):
        """test that list is not processed in place"""
        L = [[5, 1, 7, 4, -8, 0, 1, -1, 1, 1, 1, -500, 0, 3, 89, 22, 2, 0], [-5, -4, 0, 2], [7, 10, 100.0, 346, 1], [0],
             [10, 4, 2, 1.1e10, 5e-10, 5e5, 9e-20, -7e16, 8e100], [6, 2, 7], [4453, 854678457, 23, 7],
             [5, 8, 2, 1, 1, -634, -7457, -6346346, 23, 56, 634]]
        L_copy = L.copy()
        collections_filter_1(L, 1)
        self.assertTrue(L == L_copy)

    def test_8(self):
        """test random list"""
        element = random.randint(-10000000, 10000000)
        L = []
        L_with_el = []

        for i in range(10, random.randint(20, 100)):
            L.append([random.randint(-10000000, 10000000) for _ in range(random.randint(1, 1000))])
            # we must understand there is a chance element will be added to L[i] here

        for i in range(len(L)):
            if random.randint(0, 3) == 1:
                L[i].insert(random.randint(0, len(L[i])), element)
            if random.randint(0, 10) == 1:
                L[i].insert(random.randint(0, len(L[i])), element)
            # we add if, to check if element was already in L[i] (even if it was not added by these ifs)
            if element in L[i]:
                L_with_el.append(L[i])

        self.assertTrue(collections_filter_1(L, element) == L_with_el)

    ## ---glass box tests (added after formatting function)

    def test_15(self):
        '''test for sting list'''
        self.assertEqual(collections_filter_1(['abc', 'a', 'bcde', 'sdgbdsdc'], 'b'), ['abc', 'bcde', 'sdgbdsdc'])

    def test_16(self):
        '''test for sting list and substring'''
        self.assertEqual(collections_filter_1(['abc', 'a', 'bdcde', 'sdgbdsdc', 'fsd'], 'bd'), ['bdcde', 'sdgbdsdc'])

    def test_22(self):
        """tests with tuples"""
        self.assertEqual(collections_filter_1([(1, 0, 10, 4, 2), (1, 5), (-5, 1, 2)], 2), [(1, 0, 10, 4, 2), (-5, 1, 2)])

    def test_23(self):
        """tests with tuples with no match"""
        self.assertEqual(collections_filter_1([(1.0,), (0.0,), (10.0,), (4.0, 5), (2.0, 6, 7)], 648), [])

    def test_24(self):
        """tests with sets"""
        self.assertEqual(collections_filter_1([{100.0, -4}, {346, 0, 7, 2, 10, -4}, {0, 2}, {7, 10, 100.0, 346}], 2),
                         [{346, 0, 7, 2, 10, -4}, {0, 2}])

    def test_25(self):
        """tests with sets with no match"""
        self.assertEqual(collections_filter_1([{1.0, }, {0.0, }, {10.0, }, {4.0, 5}, {2.0, 6, 7}], 648), [])

    def test_assert1(self):
        """test L assertion is list of iterables"""
        with self.assertRaises(AssertionError):
            collections_filter_1([4, 5], 3)

    def test_assert2(self):
        """test L assertion is list of iterables"""
        with self.assertRaises(AssertionError):
            collections_filter_1([4, 5, 6], 's')

    def test_assert3(self):
        """test L assertion is list of str and elem must be string"""
        with self.assertRaises(AssertionError):
            collections_filter_1(['fdfg', 'sdgsdg', 'dfd'], 3)


if __name__ == "__main__":
    unittest.main()
