import unittest
from sorting.sorting import SortingAlgorithms

class TestSorting(unittest.TestCase):
    def run_sort_test(self, algorithm, array, expected):
        sorting_function = getattr(SortingAlgorithms, algorithm)
        sorting_function(array)
        self.assertEqual(array, expected)

    def test_all_sorts(self):
        test_cases = [
            ("bubble_sort", [64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
            ("merge_sort", [12, 11, 13, 5, 6, 7], [5, 6, 7, 11, 12, 13]),
            ("quick_sort", [10, 7, 8, 9, 1, 5], [1, 5, 7, 8, 9, 10]),
            ("selection_sort", [29, 10, 14, 37, 13], [10, 13, 14, 29, 37]),
            ("insertion_sort", [12, 11, 13, 5, 6], [5, 6, 11, 12, 13]),
            ("heap_sort", [4, 10, 3, 5, 1], [1, 3, 4, 5, 10]),
            ("counting_sort", [1, 4, 1, 2, 7, 5, 2], [1, 1, 2, 2, 4, 5, 7]),
            ("radix_sort", [170, 45, 75, 90, 802, 24, 2, 66], [2, 24, 45, 66, 75, 90, 170, 802]),
            ("shell_sort", [12, 34, 54, 2, 3], [2, 3, 12, 34, 54]),
            ("bucket_sort", [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68],
             [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]),
            ("cocktail_shaker_sort", [5, 1, 4, 2, 8, 0, 2], [0, 1, 2, 2, 4, 5, 8]),
            ("comb_sort", [8, 4, 1, 56, 3, -44, 23, -6, 28, 0], [-44, -6, 0, 1, 3, 4, 8, 23, 28, 56]),
            ("gnome_sort", [34, 2, 10, -9], [-9, 2, 10, 34]),
            ("tim_sort", [5, 21, 7, 23, 19], [5, 7, 19, 21, 23]),
            ("pancake_sort", [10, 5, 7, 3, 2], [2, 3, 5, 7, 10]),
            ("tree_sort", [5, 4, 7, 2, 11], [2, 4, 5, 7, 11]),
        ]

        for algorithm, array, expected in test_cases:
            with self.subTest(algorithm=algorithm):
                self.run_sort_test(algorithm, array, expected)

if __name__ == '__main__':
    unittest.main()
