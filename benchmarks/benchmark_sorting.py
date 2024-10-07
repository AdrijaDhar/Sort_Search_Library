import sys
import os
import random
import time
import pandas as pd

# Add the parent directory to the system path to resolve module import issues
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sorting.sorting import SortingAlgorithms

# Define paths to save benchmark results
results_folder = "results"
os.makedirs(results_folder, exist_ok=True)
benchmark_results_path = os.path.join(results_folder, "sorting_benchmark_results.md")

# Input sizes to benchmark
input_sizes = [100, 1000, 5000, 10000]

# Sorting algorithms to benchmark
sorting_algorithms = [
    "bubble_sort",
    "merge_sort",
    "quick_sort",
    "selection_sort",
    "insertion_sort",
    "heap_sort",
    "counting_sort",
    "radix_sort",
    "shell_sort",
    "bucket_sort",
    "cocktail_shaker_sort",
    "comb_sort",
    "gnome_sort",
    "tim_sort",
    "pancake_sort",
    "tree_sort"
]

# Dictionary to hold benchmark results
benchmark_results = {algorithm: [] for algorithm in sorting_algorithms}
benchmark_results["Input Size"] = input_sizes

# Benchmark each algorithm
for size in input_sizes:
    # Generate a random list of the given size
    array = [random.randint(0, 10000) for _ in range(size)]

    for algorithm in sorting_algorithms:
        # Make a copy of the array for each run
        arr_copy = array.copy()

        # Get the sorting function by name
        sort_function = getattr(SortingAlgorithms, algorithm)

        # Benchmark the sorting function
        start_time = time.time()
        sort_function(arr_copy)
        end_time = time.time()

        # Record the time taken
        time_taken = end_time - start_time
        benchmark_results[algorithm].append(time_taken)

# Convert the results to a DataFrame for easy handling and saving
benchmark_df = pd.DataFrame(benchmark_results)

# Save the benchmark results as a markdown file
benchmark_df.to_markdown(benchmark_results_path, index=False)

# Print benchmark results
print(benchmark_df)
