data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 27, 22, 32, 29],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
}

# indices sorted by Age descending
sorted_idx = sorted(range(len(data["Age"])), key=lambda i: data["Age"][i], reverse=True)
print(sorted_idx)  # [3, 4, 1, 0, 2]

# reconstruct dict with columns re-ordered according to those indices
data_sorted = {k: [v[i] for i in sorted_idx] for k, v in data.items()}
print(data_sorted)

print(data_sorted["Name"])  # ['David', 'Eva', 'Bob', 'Alice', 'Charlie']
print(data_sorted["Age"])  # [32, 29, 27, 24, 22]
