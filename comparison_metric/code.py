import pandas as pd
from io import StringIO

# File path for the sorting benchmark results
file_path = '/Users/adrijadhar/Desktop/Sort_Search_Library/results/sorting_benchmark_results.md'

# Read the table from the markdown file
with open(file_path, 'r') as file:
    table_string = file.read()

# Convert the markdown table to DataFrame
# Skip the first two rows, which are the table header and header separator
data = StringIO(table_string)
df = pd.read_csv(data, sep="|", skiprows=2, skipinitialspace=True)

# Remove any unnamed columns that are artifacts of parsing
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Manually set the correct column names for sorting benchmarks
df.columns = [
    'bubble_sort', 'merge_sort', 'quick_sort', 'selection_sort', 'insertion_sort',
    'heap_sort', 'counting_sort', 'radix_sort', 'shell_sort', 'bucket_sort',
    'cocktail_shaker_sort', 'comb_sort', 'gnome_sort', 'tim_sort', 'pancake_sort',
    'tree_sort', 'Input Size'
]

# Move "Input Size" column to the first position
columns = list(df.columns)
columns.insert(0, columns.pop(columns.index("Input Size")))
df = df[columns]

# Save the modified DataFrame back to a markdown file
df.to_markdown('/Users/adrijadhar/Desktop/Sort_Search_Library/results/sorting_benchmark_results_modified.md', index=False)

print("The modified markdown file has been saved.")
