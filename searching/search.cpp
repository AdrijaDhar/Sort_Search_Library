#include "search.h"
#include <cmath>
#include <algorithm>

// Linear Search
int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x)
            return i;
    }
    return -1;
}

// Binary Search
int binarySearch(int arr[], int l, int r, int x) {
    while (l <= r) {
        int mid = l + (r - l) / 2;

        if (arr[mid] == x)
            return mid;

        if (arr[mid] < x)
            l = mid + 1;
        else
            r = mid - 1;
    }
    return -1;
}

// Jump Search
int jumpSearch(int arr[], int n, int x) {
    int step = std::sqrt(n);
    int prev = 0;

    while (arr[std::min(step, n) - 1] < x) {
        prev = step;
        step += std::sqrt(n);
        if (prev >= n) {
            return -1;
        }
    }

    for (int i = prev; i < std::min(step, n); i++) {
        if (arr[i] == x) {
            return i;
        }
    }
    return -1;
}

// Interpolation Search
int interpolationSearch(int arr[], int n, int x) {
    int low = 0, high = n - 1;

    while (low <= high && x >= arr[low] && x <= arr[high]) {
        if (low == high) {
            if (arr[low] == x) return low;
            return -1;
        }

        int pos = low + ((high - low) * (x - arr[low])) / (arr[high] - arr[low]);

        if (arr[pos] == x)
            return pos;
        if (arr[pos] < x)
            low = pos + 1;
        else
            high = pos - 1;
    }
    return -1;
}

// Exponential Search
int exponentialSearch(int arr[], int n, int x) {
    if (arr[0] == x) {
        return 0;
    }

    int i = 1;
    while (i < n && arr[i] <= x) {
        i *= 2;
    }

    return binarySearch(arr, i / 2, std::min(i, n) - 1, x);
}

// Fibonacci Search
int fibonacciSearch(int arr[], int n, int x) {
    int fibM2 = 0;   // (m-2)'th Fibonacci number
    int fibM1 = 1;   // (m-1)'th Fibonacci number
    int fibM = fibM2 + fibM1; // m'th Fibonacci number

    while (fibM < n) {
        fibM2 = fibM1;
        fibM1 = fibM;
        fibM = fibM2 + fibM1;
    }

    int offset = -1;

    while (fibM > 1) {
        int i = std::min(offset + fibM2, n - 1);

        if (arr[i] < x) {
            fibM = fibM1;
            fibM1 = fibM2;
            fibM2 = fibM - fibM1;
            offset = i;
        }
        else if (arr[i] > x) {
            fibM = fibM2;
            fibM1 = fibM1 - fibM2;
            fibM2 = fibM - fibM1;
        }
        else {
            return i;
        }
    }

    if (fibM1 && arr[offset + 1] == x) {
        return offset + 1;
    }

    return -1;
}

// Ternary Search (Recursive Version)
int ternarySearch(int arr[], int l, int r, int x) {
    if (r >= l) {
        int mid1 = l + (r - l) / 3;
        int mid2 = r - (r - l) / 3;

        if (arr[mid1] == x) {
            return mid1;
        }
        if (arr[mid2] == x) {
            return mid2;
        }

        if (x < arr[mid1]) {
            return ternarySearch(arr, l, mid1 - 1, x);
        } else if (x > arr[mid2]) {
            return ternarySearch(arr, mid2 + 1, r, x);
        } else {
            return ternarySearch(arr, mid1 + 1, mid2 - 1, x);
        }
    }
    return -1;
}

// Sentinel Linear Search
int sentinelLinearSearch(int arr[], int n, int x) {
    int last = arr[n - 1];
    arr[n - 1] = x;

    int i = 0;
    while (arr[i] != x) {
        i++;
    }

    arr[n - 1] = last;

    if (i < n - 1 || arr[n - 1] == x) {
        return i;
    }
    return -1;
}

// Meta Binary Search (One-sided Binary Search)
int metaBinarySearch(int arr[], int l, int r, int x) {
    while (l <= r) {
        int mid = l + ((r - l) >> 1);

        if (arr[mid] == x) {
            return mid;
        } else if (arr[mid] < x) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return -1;
}
