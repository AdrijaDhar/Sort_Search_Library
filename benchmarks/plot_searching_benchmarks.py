import matplotlib.pyplot as plt

# Sample data from benchmarks
sizes = [100, 1000, 5000, 10000]
linear_search_times = [0.000005, 0.000070, 0.000350, 0.000650]
binary_search_times = [0.000001, 0.000003, 0.000004, 0.000005]

plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_search_times, label='Linear Search', marker='o')
plt.plot(sizes, binary_search_times, label='Binary Search', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Searching Algorithm Performance')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.savefig('benchmarks/searching_performance.png')
plt.show()
