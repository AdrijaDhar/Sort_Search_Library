# Sort Search Library

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Overview
**Sort Search Library** is a collection of custom sorting and searching algorithms implemented in Python and C++. It includes efficient algorithms for sorting lists and searching through them, aimed at providing an easy-to-use toolkit for both educational and practical applications.

This library also comes with performance benchmarks, showcasing how different algorithms scale with increasing data sizes. The project serves as a resource for learning, research, and practical implementation of fundamental algorithms in computer science.

## Features
- **Sorting Algorithms**:
  - Quick Sort
  - Merge Sort
  - Bubble Sort
- **Searching Algorithms**:
  - Linear Search
  - Binary Search
- **Multi-Language Support**: Implemented in Python and C++
- **Benchmarking and Visual Analysis**: Includes performance benchmarks with visualizations

## Installation

### Python Installation
To install the Python version of the library, you can clone the repository and install it locally:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/AdrijaDhar/Sort_Search_Library.git
   cd Sort_Search_Library
   
2. **Install the Library**:
    ```sh
    Copy code
    pip install .
### C++ Usage
To use the C++ version of the library, clone the repository and build it using CMake:

1. **Clone the Repository**:
    ```sh
    Copy code
    git clone https://github.com/AdrijaDhar/Sort_Search_Library.git
    cd Sort_Search_Library

2. **Build with CMake**:
    ```sh
    Copy code
    mkdir build
    cd build
    cmake ..
    make

This will generate the necessary executable files for usage examples and benchmarks.

### Running Benchmarks

To run the benchmarks for sorting and searching:

### Python
Run the following scripts from the root directory:

1. *** Sorting Benchmark ***:
    ```sh
    Copy code
    python3 benchmarks/benchmark_sorting.py

2. ***Searching Benchmark*** :
    ```sh
    Copy code
    python3 benchmarks/benchmark_searching.py
### C++
Make sure you have compiled the C++ programs as mentioned in the C++ Installation Section:

1. ***Sorting Benchmark***:
    ```sh
    Copy code
    ./benchmark_sorting
2. ***Searching Benchmark***:
    ```sh
    Copy code
    ./benchmark_search

Benchmark Results

## For detailed benchmark results, including tables and performance graphs, please refer to the following files:

1. **Benchmark Results Links**:
   - **[Sorting Benchmark Results](results/sorting_results.md)**: This is a link to the generated results markdown file for sorting benchmarks.
   - **[Searching Benchmark Results](results/searching_results.md)**: This is a link to the generated results markdown file for searching benchmarks.
