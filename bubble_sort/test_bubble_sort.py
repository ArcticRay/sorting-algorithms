import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_empty_list(self):
        data = []
        bubble_sort(data)
        self.assertEqual(data, [])

    def test_sorted_list(self):
        data = [1, 2, 3, 4, 5]
        bubble_sort(data)
        self.assertEqual(data, [1, 2, 3, 4, 5])

    def test_reverse_list(self):
        data = [5, 4, 3, 2, 1]
        bubble_sort(data)
        self.assertEqual(data, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        data = [3, 1, 4, 1, 5, 9]
        bubble_sort(data)
        self.assertEqual(data, [1, 1, 3, 4, 5, 9])

if __name__ == "__main__":
    unittest.main()
