import matplotlib.pyplot as plt

# Sample data from benchmarks
sizes = [100, 1000, 5000, 10000]
quick_sort_times = [0.000012, 0.000250, 0.001200, 0.010000]
merge_sort_times = [0.000014, 0.000310, 0.001500, 0.012000]
bubble_sort_times = [0.000180, 0.050000, 1.200000, 10.000000]

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
plt.savefig('benchmarks/sorting_performance.png')
plt.show()
