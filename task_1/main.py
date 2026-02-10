import random
from task_1.data_structures.sorted_array import SortedArray
from task_1.data_structures.linked_list import LinkedList
from task_1.data_structures.min_heap import MinHeap
from task_1.reporting_algorithms import (
    report_rank_k_sorted_array,
    report_rank_k_linked_list,
    report_rank_k_min_heap
)

def main():
    # Generate random data
    n = 10  # number of elements
    keys = random.sample(range(1, 101), n)  # n distinct keys between 1 and 100
    k = random.randint(1, n)  # random rank between 1 and n
    
    # 1. Initialize data structures
    s_array = SortedArray()
    l_list_sorted = LinkedList()
    m_heap = MinHeap()
    
    # Populate structures
    sorted_keys = sorted(keys)
    for key in keys:
        s_array.insert(key)
        m_heap.push(key)
    
    for key in sorted_keys:
        l_list_sorted.append(key)
    
    print(f"--- Reporting Rank k={k} (Randomized) ---")
    print(f"Keys (randomly generated): {keys}")
    print(f"Sorted Keys: {sorted_keys}")
    print("-" * 30)
    
    # 2. Run and print results
    res_array = report_rank_k_sorted_array(s_array, k)
    res_list = report_rank_k_linked_list(l_list_sorted, k)
    res_heap = report_rank_k_min_heap(m_heap, k)
    
    print(f"{'Data Structure':<20} | {'Result':<10} | {'Complexity'}")
    print("-" * 50)
    print(f"{'Sorted Array':<20} | {str(res_array):<10} | O(1)")
    print(f"{'Linked List':<20} | {str(res_list):<10} | O(n)")
    print(f"{'Min-Heap':<20} | {str(res_heap):<10} | O(k log n)")
    print("-" * 50)
    print(f"The key of rank {k} is: {sorted_keys[k-1]}")

if __name__ == "__main__":
    main()
