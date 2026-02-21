"""
Many built-in functions and methods return iterators in Python:
***************************************************************

Built-in functions that return iterators:
****************************************
1.map(func, iterable) - applies function to each item
2.filter(predicate, iterable) - filters items by condition
3.zip(iter1, iter2, ...) - pairs up elements from multiple iterables
4.reversed(seq) - reverses a sequence
5.enumerate(iterable) - adds index to items
6.range(start, stop) - generates number sequence
7.iter(iterable) - explicitly creates iterator
8.open(file) - file objects are iterators over lines

Dictionary methods:
*******************
9.dict.keys() - returns dict_keys (iterable view)
10.dict.values() - returns dict_values (iterable view)
11.dict.items() - returns dict_items (iterable view)

String methods returning not iterators but lists:
***********************************************
12. str.split() - splits string into list by delimiter
12. str.split() returns a list (NOT iterator)
    Also, str.splitlines() returns list too

itertools module (all return iterators):
***************************************
13.itertools.chain(*iterables) - chains iterables together
14.itertools.cycle(iterable) - repeats infinitely
15.itertools.islice(iterable, n) - slices iterator
16.itertools.combinations(iterable, r) - combinations
17.itertools.permutations(iterable, r) - permutations
18.itertools.groupby(iterable, key) - groups consecutive items
19.itertools.count(start) - infinite counter
20.itertools.repeat(value, times) - repeats value
"""

# Generator expressions:

gen = (x * 2 for x in range(5))  # Returns generator (iterator)
lst = [x * 2 for x in range(5)]  # Returns list
print("=" * 70)
print("Generator vs List Comprehension")
print(f"Generator: {gen}")
print(f"List: {lst}")
print("=" * 70)

# Key point: Iterators are memory-efficient for large datasets but can only be
# consumed once. Convert to list() if you need to reuse them.
# Iterator = has both __iter__() AND __next__() (enumerate, filter, map, generators)
# Iterator (has both __iter__ and __next__)
enum_obj = enumerate(["a", "b"])
print(hasattr(enum_obj, "__iter__"))  # True
print(hasattr(enum_obj, "__next__"))  # True

# List is NOT an iterator (only has __iter__, not __next__)
my_list = [1, 2, 3]
print(hasattr(my_list, "__iter__"))  # True (it's iterable)
print(hasattr(my_list, "__next__"))  # False (not an iterator)

# To get an iterator from a list:
list_iter = iter(my_list)
print(hasattr(list_iter, "__next__"))  # True (now it's an iterator)

# An object is an iterator if it has both these methods:
# *******************************************************
# __iter__() - returns the iterator object itself
# __next__() - returns the next item or raises StopIteration

###########################################################
# DEMO OF ENUMERATE RETURNING AN ITERATOR
"""Demonstrating enumerate() returns an iterator"""

# Basic example
fruits = ["apple", "banana", "cherry"]
enum_obj = enumerate(fruits)

print(f"Type: {type(enum_obj)}")  # <class 'enumerate'>
print(f"Is iterator: {hasattr(enum_obj, '__iter__') and hasattr(enum_obj, '__next__')}")
print()

# First iteration - works fine
print("First iteration:")
for index, fruit in enum_obj:
    print(f"  {index}: {fruit}")
print()

# Second iteration - nothing happens (iterator exhausted)
print("Second iteration (should be empty):")
for index, fruit in enum_obj:
    print(f"  {index}: {fruit}")
print("  (No output - iterator is exhausted!)")
print()

# Using next() to manually consume iterator
print("Manual consumption with next():")
enum_obj2 = enumerate(["red", "green", "blue"])
print(f"  {next(enum_obj2)}")  # (0, 'red')
print(f"  {next(enum_obj2)}")  # (1, 'green')
print(f"  {next(enum_obj2)}")  # (2, 'blue')
# print(next(enum_obj2))  # Would raise StopIteration
print()

# enumerate with start parameter
print("enumerate with start=1:")
for index, fruit in enumerate(["mango", "orange"], start=1):
    print(f"  {index}: {fruit}")
print()

# Converting to list (consumes the iterator)
print("Converting to list:")
enum_obj3 = enumerate(["x", "y", "z"])
result = list(enum_obj3)
print(f"  {result}")  # [(0, 'x'), (1, 'y'), (2, 'z')]
# Now enum_obj3 is exhausted
print(f"  After list(): {list(enum_obj3)}")  # []
print("=" * 70)
