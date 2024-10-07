# Sort Search Library

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Welcome to the **Custom Sorting and Search Algorithms Library**! This project aims to implement a comprehensive library of custom sorting and search algorithms optimized for different use cases, such as external sorting and in-memory sorting. It also includes performance benchmarks and comparisons with standard algorithms.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Benchmarking](#benchmarking)
6. [Results](#results)
7. [Contributing](#contributing)
8. [License](#license)

## Overview

This library includes a wide variety of sorting and searching algorithms implemented in Python and C++. The project also provides performance benchmarks to help understand the time complexity of different algorithms for varying input sizes. The goal is to highlight skills in algorithm design, complexity analysis, and optimization techniques.

## Features

- Sorting Algorithms:
  - Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort
  - Heap Sort, Counting Sort, Radix Sort, Shell Sort, Bingo Sort, Bucket Sort
  - Cocktail Shaker Sort, Comb Sort, Gnome Sort, Tim Sort, Pancake Sort
  - Tree Sort, Cycle Sort, Strand Sort, Bogo Sort, Pigeonhole Sort, Bitonic Sort

- Searching Algorithms:
  - Linear Search, Binary Search, Jump Search, Interpolation Search, Exponential Search
  - Fibonacci Search, Depth First Search (DFS), Breadth First Search (BFS)
  - Ternary Search, Sentinel Linear Search, Meta Binary Search

- **Benchmarking**: Measure the performance of sorting and searching algorithms for varying input sizes and visualize the results.

## Installation

To set up the library and run the benchmarks:


### Python Installation
To install the Python version of the library, you can clone the repository and install it locally:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/AdrijaDhar/Sort_Search_Library.git
   cd Sort_Search_Library
   
2. **Install the Library**:
    ```sh
    
    pip install .
### C++ Usage
To use the C++ version of the library, clone the repository and build it using CMake:

1. **Clone the Repository**:
    ```sh
    
    git clone https://github.com/AdrijaDhar/Sort_Search_Library.git
    cd Sort_Search_Library

2. **Build with CMake**:
    ```sh
    
    mkdir build
    cd build
    cmake ..
    make

This will generate the necessary executable files for usage examples and benchmarks.

### Running Benchmarks

To run the benchmarks for sorting and searching:

### Python
Run the following scripts from the root directory:

1. ***Sorting Benchmark***:
    ```sh
    
    python3 benchmarks/benchmark_sorting.py

2. ***Searching Benchmark*** :
    ```sh
    
    python3 benchmarks/benchmark_searching.py
### C++
Make sure you have compiled the C++ programs as mentioned in the C++ Installation Section:

1. ***Sorting Benchmark***:
    ```sh
    
    ./benchmark_sorting
2. ***Searching Benchmark***:
    ```sh
    
    ./benchmark_search
3. ***Benchmar all***:
    ```sh
    ./benchmark_all
Benchmark Results

## For detailed benchmark results, including tables and performance graphs, please refer to the following files:

1. **Benchmark Results Links**:
   - **[Sorting Benchmark Results](results/sorting_benchmark_results.md)**: This is a link to the generated results markdown file for sorting benchmarks.
   - **[Sorting Benchmark Plots](results/plots/sorting_benchmark_plot.png)**: This is link to the generated results markdown file for sorting benchmarks.
   - **[Searching Benchmark Results](results/searching_benchmark_results.md)**: This is a link to the generated results markdown file for searching benchmarks.
   - **[Searching Benchmark Plots](results/plots/searching_benchmark_plot.png)**: This is link to the generated results markdown file for searching benchmarks.
