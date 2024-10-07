import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sorting.sorting import SortingAlgorithms
import timeit
import random

def benchmark_sorting_algorithms():
    sizes = [100, 1000, 5000, 10000]
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        print(f"\nBenchmarking with input size: {size}")

        # Quick Sort
        quick_sort_time = timeit.timeit(lambda: SortingAlgorithms.quick_sort(arr.copy()), number=1)
        print(f"Quick Sort Time: {quick_sort_time:.6f} seconds")

        # Merge Sort
        merge_sort_time = timeit.timeit(lambda: SortingAlgorithms.merge_sort(arr.copy()), number=1)
        print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")

        # Bubble Sort
        bubble_sort_time = timeit.timeit(lambda: SortingAlgorithms.bubble_sort(arr.copy()), number=1)
        print(f"Bubble Sort Time: {bubble_sort_time:.6f} seconds")

if __name__ == "__main__":
    benchmark_sorting_algorithms()
