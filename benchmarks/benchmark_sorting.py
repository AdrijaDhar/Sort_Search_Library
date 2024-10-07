import timeit
import random
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sorting.sorting import SortingAlgorithms
import matplotlib.pyplot as plt

# Define the output path
output_folder = "results"
os.makedirs(output_folder, exist_ok=True)
output_file_path = os.path.join(output_folder, "sorting_results.md")

# Benchmark Sorting Algorithms and Save Results
sizes = [100, 1000, 5000, 10000]
quick_sort_times = []
merge_sort_times = []
bubble_sort_times = []

# Open the output file for writing
with open(output_file_path, "w") as f:
    f.write("# Sorting Benchmark Results\n\n")
    f.write("| Input Size | Quick Sort (sec) | Merge Sort (sec) | Bubble Sort (sec) |\n")
    f.write("|------------|------------------|------------------|-------------------|\n")

    for size in sizes:
        # Generate random array
        arr = [random.randint(0, 10000) for _ in range(size)]

        # Quick Sort
        quick_sort_time = timeit.timeit(lambda: SortingAlgorithms.quick_sort(arr.copy(), 0, len(arr) - 1), number=1)
        quick_sort_times.append(quick_sort_time)

        # Merge Sort
        merge_sort_time = timeit.timeit(lambda: SortingAlgorithms.merge_sort(arr.copy()), number=1)
        merge_sort_times.append(merge_sort_time)

        # Bubble Sort
        bubble_sort_time = timeit.timeit(lambda: SortingAlgorithms.bubble_sort(arr.copy()), number=1)
        bubble_sort_times.append(bubble_sort_time)

        # Write results to file
        f.write(f"| {size} | {quick_sort_time:.6f} | {merge_sort_time:.6f} | {bubble_sort_time:.6f} |\n")

# Plot and Save Graph
plt.figure(figsize=(10, 6))
plt.plot(sizes, quick_sort_times, label='Quick Sort', marker='o')
plt.plot(sizes, merge_sort_times, label='Merge Sort', marker='o')
plt.plot(sizes, bubble_sort_times, label='Bubble Sort', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance')
plt.yscale('log')  # Log scale to better visualize differences
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(output_folder, "sorting_performance.png"))
plt.close()
