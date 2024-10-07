import logging

logging.basicConfig(level=logging.INFO)
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

    @staticmethod
    def jump_search(arr, x):
        import math
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0

        while arr[min(step, n) - 1] < x:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1

        for i in range(prev, min(step, n)):
            if arr[i] == x:
                return i
        return -1

    @staticmethod
    def interpolation_search(arr, x):
        low, high = 0, len(arr) - 1

        while low <= high and arr[low] <= x <= arr[high]:
            pos = low + ((high - low) // (arr[high] - arr[low]) * (x - arr[low]))

            if arr[pos] == x:
                return pos
            elif arr[pos] < x:
                low = pos + 1
            else:
                high = pos - 1

        return -1

    @staticmethod
    def exponential_search(arr, x):
        if arr[0] == x:
            return 0

        n = len(arr)
        i = 1

        while i < n and arr[i] <= x:
            i *= 2

        return SearchAlgorithms.binary_search(arr[min(i, n):], x)

    @staticmethod
    def fibonacci_search(arr, x):
        n = len(arr)
        fib_m_2, fib_m_1 = 0, 1
        fib_m = fib_m_2 + fib_m_1

        while fib_m < n:
            fib_m_2 = fib_m_1
            fib_m_1 = fib_m
            fib_m = fib_m_2 + fib_m_1

        offset = -1

        while fib_m > 1:
            i = min(offset + fib_m_2, n - 1)

            if arr[i] < x:
                fib_m = fib_m_1
                fib_m_1 = fib_m_2
                fib_m_2 = fib_m - fib_m_1
                offset = i
            elif arr[i] > x:
                fib_m = fib_m_2
                fib_m_1 -= fib_m_2
                fib_m_2 = fib_m - fib_m_1
            else:
                return i

        if fib_m_1 and offset + 1 < n and arr[offset + 1] == x:
            return offset + 1

        return -1

    @staticmethod
    def ternary_search(arr, l, r, x):
        if r >= l:
            mid1 = l + (r - l) // 3
            mid2 = r - (r - l) // 3

            if arr[mid1] == x:
                return mid1
            if arr[mid2] == x:
                return mid2

            if x < arr[mid1]:
                return SearchAlgorithms.ternary_search(arr, l, mid1 - 1, x)
            elif x > arr[mid2]:
                return SearchAlgorithms.ternary_search(arr, mid2 + 1, r, x)
            else:
                return SearchAlgorithms.ternary_search(arr, mid1 + 1, mid2 - 1, x)

        return -1

    @staticmethod
    def sentinel_linear_search(arr, x):
        n = len(arr)
        last = arr[-1]
        arr[-1] = x
        i = 0

        while arr[i] != x:
            i += 1

        arr[-1] = last

        if i < n - 1 or arr[-1] == x:
            return i
        return -1

    @staticmethod
    def meta_binary_search(arr, l, r, x):
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = l + ((r - l) >> 1)

            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1

        return -1

    # Depth First Search (DFS) and Breadth First Search (BFS) will be added for graph representation

    @staticmethod
    def dfs(graph, node, visited=None):
        if visited is None:
            visited = set()
        logging.info(f"Visiting node: {node}")
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                SearchAlgorithms.dfs(graph, neighbor, visited)


    @staticmethod
    def bfs(graph, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
