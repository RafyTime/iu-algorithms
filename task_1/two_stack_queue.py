class TwoStackQueue:
    def __init__(self):
        self._stack_in = []
        self._stack_out = []

    def enqueue(self, item):
        self._stack_in.append(item)

    def _move_if_needed(self):
        if not self._stack_out:
            while self._stack_in:
                self._stack_out.append(self._stack_in.pop())

    def dequeue(self):
        self._move_if_needed()
        if not self._stack_out:
            raise IndexError("dequeue from empty queue")
        return self._stack_out.pop()

    def peek(self):
        self._move_if_needed()
        if not self._stack_out:
            raise IndexError("front of empty queue")
        return self._stack_out[-1]

    def is_empty(self):
        return not self._stack_in and not self._stack_out


if __name__ == "__main__":
    q = TwoStackQueue()
    for x in [1, 2, 3]:
        q.enqueue(x)
    print(q.dequeue())  # 1
    q.enqueue(4)
    print(q.dequeue())  # 2
    print(q.dequeue())  # 3
    print(q.dequeue())  # 4
