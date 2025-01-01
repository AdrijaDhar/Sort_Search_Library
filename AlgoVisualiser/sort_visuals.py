import time

def bubble_sort(canvas, data, delay):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_bars(canvas, data, [j, j + 1])
                time.sleep(delay)

def insertion_sort(canvas, data, delay):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            draw_bars(canvas, data, [j + 1, i])
            time.sleep(delay)
        data[j + 1] = key
        draw_bars(canvas, data, [j + 1, i])

def quick_sort(canvas, data, low, high, delay):
    if low < high:
        pi = partition(canvas, data, low, high, delay)
        quick_sort(canvas, data, low, pi - 1, delay)
        quick_sort(canvas, data, pi + 1, high, delay)

def partition(canvas, data, low, high, delay):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            draw_bars(canvas, data, [i, j])
            time.sleep(delay)
    data[i + 1], data[high] = data[high], data[i + 1]
    draw_bars(canvas, data, [i + 1, high])
    return i + 1

def draw_bars(canvas, data, color_indices):
    canvas.delete("all")
    c_width = 800
    c_height = 400
    bar_width = c_width / len(data)
    max_height = max(data)

    for i, value in enumerate(data):
        x0 = i * bar_width
        y0 = c_height - (value / max_height) * c_height
        x1 = (i + 1) * bar_width
        y1 = c_height
        color = "red" if i in color_indices else "blue"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    canvas.update()
