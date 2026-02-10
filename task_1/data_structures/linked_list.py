from typing import Optional

class Node:
    """A node in a linked list."""
    def __init__(self, data: int):
        self.data = data
        self.next: Optional[Node] = None

class LinkedList:
    """A simple singly linked list."""
    def __init__(self):
        self.head: Optional[Node] = None

    def append(self, data: int):
        """Adds a new node with data to the end of the list."""
        if not self.head:
            self.head = Node(data)
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def delete(self, data: int):
        """Removes the first node containing the given data."""
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next:
            current.next = current.next.next

    def display(self) -> list[int]:
        """Returns the list elements as a Python list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def __repr__(self):
        return f"LinkedList({self.display()})"
