"""Assessment 3.2 - Stack (LIFO)
Pushes each letter onto a stack, then pops the top element one by one
until the stack is empty."""


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        return self._items[-1] if self._items else None

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
    stack = Stack()

    print("\n=== STACK (LIFO) ===")
    for letter in letters:
        stack.push(letter)
        print(f"Pushed: {letter}   Stack: {stack}")

    print(f"\nPushed: {stack}  (top = {stack.peek()})\n")

    while not stack.is_empty():
        popped = stack.pop()
        print(f"Popped: {popped}")
        print(f"Remaining: {stack}")


if __name__ == "__main__":
    main()