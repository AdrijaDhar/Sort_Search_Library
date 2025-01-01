from tkinter import *
from sort_visuals import bubble_sort, insertion_sort, quick_sort
from search_visuals import linear_search, binary_search

def main():
    window = Tk()
    window.title("Algorithm Visualizer")
    canvas = Canvas(window, width=800, height=400, bg="white")
    canvas.pack()

    data = [10, 30, 20, 50, 40, 60, 5, 25]
    delay = 0.5  # Animation speed

    # Sorting Buttons
    Button(window, text="Bubble Sort", command=lambda: bubble_sort(canvas, data, delay)).pack()
    Button(window, text="Insertion Sort", command=lambda: insertion_sort(canvas, data, delay)).pack()
    Button(window, text="Quick Sort", command=lambda: quick_sort(canvas, data, 0, len(data) - 1, delay)).pack()

    # Searching Buttons
    Button(window, text="Linear Search", command=lambda: linear_search(canvas, data, 20, delay)).pack()
    Button(window, text="Binary Search", command=lambda: binary_search(canvas, sorted(data), 20, delay)).pack()

    window.mainloop()

if __name__ == "__main__":
    main()
