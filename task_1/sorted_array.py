"""
Sorted Array Implementation for Rank Finding

A key q has rank k if there are k-1 keys less than q in the data structure.
For a sorted array, we can directly access the element at index k-1.
"""

from typing import List, Optional


class SortedArray:
    """
    A data structure that maintains elements in sorted order.

    For rank finding, we can directly access the element at index k-1
    since the array is already sorted.
    """

    def __init__(self, elements: List[int]):
        """
        Initialize with a list of elements and sort them.

        Args:
            elements: List of integers to store in sorted order
        """
        self.data = sorted(elements)

    def find_rank(self, k: int) -> Optional[int]:
        """
        Find the key of rank k.

        Algorithm:
        1. Check if k is valid (1 <= k <= len(data))
        2. Return element at index k-1 (since rank k means k-1 elements are smaller)

        Time Complexity: O(1) - Direct array access
        Space Complexity: O(1) - No additional space needed

        Args:
            k: The rank to find (1-indexed)

        Returns:
            The key of rank k, or None if k is invalid
        """
        # Validate input
        if k < 1 or k > len(self.data):
            return None

        # Direct access to the k-th smallest element
        return self.data[k - 1]

    def insert(self, value: int) -> None:
        """
        Insert a new value while maintaining sorted order.

        Time Complexity: O(n) - Need to find insertion point and shift elements
        Space Complexity: O(1) - In-place insertion
        """
        # Find insertion point using binary search
        left, right = 0, len(self.data)
        while left < right:
            mid = (left + right) // 2
            if self.data[mid] < value:
                left = mid + 1
            else:
                right = mid

        # Insert at the found position
        self.data.insert(left, value)

    def __len__(self) -> int:
        """Return the number of elements in the array."""
        return len(self.data)

    def __str__(self) -> str:
        """String representation of the sorted array."""
        return f"SortedArray({self.data})"


def demo_sorted_array():
    """Demonstrate the sorted array implementation."""
    print("=== Sorted Array Demo ===")

    # Create sorted array with some values
    elements = [5, 2, 8, 1, 9, 3]
    sa = SortedArray(elements)
    print(f"Initial array: {sa}")

    # Test rank finding
    for k in range(1, len(sa) + 1):
        result = sa.find_rank(k)
        print(f"Rank {k}: {result}")

    # Test invalid rank
    print(f"Rank {len(sa) + 1}: {sa.find_rank(len(sa) + 1)}")

    # Test insertion
    print("\nInserting 4...")
    sa.insert(4)
    print(f"After insertion: {sa}")
    print(f"Rank 3 after insertion: {sa.find_rank(3)}")


if __name__ == "__main__":
    demo_sorted_array()
