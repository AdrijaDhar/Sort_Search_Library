import sys
import os
import random
import time
import pandas as pd
import matplotlib.pyplot as plt

# Add the project root directory to the system path to resolve module import issues
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms import SortingAlgorithms
from algorithms import SearchAlgorithms

# Define paths to save benchmark results
results_folder = "results"
os.makedirs(results_folder, exist_ok=True)
benchmark_sorting_results_path = os.path.join(results_folder, "sorting_benchmark_results_unified.md")
benchmark_searching_results_path = os.path.join(results_folder, "searching_benchmark_results_unified.md")

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

# Searching algorithms to benchmark
searching_algorithms = [
    "linear_search",
    "binary_search",
    "jump_search",
    "interpolation_search",
    "exponential_search",
    "fibonacci_search",
    "ternary_search",
    "sentinel_linear_search",
    "meta_binary_search"
]

# Dictionary to hold sorting benchmark results
sorting_benchmark_results = {algorithm: [] for algorithm in sorting_algorithms}
sorting_benchmark_results["Input Size"] = input_sizes

# Benchmark each sorting algorithm
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
        sorting_benchmark_results[algorithm].append(time_taken)

# Convert the sorting results to a DataFrame for easy handling and saving
sorting_benchmark_df = pd.DataFrame(sorting_benchmark_results)

# Save the sorting benchmark results as a markdown file
sorting_benchmark_df.to_markdown(benchmark_sorting_results_path, index=False)

# Print sorting benchmark results
print("Sorting Benchmark Results:")
print(sorting_benchmark_df)

# Dictionary to hold searching benchmark results
searching_benchmark_results = {algorithm: [] for algorithm in searching_algorithms}
searching_benchmark_results["Input Size"] = input_sizes

# Benchmark each searching algorithm
for size in input_sizes:
    # Generate a sorted list of the given size for searching
    array = sorted([random.randint(0, 10000) for _ in range(size)])
    target = random.choice(array)  # Choose a random element from the array to search for

    for algorithm in searching_algorithms:
        # Get the searching function by name
        search_function = getattr(SearchAlgorithms, algorithm)

        # Benchmark the searching function
        start_time = time.time()
        
        # Handle special cases where additional arguments are needed
        if algorithm in ["ternary_search", "meta_binary_search"]:
            # These algorithms require start (`l`) and end (`r`) indices
            result = search_function(array, 0, len(array) - 1, target)
        elif algorithm == "fibonacci_search":
            # Fibonacci search typically works on sorted arrays
            result = search_function(array, target)
        else:
            # For all other searches, we use the standard call
            result = search_function(array, target)
        
        end_time = time.time()

        # Record the time taken
        time_taken = end_time - start_time
        searching_benchmark_results[algorithm].append(time_taken)

# Convert the searching results to a DataFrame for easy handling and saving
searching_benchmark_df = pd.DataFrame(searching_benchmark_results)

# Save the searching benchmark results as a markdown file
searching_benchmark_df.to_markdown(benchmark_searching_results_path, index=False)

# Print searching benchmark results
print("\nSearching Benchmark Results:")
print(searching_benchmark_df)

# Define the folder to save the plots
plots_folder = os.path.join(results_folder, "plots")
os.makedirs(plots_folder, exist_ok=True)

# Plot Sorting Benchmark Results
plt.figure(figsize=(12, 8))
for algorithm in sorting_algorithms:
    plt.plot(sorting_benchmark_df["Input Size"], sorting_benchmark_df[algorithm], label=algorithm, marker='o')

plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Benchmark")
plt.yscale("log")  # Use logarithmic scale for better differentiation of time taken
plt.legend()
plt.grid(True)
sorting_plot_path = os.path.join(plots_folder, "sorting_benchmark_plot_unified.png")
plt.savefig(sorting_plot_path)
plt.show()

# Plot Searching Benchmark Results
plt.figure(figsize=(12, 8))
for algorithm in searching_algorithms:
    plt.plot(searching_benchmark_df["Input Size"], searching_benchmark_df[algorithm], label=algorithm, marker='o')

plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Searching Algorithm Benchmark")
plt.yscale("log")  # Use logarithmic scale for better differentiation of time taken
plt.legend()
plt.grid(True)
searching_plot_path = os.path.join(plots_folder, "searching_benchmark_plot_unified.png")
plt.savefig(searching_plot_path)
plt.show()
