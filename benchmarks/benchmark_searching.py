import sys
import os

# Add the parent directory to sys.path to make imports work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from searching.search import SearchAlgorithms
from sorting.sorting import SortingAlgorithms
import timeit
import random

def benchmark_search_algorithms():
    sizes = [100, 1000, 5000, 10000]
    for size in sizes:
        # Generate an array of random integers
        arr = [random.randint(0, 10000) for _ in range(size)]
        target = random.randint(0, 10000)

        print(f"\nBenchmarking with input size: {size}")

        # Linear Search Benchmark
        linear_search_time = timeit.timeit(lambda: SearchAlgorithms.linear_search(arr, target), number=1)
        print(f"Linear Search Time: {linear_search_time:.6f} seconds")

        # Sort the array for Binary Search
        SortingAlgorithms.quick_sort(arr, 0, len(arr) - 1)

        # Binary Search Benchmark
        binary_search_time = timeit.timeit(lambda: SearchAlgorithms.binary_search(arr, target), number=1)
        print(f"Binary Search Time: {binary_search_time:.6f} seconds")

if __name__ == "__main__":
    benchmark_search_algorithms()
