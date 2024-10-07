class SearchAlgorithms:
    @staticmethod
    def linear_search(arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1

    @staticmethod
    def binary_search(arr, x):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return -1
