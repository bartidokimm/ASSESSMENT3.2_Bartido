"""Assessment 3.2 - Queue (FIFO)
Enqueues each letter, then dequeues the front element one by one until
the queue is empty."""

from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def front(self):
        return self._items[0] if self._items else None

    def is_empty(self):
        return len(self._items) == 0

    def __str__(self):
        return " ".join(self._items) if self._items else "EMPTY"


def get_letters():
    name = input("Enter your last name (press Enter for BARTIDO): ").strip().upper()
    if not name:
        name = "BARTIDO"
    return [ch for ch in name if ch.isalpha()]


def main():
    letters = get_letters()
    queue = Queue()

    print("\n=== QUEUE (FIFO) ===")
    for letter in letters:
        queue.enqueue(letter)
        print(f"Enqueued: {letter}   Queue: {queue}")

    print(f"\nEnqueued: {queue}  (front = {queue.front()})\n")

    while not queue.is_empty():
        removed = queue.dequeue()
        print(f"Dequeued: {removed}")
        print(f"Remaining: {queue}")


if __name__ == "__main__":
    main()