#include <iostream>
#include <chrono>
#include "../sorting/sorting.h"

void benchmark_sorting() {
    int sizes[] = {100, 1000, 5000, 10000};
    for (int size : sizes) {
        int* arr = new int[size];
        
        // Fill the array with random values
        for (int i = 0; i < size; ++i) {
            arr[i] = rand() % 10000;
        }

        std::cout << "\nBenchmarking with input size: " << size << std::endl;

        // Quick Sort Benchmark
        int* arr_quick = new int[size];
        std::copy(arr, arr + size, arr_quick);
        auto start = std::chrono::high_resolution_clock::now();
        quickSort(arr_quick, 0, size - 1);
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed = end - start;
        std::cout << "Quick Sort Time: " << elapsed.count() << " seconds" << std::endl;
        delete[] arr_quick;

        // Merge Sort Benchmark
        int* arr_merge = new int[size];
        std::copy(arr, arr + size, arr_merge);
        start = std::chrono::high_resolution_clock::now();
        mergeSort(arr_merge, 0, size - 1);
        end = std::chrono::high_resolution_clock::now();
        elapsed = end - start;
        std::cout << "Merge Sort Time: " << elapsed.count() << " seconds" << std::endl;
        delete[] arr_merge;

        // Bubble Sort Benchmark
        int* arr_bubble = new int[size];
        std::copy(arr, arr + size, arr_bubble);
        start = std::chrono::high_resolution_clock::now();
        bubbleSort(arr_bubble, size);
        end = std::chrono::high_resolution_clock::now();
        elapsed = end - start;
        std::cout << "Bubble Sort Time: " << elapsed.count() << " seconds" << std::endl;
        delete[] arr_bubble;

        delete[] arr; // Delete the original array
    }
}

int main() {
    benchmark_sorting();
    return 0;
}
