# Task 1: Rank Finding Algorithms

This task implements algorithms to find the k-th smallest element (rank k) in different data structures.

## Problem Statement

We need to store n distinct key values in a data structure D. A key q is of rank k, if D has k-1 keys less than q. For a user given positive integer k, we would like to report the key of rank k stored in D.

## Implementations

### 1. Sorted Array (`sorted_array.py`)

**Algorithm**: Direct array access at index k-1

- **Time Complexity**: O(1) for rank finding
- **Space Complexity**: O(1) for rank finding
- **Insertion**: O(n) - need to find position and shift elements

**Best for**: Frequent rank queries, infrequent insertions

### 2. Linked List (`linked_list.py`)

**Algorithm**: Traverse k-1 nodes to reach the k-th element

- **Time Complexity**: O(k) for rank finding
- **Space Complexity**: O(1) for rank finding
- **Insertion**: O(n) - need to find insertion point

**Best for**: Small k values, when memory is limited

### 3. Heap (`heap.py`)

**Algorithm**: Extract k elements to find the k-th smallest

- **Time Complexity**: O(k log n) for rank finding
- **Space Complexity**: O(k) for rank finding (temporary storage)
- **Insertion**: O(log n) - heap insertion

**Best for**: Frequent insertions, infrequent rank queries

## Usage

### Running the Demo

```bash
python main.py
```

This will run all implementations and show:

- Individual demos for each data structure
- Performance comparison
- Complexity analysis

### Individual Testing

```python
from task_1.sorted_array import SortedArray
from task_1.linked_list import SortedLinkedList
from task_1.heap import MinHeap, MaxHeap

# Create data structures
elements = [5, 2, 8, 1, 9, 3]
sa = SortedArray(elements)
sll = SortedLinkedList(elements)
min_heap = MinHeap(elements)

# Find rank 3
print(sa.find_rank(3))      # O(1)
print(sll.find_rank(3))     # O(k)
print(min_heap.find_rank(3)) # O(k log n)
```

## Algorithm Analysis

### Time Complexity Comparison

| Data Structure | Rank Finding | Insertion | Best Use Case |
|----------------|--------------|-----------|---------------|
| Sorted Array   | O(1)         | O(n)      | Frequent queries |
| Linked List    | O(k)         | O(n)      | Small k, limited memory |
| Heap           | O(k log n)   | O(log n)  | Frequent insertions |

### Space Complexity

- **Sorted Array**: O(1) for rank finding
- **Linked List**: O(1) for rank finding
- **Heap**: O(k) for rank finding (temporary storage for extracted elements)

## Key Insights

1. **Sorted Array** is optimal for rank queries but expensive for insertions
2. **Heap** is optimal for insertions but expensive for rank queries
3. **Linked List** provides a middle ground but is generally less efficient
4. The choice depends on the operation frequency in your use case

## Files Structure

```md
task_1/
├── README.md           # This documentation
├── sorted_array.py     # Sorted array implementation
├── linked_list.py      # Linked list implementation
├── heap.py             # Heap implementation
└── TASK_1.md          # Original task description
```

## Testing

All implementations include comprehensive test cases that verify:

- Correct rank finding for valid inputs
- Proper handling of invalid inputs
- Insertion functionality
- Edge cases (empty structures, single elements)

Run the tests with:

```bash
python -m pytest task_1/  # If pytest is installed
# or
python main.py            # Run the demo
```
