from typing import Optional
import heapq


class MinHeap:
    """A simple min-heap wrapper around heapq."""

    def __init__(self):
        self.heap = []

    def push(self, val: int):
        """Adds an element to the heap."""
        heapq.heappush(self.heap, val)

    def pop(self) -> Optional[int]:
        """Removes and returns the smallest element."""
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def peek(self) -> Optional[int]:
        """Returns the smallest element without removing it."""
        return self.heap[0] if self.heap else None

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return f"MinHeap({self.heap})"
