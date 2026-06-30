import bisect


class SortedArray:
    """A simple sorted array implementation."""

    def __init__(self):
        self.data = []

    def insert(self, element: int):
        """Inserts an element into the array while maintaining order."""
        bisect.insort(self.data, element)

    def search(self, element: int) -> int:
        """Returns the index of the element, or -1 if not found."""
        index = bisect.bisect_left(self.data, element)
        if index < len(self.data) and self.data[index] == element:
            return index
        return -1

    def delete(self, element: int):
        """Removes the first occurrence of an element."""
        index = self.search(element)
        if index != -1:
            self.data.pop(index)

    def __repr__(self):
        return f"SortedArray({self.data})"
