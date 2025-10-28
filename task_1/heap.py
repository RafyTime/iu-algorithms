"""
Heap Implementation for Rank Finding

A key q has rank k if there are k-1 keys less than q in the data structure.
For a heap, we need to extract k elements to find the k-th smallest.
"""

import heapq
from typing import List, Optional


class MinHeap:
    """
    A data structure that maintains elements in a min-heap.

    For rank finding, we need to extract k elements to find the k-th smallest.
    This is inefficient for rank queries but efficient for maintaining heap properties.
    """

    def __init__(self, elements: List[int]):
        """
        Initialize with a list of elements.

        Args:
            elements: List of integers to store in the heap
        """
        self.heap = elements.copy()
        heapq.heapify(self.heap)  # Convert to min-heap in O(n) time

    def find_rank(self, k: int) -> Optional[int]:
        """
        Find the key of rank k.

        Algorithm:
        1. Check if k is valid (1 <= k <= len(heap))
        2. Extract k-1 elements from the heap (they are smaller)
        3. The next element is the k-th smallest 
        4. Restore the heap by re-inserting extracted elements

        Time Complexity: O(k log n) - Extract k elements, each takes O(log n)
        Space Complexity: O(k) - Store extracted elements temporarily

        Args:
            k: The rank to find (1-indexed)

        Returns:
            The key of rank k, or None if k is invalid
        """
        # Validate input
        if k < 1 or k > len(self.heap):
            return None

        # Store original heap state
        original_heap = self.heap.copy()
        extracted = []

        try:
            # Extract k-1 elements (they are smaller than the k-th)
            for _ in range(k - 1):
                if self.heap:
                    extracted.append(heapq.heappop(self.heap))

            # The next element is the k-th smallest
            result = heapq.heappop(self.heap) if self.heap else None

            return result

        finally:
            # Restore the heap by re-inserting all extracted elements
            self.heap = original_heap.copy()

    def insert(self, value: int) -> None:
        """
        Insert a new value into the heap.

        Time Complexity: O(log n) - Heap insertion
        Space Complexity: O(1) - In-place insertion
        """
        heapq.heappush(self.heap, value)

    def __len__(self) -> int:
        """Return the number of elements in the heap."""
        return len(self.heap)

    def __str__(self) -> str:
        """String representation of the heap."""
        return f"MinHeap({sorted(self.heap)})"  # Show sorted for readability


class MaxHeap:
    """
    A data structure that maintains elements in a max-heap.

    For rank finding, we can use a different approach:
    - Extract n-k+1 elements to find the k-th smallest
    - This is still O(k log n) but might be more efficient for large k
    """

    def __init__(self, elements: List[int]):
        """
        Initialize with a list of elements.

        Args:
            elements: List of integers to store in the heap
        """
        # Convert to max-heap by negating values
        self.heap = [-x for x in elements]
        heapq.heapify(self.heap)

    def find_rank(self, k: int) -> Optional[int]:
        """
        Find the key of rank k using max-heap approach.

        Algorithm:
        1. Check if k is valid (1 <= k <= len(heap))
        2. Extract n-k+1 elements from the max-heap
        3. The next element is the k-th smallest
        4. Restore the heap

        Time Complexity: O((n-k) log n) - Extract n-k+1 elements
        Space Complexity: O(n-k) - Store extracted elements

        Args:
            k: The rank to find (1-indexed)

        Returns:
            The key of rank k, or None if k is invalid
        """
        # Validate input
        if k < 1 or k > len(self.heap):
            return None

        n = len(self.heap)

        # Store original heap state
        original_heap = self.heap.copy()
        extracted = []

        try:
            # Extract n-k elements from max-heap (keep k elements)
            for _ in range(n - k):
                if self.heap:
                    extracted.append(heapq.heappop(self.heap))

            # The next element is the k-th smallest
            result = -heapq.heappop(self.heap) if self.heap else None

            return result

        finally:
            # Restore the heap
            self.heap = original_heap.copy()

    def insert(self, value: int) -> None:
        """
        Insert a new value into the max-heap.

        Time Complexity: O(log n) - Heap insertion
        Space Complexity: O(1) - In-place insertion
        """
        heapq.heappush(self.heap, -value)

    def __len__(self) -> int:
        """Return the number of elements in the heap."""
        return len(self.heap)

    def __str__(self) -> str:
        """String representation of the heap."""
        return (
            f"MaxHeap({sorted([-x for x in self.heap])})"  # Show sorted for readability
        )


def demo_heap():
    """Demonstrate the heap implementations."""
    print("=== Heap Demo ===")

    # Create heaps with some values
    elements = [5, 2, 8, 1, 9, 3]

    print("MinHeap approach:")
    min_heap = MinHeap(elements)
    print(f"Initial heap: {min_heap}")

    # Test rank finding
    for k in range(1, len(min_heap) + 1):
        result = min_heap.find_rank(k)
        print(f"Rank {k}: {result}")

    print("\nMaxHeap approach:")
    max_heap = MaxHeap(elements)
    print(f"Initial heap: {max_heap}")

    # Test rank finding
    for k in range(1, len(max_heap) + 1):
        result = max_heap.find_rank(k)
        print(f"Rank {k}: {result}")

    # Test insertion
    print("\nInserting 4 into MinHeap...")
    min_heap.insert(4)
    print(f"After insertion: {min_heap}")
    print(f"Rank 3 after insertion: {min_heap.find_rank(3)}")


if __name__ == "__main__":
    demo_heap()
