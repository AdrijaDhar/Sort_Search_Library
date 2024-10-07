from sorting.sorting import SortingAlgorithms
from searching.search import SearchAlgorithms

def main():
    # Sample data for demonstration
    arr = [34, 7, 23, 32, 5, 62]
    
    # Sorting Example
    print("Original Array:", arr)
    SortingAlgorithms.quick_sort(arr, 0, len(arr) - 1)
    print("Sorted Array using Quick Sort:", arr)

    # Searching Example
    target = 23
    index = SearchAlgorithms.binary_search(arr, target)
    if index != -1:
        print(f"Element {target} found at index {index} using Binary Search")
    else:
        print(f"Element {target} not found in the array")

if __name__ == "__main__":
    main()
