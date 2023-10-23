import unittest, random

from mystery_3 import mystery_3

# from experiment, it was seen that mystery_3 sort the list and return it, leaving the original list empty
# some glass box test added after formatting the function

class TestMystery_1(unittest.TestCase):
    def is_sorted(self, l:list):
        return all(l[i] <= l[i + 1] for i in range(len(l) - 1))

    def test_0(self):
        """tests empty list"""
        self.assertEqual(mystery_3([]),[])

    def test_1(self):
        """tests 1 element list"""
        self.assertEqual(mystery_3([1]),[1])

    def test_2(self):
        """tests some list"""
        self.assertEqual(mystery_3([1,0,10,4,2]),[0,1,2,4,10])

    def test_3(self):
        """tests some list"""
        self.assertEqual(mystery_3([1.0,0.0,10.0,4.0,2.0]),[0.0,1.0,2.0,4.0,10.0])

    def test_4(self):
        """tests some list"""
        self.assertEqual(mystery_3([100.0,-4,346,0,7,2,10]),[-4,0,2,7,10,100.0,346])

    def test_5(self):
        """tests list with chars"""
        self.assertEqual(mystery_3(['e','f','l','a','b','z']),['a','b','e','f','l','z'])

    def test_6(self):
        """tests big list with numbers"""
        self.assertEqual(mystery_3([5,1,7,4,-8,0,1,-1,1,1,1,-500,0,3,89,22,2,0,-5,-4,0,2,7,10,100.0,346,1,0,10,4,2,1.1e10,5e-10,5e5,9e-20,-7e16,8e100,6,2,7,4453,854678457,23,7,5,8,2,1,1,-634,-7457,-6346346,23,56,634]),[-7e+16, -6346346, -7457, -634, -500, -8, -5, -4, -1, 0, 0, 0, 0, 0, 9e-20, 5e-10, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7, 7, 7, 8, 10, 10, 22, 23, 23, 56, 89, 100.0, 346, 634, 4453, 500000.0, 854678457, 11000000000.0, 8e+100])

    def test_7(self):
        """test that original list cleared"""
        L=[5,1,7,4,-8,0,1,-1,1,1,1,-500,0,3,89,22,2,0,-5,-4,0,2,7,10,100.0,346,1,0,10,4,2,1.1e10,5e-10,5e5,9e-20,-7e16,8e100,6,2,7,4453,854678457,23,7,5,8,2,1,1,-634,-7457,-6346346,23,56,634]
        L_sort=mystery_3(L)
        self.assertTrue(self.is_sorted(L_sort))
        self.assertTrue(L==[])

    def test_8(self):
        """test random list"""
        L=[random.randint(-10000000,-10000000) for _ in range(800)]
        #
        #  !!!   it seems mystery_3 uses recustion, so with  L=[random.randint(-10000000,-10000000) for _ in range(1000)]
        #        random list len>1000 it rasies max depth recursion error
        #
        L_copy=L.copy()
        L=mystery_3(L)
        self.assertTrue(sorted(L_copy)==L)

    # glass box testing

    def test_assert1(self):
        '''test assetions that L1 is list'''
        with self.assertRaises(AssertionError):
            mystery_3(4)

    def test_assert2(self):
        '''test assetions that L2 is list'''
        with self.assertRaises(AssertionError):
            mystery_3([4],5)


    def test_9(self):
        """test with L2"""
        self.assertEqual(mystery_3([],['e', 'f', 'l', 'a', 'b', 'z']), ['e', 'f', 'l', 'a', 'b', 'z'])

    def test_10(self):
        """test L1 sorted is appended to L2"""
        self.assertEqual(mystery_3(['e', 'f', 'l', 'a', 'b', 'z'],[1,0,10,4,2]), [1,0,10,4,2,'a', 'b', 'e', 'f', 'l', 'z'])


if __name__ == "__main__":
    unittest.main()