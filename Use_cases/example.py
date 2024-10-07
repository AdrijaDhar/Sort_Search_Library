import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms import SortingAlgorithms, SearchAlgorithms

# Original array to demonstrate sorting and searching
arr = [34, 7, 23, 32, 5, 62]

# Sorting Example
print("Original Array:", arr)
SortingAlgorithms.quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array using Quick Sort:", arr)

# Searching Example
target = 23
index = SearchAlgorithms.binary_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in the array")
