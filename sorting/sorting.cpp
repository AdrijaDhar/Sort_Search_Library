#include "sorting.h"
#include <algorithm>
#include <vector>
#include <cmath>

// Quick Sort
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j <= high - 1; j++) {
            if (arr[j] <= pivot) {
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[high]);
        int pi = i + 1;

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Merge Sort
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        int n1 = m - l + 1, n2 = r - m;
        int L[n1], R[n2];

        for (int i = 0; i < n1; i++) L[i] = arr[l + i];
        for (int i = 0; i < n2; i++) R[i] = arr[m + 1 + i];

        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) arr[k++] = L[i++];
            else arr[k++] = R[j++];
        }
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }
}

// Bubble Sort
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Selection Sort
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        std::swap(arr[min_idx], arr[i]);
    }
}

// Insertion Sort
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// Heap Sort
void heapify(int arr[], int n, int i) {
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < n && arr[l] > arr[largest])
        largest = l;

    if (r < n && arr[r] > arr[largest])
        largest = r;

    if (largest != i) {
        std::swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i > 0; i--) {
        std::swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

// Counting Sort
void countingSort(int arr[], int n) {
    int max = *std::max_element(arr, arr + n);
    int min = *std::min_element(arr, arr + n);
    int range = max - min + 1;

    std::vector<int> count(range), output(n);
    for (int i = 0; i < n; i++)
        count[arr[i] - min]++;

    for (int i = 1; i < count.size(); i++)
        count[i] += count[i - 1];

    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i] - min] - 1] = arr[i];
        count[arr[i] - min]--;
    }

    for (int i = 0; i < n; i++)
        arr[i] = output[i];
}

// Radix Sort
int getMax(int arr[], int n) {
    return *std::max_element(arr, arr + n);
}

void countSortRadix(int arr[], int n, int exp) {
    int output[n];
    int count[10] = {0};

    for (int i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;

    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];

    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }

    for (int i = 0; i < n; i++)
        arr[i] = output[i];
}

void radixSort(int arr[], int n) {
    int m = getMax(arr, n);
    for (int exp = 1; m / exp > 0; exp *= 10)
        countSortRadix(arr, n, exp);
}

// Shell Sort
void shellSort(int arr[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            arr[j] = temp;
        }
    }
}
// Bingo Sort
void bingoSort(int arr[], int n) {
    int max = *std::max_element(arr, arr + n);
    int currentValue = *std::min_element(arr, arr + n);
    int nextValue;

    int index = 0;
    while (currentValue < max) {
        nextValue = max;
        for (int i = index; i < n; i++) {
            if (arr[i] == currentValue) {
                std::swap(arr[i], arr[index]);
                index++;
            } else if (arr[i] > currentValue) {
                nextValue = std::min(nextValue, arr[i]);
            }
        }
        currentValue = nextValue;
    }
}

// Bucket Sort
void bucketSort(float arr[], int n) {
    std::vector<float> buckets[n];

    for (int i = 0; i < n; i++) {
        int bucketIndex = n * arr[i];
        buckets[bucketIndex].push_back(arr[i]);
    }

    for (int i = 0; i < n; i++) {
        std::sort(buckets[i].begin(), buckets[i].end());
    }

    int index = 0;
    for (int i = 0; i < n; i++) {
        for (float value : buckets[i]) {
            arr[index++] = value;
        }
    }
}

// Cocktail Shaker Sort
void cocktailShakerSort(int arr[], int n) {
    bool swapped = true;
    int start = 0;
    int end = n - 1;

    while (swapped) {
        swapped = false;

        for (int i = start; i < end; ++i) {
            if (arr[i] > arr[i + 1]) {
                std::swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }

        if (!swapped)
            break;

        swapped = false;
        --end;

        for (int i = end - 1; i >= start; --i) {
            if (arr[i] > arr[i + 1]) {
                std::swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }
        ++start;
    }
}

// Comb Sort
void combSort(int arr[], int n) {
    int gap = n;
    bool swapped = true;

    while (gap != 1 || swapped) {
        gap = (gap * 10) / 13;
        if (gap < 1) gap = 1;

        swapped = false;
        for (int i = 0; i < n - gap; i++) {
            if (arr[i] > arr[i + gap]) {
                std::swap(arr[i], arr[i + gap]);
                swapped = true;
            }
        }
    }
}

// Gnome Sort
void gnomeSort(int arr[], int n) {
    int index = 0;

    while (index < n) {
        if (index == 0 || arr[index] >= arr[index - 1]) {
            index++;
        } else {
            std::swap(arr[index], arr[index - 1]);
            index--;
        }
    }
}

// Tim Sort (Using Insertion Sort and Merge)
const int RUN = 32;

void insertionSortTim(int arr[], int left, int right) {
    for (int i = left + 1; i <= right; i++) {
        int temp = arr[i];
        int j = i - 1;
        while (j >= left && arr[j] > temp) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = temp;
    }
}

void mergeTim(int arr[], int l, int m, int r) {
    int len1 = m - l + 1, len2 = r - m;
    int left[len1], right[len2];

    for (int x = 0; x < len1; x++)
        left[x] = arr[l + x];
    for (int x = 0; x < len2; x++)
        right[x] = arr[m + 1 + x];

    int i = 0;
    int j = 0;
    int k = l;

    while (i < len1 && j < len2) {
        if (left[i] <= right[j]) {
            arr[k] = left[i];
            i++;
        } else {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    while (i < len1) {
        arr[k] = left[i];
        k++;
        i++;
    }

    while (j < len2) {
        arr[k] = right[j];
        k++;
        j++;
    }
}

void timSort(int arr[], int n) {
    for (int i = 0; i < n; i += RUN)
        insertionSortTim(arr, i, std::min((i + RUN - 1), (n - 1)));

    for (int size = RUN; size < n; size = 2 * size) {
        for (int left = 0; left < n; left += 2 * size) {
            int mid = left + size - 1;
            int right = std::min((left + 2 * size - 1), (n - 1));
            if (mid < right)
                mergeTim(arr, left, mid, right);
        }
    }
}

// Pancake Sort
void flip(int arr[], int i) {
    int start = 0;
    while (start < i) {
        std::swap(arr[start], arr[i]);
        start++;
        i--;
    }
}

void pancakeSort(int arr[], int n) {
    for (int curr_size = n; curr_size > 1; --curr_size) {
        int mi = std::max_element(arr, arr + curr_size) - arr;

        if (mi != curr_size - 1) {
            flip(arr, mi);
            flip(arr, curr_size - 1);
        }
    }
}

// Tree Sort (using Binary Search Tree)
struct TreeNode {
    int key;
    TreeNode* left, * right;
    TreeNode(int item) {
        key = item;
        left = right = nullptr;
    }
};

TreeNode* insert(TreeNode* node, int key) {
    if (node == nullptr) return new TreeNode(key);

    if (key < node->key) node->left = insert(node->left, key);
    else node->right = insert(node->right, key);

    return node;
}

void storeSorted(TreeNode* root, int arr[], int& i) {
    if (root != nullptr) {
        storeSorted(root->left, arr, i);
        arr[i++] = root->key;
        storeSorted(root->right, arr, i);
    }
}

void treeSort(int arr[], int n) {
    TreeNode* root = nullptr;
    root = insert(root, arr[0]);

    for (int i = 1; i < n; i++) {
        insert(root, arr[i]);
    }

    int i = 0;
    storeSorted(root, arr, i);
}

