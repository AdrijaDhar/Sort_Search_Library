#ifndef SEARCH_H
#define SEARCH_H

// Function prototypes for various search algorithms

int linearSearch(int arr[], int n, int x);
int binarySearch(int arr[], int l, int r, int x);
int jumpSearch(int arr[], int n, int x);
int interpolationSearch(int arr[], int n, int x);
int exponentialSearch(int arr[], int n, int x);
int fibonacciSearch(int arr[], int n, int x);
int ternarySearch(int arr[], int l, int r, int x);
int sentinelLinearSearch(int arr[], int n, int x);
int metaBinarySearch(int arr[], int l, int r, int x);

#endif // SEARCH_H
