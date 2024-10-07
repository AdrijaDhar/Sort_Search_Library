#include <iostream>
#include "sorting/sorting.h"
#include "searching/search.h"

int main() {
    int arr[] = {34, 7, 23, 32, 5, 62};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Sorting Example
    std::cout << "Original Array: ";
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    quickSort(arr, 0, n - 1);

    std::cout << "Sorted Array using Quick Sort: ";
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    // Searching Example
    int target = 23;
    int index = binarySearch(arr, 0, n - 1, target);
    if (index != -1) {
        std::cout << "Element " << target << " found at index " << index << " using Binary Search" << std::endl;
    } else {
        std::cout << "Element " << target << " not found in the array" << std::endl;
    }

    return 0;
}
