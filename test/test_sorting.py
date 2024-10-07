import unittest
from sorting.sorting import SortingAlgorithms

class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        array = [64, 34, 25, 12, 22, 11, 90]
        SortingAlgorithms.bubble_sort(array)
        self.assertEqual(array, [11, 12, 22, 25, 34, 64, 90])

    def test_merge_sort(self):
        array = [12, 11, 13, 5, 6, 7]
        SortingAlgorithms.merge_sort(array)
        self.assertEqual(array, [5, 6, 7, 11, 12, 13])

    def test_quick_sort(self):
        array = [10, 7, 8, 9, 1, 5]
        SortingAlgorithms.quick_sort(array)
        self.assertEqual(array, [1, 5, 7, 8, 9, 10])

if __name__ == '__main__':
    unittest.main()
