#include <iostream>
#include <chrono>
#include <algorithm>  // For std::sort
#include "../searching/search.h"
#include "../sorting/sorting.h"

void benchmark_searching() {
    int sizes[] = {100, 1000, 5000, 10000};
    for (int size : sizes) {
        int* arr = new int[size];

        // Fill the array with random values
        for (int i = 0; i < size; ++i) {
            arr[i] = rand() % 10000;
        }

        // Random target value for searching
        int target = rand() % 10000;

        std::cout << "\nBenchmarking with input size: " << size << std::endl;

        // Linear Search Benchmark
        auto start = std::chrono::high_resolution_clock::now();
        int index_linear = linearSearch(arr, size, target);
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed = end - start;
        std::cout << "Linear Search Time: " << elapsed.count() << " seconds (index: " << index_linear << ")" << std::endl;

        // Sorting the array for Binary Search
        quickSort(arr, 0, size - 1);

        // Binary Search Benchmark
        start = std::chrono::high_resolution_clock::now();
        int index_binary = binarySearch(arr, 0, size - 1, target);
        end = std::chrono::high_resolution_clock::now();
        elapsed = end - start;
        std::cout << "Binary Search Time: " << elapsed.count() << " seconds (index: " << index_binary << ")" << std::endl;

        delete[] arr; // Delete the original array
    }
}

int main() {
    benchmark_searching();
    return 0;
}
