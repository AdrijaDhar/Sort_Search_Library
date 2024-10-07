
import sys
import os

# Add the project root to sys.path so Python can find the modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms import SortingAlgorithms, SearchAlgorithms
# Example with Sorting
array = [34, 7, 23, 32, 5, 62]

# Quick Sort
SortingAlgorithms.quick_sort(array)
print("Sorted Array using Quick Sort:", array)

# Reset array to original state
array = [34, 7, 23, 32, 5, 62]

# Merge Sort
SortingAlgorithms.merge_sort(array)
print("Sorted Array using Merge Sort:", array)

# Example with Searching
sorted_array = [5, 7, 23, 32, 34, 62]

# Binary Search
target = 23
index = SearchAlgorithms.binary_search(sorted_array, target)
if index != -1:
    print(f"Element {target} found at index {index} using Binary Search")
else:
    print(f"Element {target} not found in the array using Binary Search")

# Linear Search
index_linear = SearchAlgorithms.linear_search(array, target)
if index_linear != -1:
    print(f"Element {target} found at index {index_linear} using Linear Search")
else:
    print(f"Element {target} not found in the array using Linear Search")
