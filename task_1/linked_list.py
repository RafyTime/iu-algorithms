"""
Linked List Implementation for Rank Finding

A key q has rank k if there are k-1 keys less than q in the data structure.
For a linked list, we need to traverse to find the k-th smallest element.
"""

from typing import Optional, List


class ListNode:
    """Node for the linked list."""

    def __init__(self, value: int):
        self.value = value
        self.next: Optional["ListNode"] = None


class SortedLinkedList:
    """
    A data structure that maintains elements in sorted order using a linked list.

    For rank finding, we need to traverse the list to find the k-th element.
    """

    def __init__(self, elements: List[int]):
        """
        Initialize with a list of elements and sort them.

        Args:
            elements: List of integers to store in sorted order
        """
        self.head: Optional[ListNode] = None
        self.size = 0

        # Insert elements in sorted order
        for element in sorted(elements):
            self.insert(element)

    def find_rank(self, k: int) -> Optional[int]:
        """
        Find the key of rank k.

        Algorithm:
        1. Check if k is valid (1 <= k <= size)
        2. Traverse the list k-1 steps to reach the k-th element
        3. Return the value at that position

        Time Complexity: O(k) - Need to traverse k-1 nodes
        Space Complexity: O(1) - Only using a pointer

        Args:
            k: The rank to find (1-indexed)

        Returns:
            The key of rank k, or None if k is invalid
        """
        # Validate input
        if k < 1 or k > self.size:
            return None

        # Traverse to the k-th element
        current = self.head
        for _ in range(k - 1):
            current = current.next

        return current.value

    def insert(self, value: int) -> None:
        """
        Insert a new value while maintaining sorted order.

        Time Complexity: O(n) - Need to find insertion point
        Space Complexity: O(1) - Only creating one new node
        """
        new_node = ListNode(value)

        # Case 1: Insert at head
        if self.head is None or value <= self.head.value:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return

        # Case 2: Find insertion point
        current = self.head
        while current.next is not None and current.next.value < value:
            current = current.next

        # Insert after current node
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self.size

    def __str__(self) -> str:
        """String representation of the linked list."""
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return f"SortedLinkedList({values})"


def demo_linked_list():
    """Demonstrate the linked list implementation."""
    print("=== Linked List Demo ===")

    # Create sorted linked list with some values
    elements = [5, 2, 8, 1, 9, 3]
    sll = SortedLinkedList(elements)
    print(f"Initial list: {sll}")

    # Test rank finding
    for k in range(1, len(sll) + 1):
        result = sll.find_rank(k)
        print(f"Rank {k}: {result}")

    # Test invalid rank
    print(f"Rank {len(sll) + 1}: {sll.find_rank(len(sll) + 1)}")

    # Test insertion
    print("\nInserting 4...")
    sll.insert(4)
    print(f"After insertion: {sll}")
    print(f"Rank 3 after insertion: {sll.find_rank(3)}")


if __name__ == "__main__":
    demo_linked_list()
