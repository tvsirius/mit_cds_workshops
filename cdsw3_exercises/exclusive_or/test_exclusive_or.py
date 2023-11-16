import unittest

from exclusive_or import exclusive_or

class TestExclusiveOr(unittest.TestCase):
    """Test the exclusive_or function"""

    def test_exclusive_or_abc_in_list1_not_in_list2(self):
        """Test if 'abc' is in list1 and not in list2"""
        self.assertTrue(exclusive_or('abc', ['a', 'b', 'abc'], ['b', 'd', 'v']))

    def test_exclusive_or_abc_in_list2_not_in_list1(self):
        """Test if 'abc' is in list2 and not in list1"""
        self.assertTrue(exclusive_or('abc', ['a', 'b', 'agg'], ['b', 'd', 'abc', 'v']))

    def test_exclusive_or_abc_in_both_lists(self):
        """Test if 'abc' is in both lists"""
        self.assertFalse(exclusive_or('abc', ['a', 'b', 'ac'], ['b', 'd', 'v', '11']))

    def test_exclusive_or_abc_in_both_lists_with_common_elements(self):
        """Test if 'abc' is in both lists with common elements"""
        self.assertFalse(exclusive_or('abc', ['a', 'b', 'abc'], ['b', 'abc', 'd', 'v', '11']))

    def test_exclusive_or_abc_in_list1_empty_list2(self):
        """Test if 'abc' is in list1 and list2 is empty"""
        self.assertTrue(exclusive_or('abc', ['a', 'b', 'abc'], []))

    def test_exclusive_or_abc_in_list2_empty_list1(self):
        """Test if 'abc' is in list2 and list1 is empty"""
        self.assertTrue(exclusive_or('abc', [], ['b', 'd', 'abc', 'v']))

    def test_exclusive_or_abc_in_both_empty_lists(self):
        """Test if 'abc' is in both empty lists"""
        self.assertFalse(exclusive_or('abc', [], []))

    def test_exclusive_or_abc_in_list1_with_single_element(self):
        """Test if 'abc' is in list1 with single element"""
        self.assertTrue(exclusive_or('abc', ['abc'], ['b']))

    def test_exclusive_or_abc_in_list2_with_single_element(self):
        """Test if 'abc' is in list2 with single element"""
        self.assertTrue(exclusive_or('abc', ['a'], ['abc']))

    def test_exclusive_or_empty_string_in_both_lists(self):
        """Test if empty string is in both lists"""
        self.assertTrue(exclusive_or('', ['a', 'b', ''], ['b', 'd', 'v']))

    def test_exclusive_or_empty_string_in_list2_with_empty_string(self):
        """Test if empty string is in list2 with empty string"""
        self.assertFalse(exclusive_or('', ['a', 'b', ''], ['b', 'd', '', 'v']))

    def test_exclusive_or_empty_string_in_both_lists_with_non_empty_string(self):
        """Test if empty string is in both lists with non-empty string"""
        self.assertFalse(exclusive_or('', ['a', 'b', 'ac'], ['b', 'd', 'v', '11']))

    def test_exclusive_or_empty_string_in_list2_with_empty_string_and_non_empty_string(self):
        """Test if empty string is in list2 with empty string and non-empty string"""
        self.assertFalse(exclusive_or('', ['a', 'b', ''], ['b', '', 'd', 'v', '11']))

    def test_exclusive_or_invalid_input_type(self):
        """Test if the function raises a TypeError when the inputs are not of the expected types"""
        with self.assertRaises(AssertionError):
            exclusive_or('abc', ['a', 'b', 'abc'], 'not a list')

    def test_exclusive_or_string_input_type(self):
        """Test if the function raises a TypeError when the first input is not a string"""
        with self.assertRaises(AssertionError):
            exclusive_or(123, ['a', 'b', 'abc'], ['b', 'd', 'v'])
            
    def test_exclusive_or_list_contains_non_string_element(self):
        """Test if the function raises a TypeError when the lists contain non-string elements"""
        with self.assertRaises(AssertionError):
            exclusive_or('abc', ['a', 'b', 123], ['b', 'd', 'v'])

if __name__ == '__main__':
   unittest.main()