import time
from sort_visuals import draw_bars
def linear_search(canvas, data, target, delay):
    for i in range(len(data)):
        draw_bars(canvas, data, [i])
        time.sleep(delay)
        if data[i] == target:
            draw_bars(canvas, data, [i])  # Highlight the found element
            return i
    return -1

def binary_search(canvas, data, target, delay):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        draw_bars(canvas, data, [mid])
        time.sleep(delay)
        if data[mid] == target:
            draw_bars(canvas, data, [mid])  # Highlight the found element
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def jump_search(canvas, data, target, delay):
    import math
    n = len(data)
    step = int(math.sqrt(n))
    prev = 0
    while data[min(step, n) - 1] < target:
        draw_bars(canvas, data, [prev, min(step, n) - 1])
        time.sleep(delay)
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        draw_bars(canvas, data, [i])
        time.sleep(delay)
        if data[i] == target:
            draw_bars(canvas, data, [i])  # Highlight the found element
            return i
    return -1
