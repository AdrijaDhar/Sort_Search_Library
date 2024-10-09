import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def bubble_sort_visual(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, align="edge", color="skyblue")

    def update_bars(frame):
        for i in range(frame[0]):
            if frame[1] == i or frame[2] == i:
                bars[i].set_color('orange')
            else:
                bars[i].set_color('skyblue')
            bars[i].set_height(arr[i])

    def sort_generator():
        for i in range(n):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                yield j, j+1  # Return current step for visualization

    ani = animation.FuncAnimation(fig, update_bars, frames=sort_generator, repeat=False, blit=False)
    plt.show()

# Example usage:
data = [30, 25, 40, 70, 15, 90, 10, 80]
bubble_sort_visual(data)
