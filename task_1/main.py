"""
Main demonstration of rank finding algorithms.

This module demonstrates three different data structures for finding
the k-th smallest element (rank k) in a collection of distinct integers.
"""

from task_1.sorted_array import SortedArray, demo_sorted_array
from task_1.linked_list import SortedLinkedList, demo_linked_list
from task_1.heap import MinHeap, MaxHeap, demo_heap


def compare_performance():
    """
    Compare the performance of different data structures for rank finding.

    This demonstrates the time complexity differences:
    - Sorted Array: O(1) for rank finding
    - Linked List: O(k) for rank finding
    - Heap: O(k log n) for rank finding
    """
    print("=== Performance Comparison ===")

    # Test data
    elements = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    k = 5  # Find the 5th smallest element

    print(f"Finding rank {k} in: {elements}")
    print()

    # Sorted Array - O(1) access
    sa = SortedArray(elements)
    result_sa = sa.find_rank(k)
    print(f"Sorted Array: {result_sa} (O(1) access)")

    # Linked List - O(k) traversal
    sll = SortedLinkedList(elements)
    result_sll = sll.find_rank(k)
    print(f"Linked List: {result_sll} (O(k) traversal)")

    # Min Heap - O(k log n) extraction
    min_heap = MinHeap(elements)
    result_heap = min_heap.find_rank(k)
    print(f"Min Heap: {result_heap} (O(k log n) extraction)")

    # Max Heap - O((n-k) log n) extraction
    max_heap = MaxHeap(elements)
    result_max_heap = max_heap.find_rank(k)
    print(f"Max Heap: {result_max_heap} (O((n-k) log n) extraction)")

    print("\nAll results should be the same!")


def analyze_complexity():
    """
    Analyze and explain the time complexity of each approach.
    """
    print("=== Complexity Analysis ===")
    print()
    print("1. SORTED ARRAY:")
    print("   - Rank Finding: O(1) - Direct array access")
    print("   - Insertion: O(n) - Need to find position and shift elements")
    print("   - Best for: Frequent rank queries, infrequent insertions")
    print()
    print("2. LINKED LIST:")
    print("   - Rank Finding: O(k) - Traverse k-1 nodes")
    print("   - Insertion: O(n) - Need to find insertion point")
    print("   - Best for: Small k values, when memory is limited")
    print()
    print("3. HEAP:")
    print("   - Rank Finding: O(k log n) - Extract k elements")
    print("   - Insertion: O(log n) - Heap insertion")
    print("   - Best for: Frequent insertions, infrequent rank queries")
    print()
    print("RECOMMENDATION:")
    print("   - Use Sorted Array for frequent rank queries")
    print("   - Use Heap for frequent insertions and infrequent rank queries")
    print("   - Use Linked List only when memory is very limited")


def main():
    """Main function to demonstrate all implementations."""
    print("Rank Finding Algorithms Demonstration")
    print("=" * 50)
    print()

    # Run individual demos
    demo_sorted_array()
    print()
    demo_linked_list()
    print()
    demo_heap()
    print()

    # Compare performance
    compare_performance()
    print()

    # Analyze complexity
    analyze_complexity()


if __name__ == "__main__":
    main()
