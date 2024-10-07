import sys
import os

# Add the project root to sys.path so Python can find the modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sorting.sorting import SortingAlgorithms
from searching.search import SearchAlgorithms

# Example with Sorting
array = [34, 7, 23, 32, 5, 62]

# Bubble Sort
SortingAlgorithms.bubble_sort(array)
print("Sorted Array using Bubble Sort:", array)

# Reset array to original state
array = [34, 7, 23, 32, 5, 62]

# Selection Sort
SortingAlgorithms.selection_sort(array)
print("Sorted Array using Selection Sort:", array)

# Example with Searching
sorted_array = [5, 7, 23, 32, 34, 62]

# Jump Search
target = 32
index_jump = SearchAlgorithms.jump_search(sorted_array, target)
if index_jump != -1:
    print(f"Element {target} found at index {index_jump} using Jump Search")
else:
    print(f"Element {target} not found in the array using Jump Search")

# Interpolation Search
index_interp = SearchAlgorithms.interpolation_search(sorted_array, target)
if index_interp != -1:
    print(f"Element {target} found at index {index_interp} using Interpolation Search")
else:
    print(f"Element {target} not found in the array using Interpolation Search")
