import pandas as pd
import matplotlib.pyplot as plt  # Correct import
import os

# Define paths to the benchmark result files
root_folder = "/Users/adrijadhar/Desktop/Sort_Search_Library"
results_folder = os.path.join(root_folder, "results")
benchmark_compare_folder = os.path.join(results_folder, "benchmark_compare")

# Create the results folder if it doesn't exist
os.makedirs(results_folder, exist_ok=True)
os.makedirs(benchmark_compare_folder, exist_ok=True)

# Corrected paths to the benchmark result files
sorting_unified_results_path = os.path.join(results_folder, "sorting_benchmark_results_unified.md")
sorting_separate_results_path = os.path.join(results_folder, "sorting_benchmark_results.md")
searching_unified_results_path = os.path.join(results_folder, "searching_benchmark_results_unified.md")
searching_separate_results_path = os.path.join(results_folder, "searching_benchmark_results.md")

# Full lists of sorting and searching algorithms to compare
sorting_algorithms = [
    "bubble_sort", "merge_sort", "quick_sort", "selection_sort", "insertion_sort",
    "heap_sort", "counting_sort", "radix_sort", "shell_sort",
    "bucket_sort", "cocktail_shaker_sort", "comb_sort", "gnome_sort",
    "tim_sort", "pancake_sort", "tree_sort"
]

searching_algorithms = [
    "linear_search", "binary_search", "jump_search", "interpolation_search",
    "exponential_search", "fibonacci_search", "ternary_search",
    "sentinel_linear_search", "meta_binary_search"
]

# Headers for sorting and searching benchmark files
sorting_headers = [
    "Input Size", "bubble_sort", "merge_sort", "quick_sort", "selection_sort", 
    "insertion_sort", "heap_sort", "counting_sort", "radix_sort", "shell_sort", 
    "bucket_sort", "cocktail_shaker_sort", "comb_sort", "gnome_sort", 
    "tim_sort", "pancake_sort", "tree_sort"
]

searching_headers = [
    "Input Size", "linear_search", "binary_search", "jump_search", 
    "interpolation_search", "exponential_search", "fibonacci_search", 
    "ternary_search", "sentinel_linear_search", "meta_binary_search"
]

# Function to read benchmark results from markdown and ensure all expected columns exist
def read_benchmark_file(file_path, expected_columns, header_names):
    # Read the markdown, skipping the first 2 rows, which are headers
    df = pd.read_csv(file_path, delimiter="|", skiprows=2, skipinitialspace=True)

    # Remove unnamed columns that might be parsing artifacts
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Manually set the correct column headers
    df.columns = header_names

    # Debugging: Print the columns after manually setting headers
    print(f"Columns in {file_path} after setting headers: {df.columns.tolist()}")

    # Check if 'Input Size' column exists, if not raise an error
    if 'Input Size' not in df.columns:
        raise KeyError("'Input Size' column is missing from the parsed DataFrame.")

    # Move 'Input Size' to the first position
    input_size_column = df.pop('Input Size')
    df.insert(0, 'Input Size', input_size_column)

    # Convert all columns to appropriate types
    df['Input Size'] = pd.to_numeric(df['Input Size'], errors='coerce')
    df.dropna(subset=['Input Size'], inplace=True)
    df['Input Size'] = df['Input Size'].astype(int)

    # Convert other columns to numeric values
    for column in df.columns:
        if column != 'Input Size':
            df[column] = pd.to_numeric(df[column], errors='coerce')

    # Fill NaN values with 0 for all other columns
    df.fillna(0, inplace=True)

    # Debugging: Print the first few rows to verify the data
    print(f"First few rows of {file_path} after cleaning:\n", df.head())

    return df

# Load data with updated header assignments
try:
    sorting_unified = read_benchmark_file(sorting_unified_results_path, sorting_algorithms, sorting_headers)
except KeyError as e:
    print(f"Error reading sorting unified benchmark file: {e}")

try:
    sorting_separate = read_benchmark_file(sorting_separate_results_path, sorting_algorithms, sorting_headers)
except FileNotFoundError as e:
    print(f"Error reading sorting separate benchmark file: {e}")

try:
    searching_unified = read_benchmark_file(searching_unified_results_path, searching_algorithms, searching_headers)
except KeyError as e:
    print(f"Error reading searching unified benchmark file: {e}")

try:
    searching_separate = read_benchmark_file(searching_separate_results_path, searching_algorithms, searching_headers)
except FileNotFoundError as e:
    print(f"Error reading searching separate benchmark file: {e}")

# Continue with the rest of the script...


# Load data
sorting_unified = read_benchmark_file(sorting_unified_results_path, sorting_algorithms, sorting_headers)
sorting_separate = read_benchmark_file(sorting_separate_results_path, sorting_algorithms, sorting_headers)
searching_unified = read_benchmark_file(searching_unified_results_path, searching_algorithms, searching_headers)
searching_separate = read_benchmark_file(searching_separate_results_path, searching_algorithms, searching_headers)


# Calculate Differences and Optimization Percentage
def calculate_differences_and_percentage(separate_df, unified_df, algorithms):
    results = pd.DataFrame()
    results["Input Size"] = separate_df["Input Size"]

    for algorithm in algorithms:
        results[f"{algorithm} - Separate"] = separate_df[algorithm]
        results[f"{algorithm} - Unified"] = unified_df[algorithm]
        results[f"{algorithm} - Difference"] = unified_df[algorithm] - separate_df[algorithm]

        # Avoid division by zero for percentage change
        results[f"{algorithm} - Percentage Change"] = results.apply(
            lambda row: 0 if row[f"{algorithm} - Separate"] == 0 else 
                        (row[f"{algorithm} - Difference"] / row[f"{algorithm} - Separate"]) * 100,
            axis=1
        ).round(2)

    # Print results for debugging
    print("Calculated differences and percentage change:")
    print(results.head())

    return results

# Calculate differences for sorting and searching
sorting_differences = calculate_differences_and_percentage(sorting_separate, sorting_unified, sorting_algorithms)
searching_differences = calculate_differences_and_percentage(searching_separate, searching_unified, searching_algorithms)

# Save the differences to markdown
sorting_diff_table_path = os.path.join(results_folder, "sorting_differences_table.md")
searching_diff_table_path = os.path.join(results_folder, "searching_differences_table.md")
sorting_differences.to_markdown(sorting_diff_table_path, index=False)
searching_differences.to_markdown(searching_diff_table_path, index=False)

# Create and save visualizations
def create_comparison_plots(differences_df, algorithms, result_type):
    for algorithm in algorithms:
        plt.figure(figsize=(10, 5))
        input_sizes = differences_df["Input Size"]

        # Plot Separate Approach
        plt.bar(input_sizes - 20, differences_df[f"{algorithm} - Separate"], width=40, label="Separate Approach", alpha=0.7, color='b')
        
        # Plot Unified Approach (using a slight offset to distinguish if identical)
        plt.bar(input_sizes + 20, differences_df[f"{algorithm} - Unified"], width=40, label="Unified Approach", alpha=0.7, color='r')

        # If both approaches are the same, plot the unified again with transparency
        if (differences_df[f"{algorithm} - Separate"] == differences_df[f"{algorithm} - Unified"]).all():
            plt.bar(input_sizes, differences_df[f"{algorithm} - Unified"], width=20, label="Identical Values", alpha=0.3, color='g')

        plt.xlabel("Input Size")
        plt.ylabel("Time (seconds)")
        plt.title(f"{result_type.capitalize()} Performance Comparison - {algorithm}")
        plt.legend()
        plt.grid(axis='y')

        # Save plot
        plot_path = os.path.join(results_folder, f"{result_type.lower()}_{algorithm.lower().replace(' ', '_')}_comparison.png")
        plt.savefig(plot_path)
        plt.show()

# Create bar charts for sorting and searching
create_comparison_plots(sorting_differences, sorting_algorithms, "sorting")
create_comparison_plots(searching_differences, searching_algorithms, "searching")

# Summary of Improvements
def summarize_optimization(results_df, algorithms):
    summary = []

    for algorithm in algorithms:
        for idx, row in results_df.iterrows():
            input_size = row["Input Size"]
            percentage_change = row[f"{algorithm} - Percentage Change"]
            if percentage_change < 0:
                summary.append(f"For {algorithm} at input size {input_size}, Unified approach was better by {-percentage_change}%")
            elif percentage_change > 0:
                summary.append(f"For {algorithm} at input size {input_size}, Separate approach was better by {percentage_change}%")
            else:
                summary.append(f"For {algorithm} at input size {input_size}, both approaches performed the same.")
    
    return summary

# Generate summaries for sorting and searching
sorting_optimization_summary = summarize_optimization(sorting_differences, sorting_algorithms)
searching_optimization_summary = summarize_optimization(searching_differences, searching_algorithms)

# Save the summaries to text files
sorting_summary_path = os.path.join(results_folder, "sorting_optimization_summary.txt")
searching_summary_path = os.path.join(results_folder, "searching_optimization_summary.txt")
with open(sorting_summary_path, 'w') as f:
    for line in sorting_optimization_summary:
        f.write(line + "\n")

with open(searching_summary_path, 'w') as f:
    for line in searching_optimization_summary:
        f.write(line + "\n")

# Print summaries
print("Sorting Optimization Summary:")
for line in sorting_optimization_summary:
    print(line)

print("\nSearching Optimization Summary:")
for line in searching_optimization_summary:
    print(line)
