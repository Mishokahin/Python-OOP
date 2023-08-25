from projects.extended_list import IntegerList

import unittest


class IntegerListTests(unittest.TestCase):
    def test_correct_initialization(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], integer_list.get_data())

    def test_list_only_takes_integers(self):
        integer_list = IntegerList(1, "2", 3.0, False)
        self.assertEqual([1], integer_list.get_data())

    def test_adding_int_value(self):
        integer_list = IntegerList(1, 2, 3)
        integer_list.add(4)
        self.assertEqual([1, 2, 3, 4], integer_list.get_data())

    def test_adding_non_int_value(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as ve:
            integer_list.add("4")
        self.assertEqual("Element is not Integer", ve.exception.args[0])

    def test_successful_element_removal(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual(1, integer_list.remove_index(0))

    def test_element_removal_index_out_of_range(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ie:
            integer_list.remove_index(len(integer_list.get_data()) + 1)
        self.assertEqual("Index is out of range", ie.exception.args[0])

    def test_successful_element_insertion(self):
        integer_list = IntegerList(1, 2, 4)
        integer_list.insert(2, 3)
        self.assertEqual([1, 2, 3, 4], integer_list.get_data())

    def test_element_insertion_index_out_of_range(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ie:
            integer_list.insert(5, 4)
        self.assertEqual("Index is out of range", ie.exception.args[0])

    def test_element_insertion_non_int_value(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as ve:
            integer_list.insert(2, "4")
        self.assertEqual("Element is not Integer", ve.exception.args[0])

    def test_get_biggest(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual(3, integer_list.get_biggest())

    def test_get_index(self):
        integer_list = IntegerList(1, 2, 3)
        self.assertEqual(0, integer_list.get_index(1))


if __name__ == "__main__":
    unittest.main()