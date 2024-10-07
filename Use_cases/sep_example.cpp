#include "sorting.h"
#include "search.h"
#include <iostream>

int main() {
    int arr[] = {34, 7, 23, 32, 5, 62};
    int n = sizeof(arr) / sizeof(arr[0]);

    std::cout << "Using Separate Headers (sorting.h and search.h):\n";

    // Sorting Example
    // Merge Sort Example
    int arr2[] = {34, 7, 23, 32, 5, 62};
    mergeSort(arr2, 0, n - 1);
    std::cout << "Sorted Array using Merge Sort: ";
    for (int i = 0; i < n; i++) {
        std::cout << arr2[i] << " ";
    }
    std::cout << std::endl;

    // Bubble Sort Example
    int arr3[] = {34, 7, 23, 32, 5, 62};
    bubbleSort(arr3, n);
    std::cout << "Sorted Array using Bubble Sort: ";
    for (int i = 0; i < n; i++) {
        std::cout << arr3[i] << " ";
    }
    std::cout << std::endl;

    // Searching Example
    // Binary Search Example
    int target = 32;
    int index = binarySearch(arr2, 0, n - 1, target);
    if (index != -1) {
        std::cout << "Element " << target << " found at index " << index << " using Binary Search\n";
    } else {
        std::cout << "Element " << target << " not found in the array using Binary Search\n";
    }

    // Jump Search Example
    int indexJump = jumpSearch(arr3, n, target);
    if (indexJump != -1) {
        std::cout << "Element " << target << " found at index " << indexJump << " using Jump Search\n";
    } else {
        std::cout << "Element " << target << " not found in the array using Jump Search\n";
    }

    return 0;
}
