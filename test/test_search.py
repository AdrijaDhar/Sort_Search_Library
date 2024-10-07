import unittest
from searching.search import SearchAlgorithms

class TestSearch(unittest.TestCase):
    def test_linear_search(self):
        array = [2, 3, 4, 10, 40]
        self.assertEqual(SearchAlgorithms.linear_search(array, 10), 3)
        self.assertEqual(SearchAlgorithms.linear_search(array, 5), -1)

    def test_binary_search(self):
        array = [2, 3, 4, 10, 40]
        self.assertEqual(SearchAlgorithms.binary_search(array, 10), 3)
        self.assertEqual(SearchAlgorithms.binary_search(array, 5), -1)

if __name__ == '__main__':
    unittest.main()
