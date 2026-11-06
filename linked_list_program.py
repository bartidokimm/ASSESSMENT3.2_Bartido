"""Assessment 3.2 - Linked List
Inserts each letter at the end of a singly linked list, then deletes the
first node one by one until the list is empty."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_first(self):
        if self.head is None:
            return None
        removed = self.head.data
        self.head = self.head.next
        return removed

    def is_empty(self):
        return self.head is None

    def __str__(self):
        if self.head is None:
            return "EMPTY"
        parts, current = [], self.head
        while current:
            parts.append(current.data)
            current = current.next
        return " -> ".join(parts)


def get_letters():
    name = input("Enter your last name (press Enter for BARTIDO): ").strip().upper()
    if not name:
        name = "BARTIDO"
    return [ch for ch in name if ch.isalpha()]


def main():
    letters = get_letters()
    linked_list = LinkedList()

    print("\n=== LINKED LIST ===")
    for letter in letters:
        linked_list.insert_end(letter)
        print(f"Inserted: {letter}   List: {linked_list}")

    print(f"\nAdded: {linked_list}\n")

    while not linked_list.is_empty():
        removed = linked_list.delete_first()
        print(f"Removed: {removed}")
        print(f"Remaining: {linked_list}")


if __name__ == "__main__":
    main()