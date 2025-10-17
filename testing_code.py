import itertools
from collections import Counter

colors = ["red", "blue", "green"]
cycle_colors = itertools.cycle(colors)
result = [next(cycle_colors) for _ in range(10)]

counts = Counter(result)  # counts is a dictionary with counts of each color
print(counts)  # Example output: Counter({'red': 4, 'blue': 3, 'green': 3})
for color, count in counts.items():
    print(f"{color} {count}")
