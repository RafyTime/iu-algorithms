class TwoStackQueue[T]:
    def __init__(self):
        self._stack_in: list[T] = []
        self._stack_out: list[T] = []

    def enqueue(self, item: T) -> None:
        self._stack_in.append(item)

    def _move_if_needed(self) -> None:
        if not self._stack_out:
            while self._stack_in:
                self._stack_out.append(self._stack_in.pop())

    def dequeue(self) -> T:
        self._move_if_needed()
        if not self._stack_out:
            raise IndexError("dequeue from empty queue")
        return self._stack_out.pop()

    def peek(self) -> T:
        self._move_if_needed()
        if not self._stack_out:
            raise IndexError("front of empty queue")
        return self._stack_out[-1]

    def is_empty(self) -> bool:
        return not self._stack_in and not self._stack_out


if __name__ == "__main__":
    q = TwoStackQueue[int]()
    for x in [1, 2, 3]:
        q.enqueue(x)
    print(q.dequeue())  # 1
    q.enqueue(4)
    print(q.dequeue())  # 2
    print(q.dequeue())  # 3
    print(q.dequeue())  # 4
