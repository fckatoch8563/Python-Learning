# 1 EXAMPLE ON UNDERSTANDING HEAPQ MODULE
# *****************************************


import heapq


service_queue = []

# Add people to the queue with (priority, name)
heapq.heappush(service_queue, (2, "Jim"))
print("After pushing (2, 'Jim'):", service_queue)

heapq.heappush(service_queue, (1, "Pam"))
print("After pushing (1, 'Pam'):", service_queue)

heapq.heappush(service_queue, (3, "Dwight"))
print("After pushing (3, 'Dwight'):", service_queue)

heapq.heappush(service_queue, (2, "Michael"))
print("After pushing (2, 'Michael'):", service_queue)

# Add more names with different priorities
heapq.heappush(service_queue, (0, "Angela"))
print("After pushing (0, 'Angela'):", service_queue)

heapq.heappush(service_queue, (4, "Stanley"))
print("After pushing (4, 'Stanley'):", service_queue)

heapq.heappush(service_queue, (1, "Oscar"))
print("After pushing (1, 'Oscar'):", service_queue)

# Pop elements to show priority order
print("\nServing order:")
while service_queue:
    priority, name = heapq.heappop(service_queue)
    print(f"Serving {name} with priority {priority}")

"""
After pushing (2, 'Jim'): [(2, 'Jim')]
After pushing (1, 'Pam'): [(1, 'Pam'), (2, 'Jim')]
After pushing (3, 'Dwight'): [(1, 'Pam'), (2, 'Jim'), (3, 'Dwight')]
After pushing (2, 'Michael'): [(1, 'Pam'), (2, 'Jim'), (3, 'Dwight'), (2, 'Michael')]
Serving Pam with priority 1
Serving Jim with priority 2
Serving Michael with priority 2
Serving Dwight with priority 3
"""
##############################################################################
# EXAMPLE 2: Understanding How heappop() Works
# *****************************************

import heapq

# Create a new heap with multiple items
task_queue = []
tasks = [
    (5, "Task E"),
    (2, "Task B"),
    (7, "Task G"),
    (1, "Task A"),
    (4, "Task D"),
    (3, "Task C"),
    (6, "Task F"),
]

print("Adding all tasks to the heap:")
for task in tasks:
    heapq.heappush(task_queue, task)

print(f"Initial heap: {task_queue}")
print(f"Heap has {len(task_queue)} items\n")

# Now demonstrate step-by-step removal
print("=" * 60)
print("REMOVING ITEMS ONE BY ONE:")
print("=" * 60)

step = 1
while task_queue:
    print(f"\nStep {step}:")
    print(f"Before pop: {task_queue}")
    print(f"Smallest element at root (index 0): {task_queue[0]}")

    # Pop the smallest element
    removed = heapq.heappop(task_queue)
    print(f"Popped: {removed}")

    if task_queue:
        print(f"After pop:  {task_queue}")
        print(f"New smallest at root: {task_queue[0]}")
    else:
        print("Heap is now empty!")

    step += 1

print("\n" + "=" * 60)
print("KEY INSIGHTS:")
print("=" * 60)
print("1. heappop() always removes the SMALLEST element (at index 0)")
print("2. After removal, the last element moves to root position")
print("3. The heap then 'sifts down' to maintain heap property")
print("4. This ensures O(log n) time complexity for removal")
print("5. The heap is always partially sorted, not fully sorted")
#######################################################################################
# 3 EXAMPLE

import heapq

# Create a new heap with multiple items
task_queue = []
tasks = [
    (5, "Task E"),
    (2, "Task B"),
    (7, "Task G"),
    (1, "Task A"),
    (4, "Task D"),
    (3, "Task C"),
    (6, "Task F"),
]

print("Adding all tasks to the heap:")
for task in tasks:
    heapq.heappush(task_queue, task)

print(f"Initial heap: {task_queue}")
print(f"Heap has {len(task_queue)} items\n")

# REMOVING ITEMS BASED ON PRIORITY
print("Removing tasks based on priority:")
while task_queue:
    next_task = heapq.heappop(task_queue)
    print(f"Processing {next_task} | Remaining heap: {task_queue}")

print("\nAll tasks processed.")
#########################################################################################
# 4. EXAMPLE
import heapq

# Start with an empty list
heap = []

# Insert values into the heap using a for loop
values = [7, 2, 5, 1, 9, 3]
print("Inserting values into the heap:")
for v in values:
    heapq.heappush(heap, v)
    print(f"After pushing {v}: {heap}")

print("\nRemoving values from the heap (always smallest first):")
while heap:
    smallest = heapq.heappop(heap)
    print(f"Popped {smallest}, heap is now: {heap}")

##################################################################################
# EXAMPLE: Manual Sifting in a List (Min-Heap Logic)
# -----------------------------------------------
# This code shows how the heap property is maintained by sifting up during insertion.

numbers = [7, 2, 5, 1, 9, 3]
heap = []

print("Building a heap by inserting one by one and sifting up:")


def sift_up(heap, idx):
    # Sift the element at idx up to maintain heap property
    while idx > 0:
        parent = (idx - 1) // 2
        if heap[idx] < heap[parent]:
            heap[idx], heap[parent] = heap[parent], heap[idx]
            idx = parent
        else:
            break


for num in numbers:
    heap.append(num)
    print(f"Inserted {num}, before sifting: {heap}")
    sift_up(heap, len(heap) - 1)
    print(f"After sifting: {heap}")

print("\nFinal heap:", heap)

# Now show sifting down during removal
print("\nRemoving items with manual sift-down:")


def sift_down(heap, idx):
    n = len(heap)
    while True:
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx
        if left < n and heap[left] < heap[smallest]:
            smallest = left
        if right < n and heap[right] < heap[smallest]:
            smallest = right
        if smallest != idx:
            heap[idx], heap[smallest] = heap[smallest], heap[idx]
            idx = smallest
        else:
            break


while heap:
    print(f"\nHeap before pop: {heap}")
    # Remove root (smallest)
    heap[0], heap[-1] = heap[-1], heap[0]
    smallest = heap.pop()
    print(f"Popped {smallest}")
    if heap:
        sift_down(heap, 0)
        print(f"Heap after sifting down: {heap}")
    else:
        print("Heap is now empty!")

    ####################################################################################
    # REAL LIFE EXAMPLE USING VIP PARKING SYSTEM.abs
    # ************************************************

    import heapq

# Each entry is (priority, ticket_holder)
parking_queue = []

# Add people with different ticket types
heapq.heappush(parking_queue, (2, "Alice (Silver)"))
heapq.heappush(parking_queue, (1, "Bob (Gold)"))
heapq.heappush(parking_queue, (3, "Charlie (Regular)"))
heapq.heappush(parking_queue, (1, "Diana (Gold)"))
heapq.heappush(parking_queue, (2, "Eve (Silver)"))

print("Parking order (VIPs first):")
while parking_queue:
    priority, name = heapq.heappop(parking_queue)
    print(f"{name} with priority {priority} leaves the parking slot")


# OUTPUT
"""
Bob (Gold) with priority 1 gets a parking spot
Diana (Gold) with priority 1 gets a parking spot
Alice (Silver) with priority 2 gets a parking spot
Eve (Silver) with priority 2 gets a parking spot
Charlie (Regular) with priority 3 gets a parking spot
"""
######################################################################################


import heapq

# Each entry is (priority, patient_name)
triage_queue = []

# Add patients with different priorities
heapq.heappush(triage_queue, (2, "Alice (Serious)"))
heapq.heappush(triage_queue, (1, "Bob (Critical)"))
heapq.heappush(triage_queue, (3, "Charlie (Stable)"))
heapq.heappush(triage_queue, (1, "Diana (Critical)"))
heapq.heappush(triage_queue, (2, "Eve (Serious)"))

print("Treatment order (most critical first):")
while triage_queue:
    priority, name = heapq.heappop(triage_queue)
    print(f"{name} with priority {priority} is treated")

# output
"""
Bob (Critical) with priority 1 is treated
Diana (Critical) with priority 1 is treated
Alice (Serious) with priority 2 is treated
Eve (Serious) with priority 2 is treated
Charlie (Stable) with priority 3 is treated
"""
"""
The heap property (as used in heapq) is preferred over filter(), sorted(), etc. in certain scenarios because:
*************************************************************************************************************

Efficiency:
Heaps allow you to insert and remove the smallest (or largest) item in O(log n) time.
sorted() sorts the entire list, which is O(n log n) time.
filter() just selects items, but does not sort or maintain order.

Use Cases:
When you need quick access to the smallest/largest item repeatedly (priority queue).
When you want to maintain a running list of the top N smallest/largest items (using heapq.nsmallest/nlargest).
When you need to merge multiple sorted streams efficiently (heapq.merge).

Practical uses:
Task scheduling (always process the next most urgent task)
Dijkstra’s shortest path algorithm (priority queue for nodes)
Event simulation (process next event in order)
Real-time data streams (keep top N items efficiently)
Job queues, bandwidth management, and more

In summary:
Heaps are best when you need fast, repeated access to the 
smallest/largest element, not just a one-time sort or filter.
"""
###################################################################################################################
