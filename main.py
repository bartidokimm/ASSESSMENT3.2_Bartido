"""Assessment 3.2 - Linear Data Structure
Main menu that runs each program from its own Python file."""

import array_program
import linked_list_program
import stack_program
import queue_program


def main():
    while True:
        print("\n===== LINEAR DATA STRUCTURES =====")
        print("1. Array")
        print("2. Linked List")
        print("3. Stack (LIFO)")
        print("4. Queue (FIFO)")
        print("5. Exit")
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            array_program.main()
        elif choice == "2":
            linked_list_program.main()
        elif choice == "3":
            stack_program.main()
        elif choice == "4":
            queue_program.main()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()