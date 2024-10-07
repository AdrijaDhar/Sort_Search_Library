def test_all_searches(self):
    test_cases = [
        ("linear_search", [2, 3, 4, 10, 40], 10, 3),
        ("linear_search", [2, 3, 4, 10, 40], 5, -1),
        ("binary_search", [2, 3, 4, 10, 40], 10, 3),
        ("binary_search", [2, 3, 4, 10, 40], 5, -1),
        ("jump_search", [1, 3, 5, 7, 9, 11, 13, 15], 7, 3),
        ("jump_search", [1, 3, 5, 7, 9, 11, 13, 15], 8, -1),
        ("interpolation_search", [10, 20, 30, 40, 50], 30, 2),
        ("interpolation_search", [10, 20, 30, 40, 50], 60, -1),
        ("exponential_search", [2, 3, 4, 10, 40], 10, 3),
        ("exponential_search", [2, 3, 4, 10, 40], 5, -1),
        ("fibonacci_search", [2, 3, 4, 10, 40], 10, 3),
        ("fibonacci_search", [2, 3, 4, 10, 40], 5, -1),
        ("ternary_search", [1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 3, 0, len([1, 2, 3, 4, 5, 6, 7, 8, 9]) - 1),
        ("ternary_search", [1, 2, 3, 4, 5, 6, 7, 8, 9], 10, -1, 0, len([1, 2, 3, 4, 5, 6, 7, 8, 9]) - 1),
        ("sentinel_linear_search", [10, 20, 30, 40, 50], 40, 3),
        ("sentinel_linear_search", [10, 20, 30, 40, 50], 60, -1),
        ("meta_binary_search", [1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 6, 0, len([1, 2, 3, 4, 5, 6, 7, 8, 9]) - 1),
        ("meta_binary_search", [1, 2, 3, 4, 5, 6, 7, 8, 9], 10, -1, 0, len([1, 2, 3, 4, 5, 6, 7, 8, 9]) - 1),
    ]

    for algorithm, array, target, expected, *args in test_cases:
        with self.subTest(algorithm=algorithm, target=target):
            self.run_search_test(algorithm, array, target, expected, *args)
