from typing import TypedDict, List


class DataDict(TypedDict):
    Name: List[str]
    Age: List[int]
    City: List[str]


data: DataDict = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 27, 22, 32, 29],
    "City": ["NY", "LA", "Chicago", "Houston", "Phoenix"],
}

# build index list 0..4
indices = list(range(len(data["Age"])))  # [0, 1, 2, 3, 4]


# def sort_key(i):
#     return data["Age"][i]


# # sort indices by Age descending
# sorted_idx = sorted(indices, key=sort_key, reverse=True)
# print(sorted_idx)  # [3, 4, 1, 0, 2]


# sort indices by the Age value at that index (descending)
sorted_idx = sorted(indices, key=lambda i: data["Age"][i], reverse=True)
print(sorted_idx)
