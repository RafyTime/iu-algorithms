import copy
import heapq
from typing import Optional
from task_1.data_structures.sorted_array import SortedArray
from task_1.data_structures.linked_list import LinkedList
from task_1.data_structures.min_heap import MinHeap


def report_rank_k_sorted_array(d: SortedArray, k: int) -> Optional[int]:
    """Returns the key of rank k in a sorted array. Complexity: O(1)"""
    if 1 <= k <= len(d.data):
        return d.data[k - 1]
    return None


def report_rank_k_linked_list(d: LinkedList, k: int) -> Optional[int]:
    """Returns the key of rank k in a linked list. Complexity: O(n)"""
    if k < 1:
        return None
    current = d.head
    count = 1
    while current and count < k:
        current = current.next
        count += 1
    return current.data if current else None


def report_rank_k_min_heap(d: MinHeap, k: int) -> Optional[int]:
    """Returns the key of rank k in a min-heap. Complexity: O(k log n)"""
    if not (1 <= k <= len(d)):
        return None
    # We copy the heap to avoid destroying the original structure
    temp_heap = copy.deepcopy(d.heap)
    result = None
    for _ in range(k):
        result = heapq.heappop(temp_heap)
    return result
