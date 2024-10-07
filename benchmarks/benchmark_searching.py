import timeit
import random
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from searching.search import SearchAlgorithms
import matplotlib.pyplot as plt

# Define the output path
output_folder = "results"
os.makedirs(output_folder, exist_ok=True)
output_file_path = os.path.join(output_folder, "searching_results.md")

# Benchmark Searching Algorithms and Save Results
sizes = [100, 1000, 5000, 10000]
linear_search_times = []
binary_search_times = []

# Open the output file for writing
with open(output_file_path, "w") as f:
    f.write("# Searching Benchmark Results\n\n")
    f.write("| Input Size | Linear Search (sec) | Binary Search (sec) |\n")
    f.write("|------------|---------------------|---------------------|\n")

    for size in sizes:
        # Generate sorted array for binary search
        arr = sorted([random.randint(0, 10000) for _ in range(size)])
        target = random.randint(0, 10000)

        # Linear Search
        linear_search_time = timeit.timeit(lambda: SearchAlgorithms.linear_search(arr, target), number=1)
        linear_search_times.append(linear_search_time)

        # Binary Search
        binary_search_time = timeit.timeit(lambda: SearchAlgorithms.binary_search(arr, target), number=1)
        binary_search_times.append(binary_search_time)

        # Write results to file
        f.write(f"| {size} | {linear_search_time:.6f} | {binary_search_time:.6f} |\n")

# Plot and Save Graph
plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_search_times, label='Linear Search', marker='o')
plt.plot(sizes, binary_search_times, label='Binary Search', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Searching Algorithm Performance')
plt.yscale('log')  # Log scale for better comparison
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(output_folder, "searching_performance.png"))
plt.close()
