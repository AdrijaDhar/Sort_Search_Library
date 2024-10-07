class SortingAlgorithms:
    @staticmethod
    def quick_sort(arr, low=0, high=None):
        if high is None:
            high = len(arr) - 1

        if low < high:
            pi = SortingAlgorithms.partition(arr, low, high)
            SortingAlgorithms.quick_sort(arr, low, pi - 1)
            SortingAlgorithms.quick_sort(arr, pi + 1, high)

    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            SortingAlgorithms.merge_sort(L)
            SortingAlgorithms.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    @staticmethod
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    @staticmethod
    def heap_sort(arr):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[l] > arr[largest]:
                largest = l

            if r < n and arr[r] > arr[largest]:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

    @staticmethod
    def counting_sort(arr):
        max_element = max(arr)
        min_element = min(arr)
        range_of_elements = max_element - min_element + 1

        count = [0] * range_of_elements
        output = [0] * len(arr)

        for i in range(len(arr)):
            count[arr[i] - min_element] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i] - min_element] - 1] = arr[i]
            count[arr[i] - min_element] -= 1

        for i in range(len(arr)):
            arr[i] = output[i]

    @staticmethod
    def radix_sort(arr):
        def counting_sort_exp(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                index = (arr[i] // exp) % 10
                count[index] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            for i in range(n - 1, -1, -1):
                index = (arr[i] // exp) % 10
                output[count[index] - 1] = arr[i]
                count[index] -= 1

            for i in range(n):
                arr[i] = output[i]

        max_num = max(arr)
        exp = 1
        while max_num // exp > 0:
            counting_sort_exp(arr, exp)
            exp *= 10

    @staticmethod
    def shell_sort(arr):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

    

    @staticmethod
    def bucket_sort(arr):
        n = len(arr)
        if n <= 0:
            return

        max_value = max(arr)
        buckets = [[] for _ in range(n)]

        for i in arr:
            index = int(n * i / (max_value + 1))
            buckets[index].append(i)

        for bucket in buckets:
            bucket.sort()

        result_index = 0
        for bucket in buckets:
            for value in bucket:
                arr[result_index] = value
                result_index += 1

    @staticmethod
    def cocktail_shaker_sort(arr):
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            swapped = False
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            start += 1

    @staticmethod
    def comb_sort(arr):
        n = len(arr)
        gap = n
        shrink = 1.3
        sorted_flag = False

        while not sorted_flag:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted_flag = True

            for i in range(n - gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    sorted_flag = False

    @staticmethod
    def gnome_sort(arr):
        index = 0
        n = len(arr)
        while index < n:
            if index == 0 or arr[index] >= arr[index - 1]:
                index += 1
            else:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
                index -= 1

    @staticmethod
    def tim_sort(arr):
        RUN = 32

        def insertion_sort(arr, left, right):
            for i in range(left + 1, right + 1):
                key = arr[i]
                j = i - 1
                while j >= left and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

        def merge(arr, l, m, r):
            len1, len2 = m - l + 1, r - m
            left, right = [], []

            for i in range(0, len1):
                left.append(arr[l + i])
            for i in range(0, len2):
                right.append(arr[m + 1 + i])

            i, j, k = 0, 0, l

            while i < len1 and j < len2:
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len1:
                arr[k] = left[i]
                k += 1
                i += 1

            while j < len2:
                arr[k] = right[j]
                k += 1
                j += 1

        n = len(arr)
        for i in range(0, n, RUN):
            insertion_sort(arr, i, min((i + 31), (n - 1)))

        size = RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min((n - 1), (left + size - 1))
                right = min((left + 2 * size - 1), (n - 1))

                if mid < right:
                    merge(arr, left, mid, right)

            size = 2 * size

    @staticmethod
    def pancake_sort(arr):
        def flip(arr, i):
            start = 0
            while start < i:
                arr[start], arr[i] = arr[i], arr[start]
                start += 1
                i -= 1

        n = len(arr)
        for curr_size in range(n, 1, -1):
            max_idx = arr.index(max(arr[:curr_size]))
            if max_idx != curr_size - 1:
                flip(arr, max_idx)
                flip(arr, curr_size - 1)

    @staticmethod
    def tree_sort(arr):
        class TreeNode:
            def __init__(self, key):
                self.left = None
                self.right = None
                self.val = key

        def insert(root, key):
            if root is None:
                return TreeNode(key)
            else:
                if root.val < key:
                    root.right = insert(root.right, key)
                else:
                    root.left = insert(root.left, key)
            return root

        def store_sorted(root, arr, i):
            if root is not None:
                i = store_sorted(root.left, arr, i)
                arr[i] = root.val
                i += 1
                i = store_sorted(root.right, arr, i)
            return i

        if not arr:
            return

        root = TreeNode(arr[0])
        for i in range(1, len(arr)):
            insert(root, arr[i])

        store_sorted(root, arr, 0)
