#include "algorithms.h"
#include <iostream>

int main() {
    int arr[] = {34, 7, 23, 32, 5, 62};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Sorting Example with Quick Sort
    int arr1[] = {34, 7, 23, 32, 5, 62};
    quickSort(arr1, 0, n - 1);
    std::cout << "Sorted Array using Quick Sort: ";
    for (int i = 0; i < n; i++) {
        std::cout << arr1[i] << " ";
    }
    std::cout << std::endl;

    // Sorting Example with Merge Sort
    int arr2[] = {34, 7, 23, 32, 5, 62};
    mergeSort(arr2, 0, n - 1);
    std::cout << "Sorted Array using Merge Sort: ";
    for (int i = 0; i < n; i++) {
        std::cout << arr2[i] << " ";
    }
    std::cout << std::endl;

    // Sorting Example with Bubble Sort
    int arr3[] = {34, 7, 23, 32, 5, 62};
    bubbleSort(arr3, n);
    std::cout << "Sorted Array using Bubble Sort: ";
    for (int i = 0; i < n; i++) {
        std::cout << arr3[i] << " ";
    }
    std::cout << std::endl;

    // Searching Example with Binary Search
    int target = 23;
    int index = binarySearch(arr2, 0, n - 1, target);
    if (index != -1) {
        std::cout << "Element " << target << " found at index " << index << " using Binary Search" << std::endl;
    } else {
        std::cout << "Element " << target << " not found in the array" << std::endl;
    }

    // Searching Example with Linear Search
    int indexLinear = linearSearch(arr, n, target);
    if (indexLinear != -1) {
        std::cout << "Element " << target << " found at index " << indexLinear << " using Linear Search" << std::endl;
    } else {
        std::cout << "Element " << target << " not found in the array" << std::endl;
    }

    // Additional Sorting Examples
    int arr4[] = {34, 7, 23, 32, 5, 62};
    selectionSort(arr4, n);
    std::cout << "Sorted Array using Selection Sort: ";
    for (int i = 0; i < n; i++) {
        std::cout << arr4[i] << " ";
    }
    std::cout << std::endl;

    int arr5[] = {34, 7, 23, 32, 5, 62};
    heapSort(arr5, n);
    std::cout << "Sorted Array using Heap Sort: ";
    for (int i = 0; i < n; i++) {
        std::cout << arr5[i] << " ";
    }
    std::cout << std::endl;

    // Additional Searching Examples
    int indexJump = jumpSearch(arr2, n, target);
    if (indexJump != -1) {
        std::cout << "Element " << target << " found at index " << indexJump << " using Jump Search" << std::endl;
    } else {
        std::cout << "Element " << target << " not found in the array using Jump Search" << std::endl;
    }

    int indexInterpolation = interpolationSearch(arr2, n, target);
    if (indexInterpolation != -1) {
        std::cout << "Element " << target << " found at index " << indexInterpolation << " using Interpolation Search" << std::endl;
    } else {
        std::cout << "Element " << target << " not found in the array using Interpolation Search" << std::endl;
    }

    return 0;
}
