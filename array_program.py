"""Assessment 3.2 - Array
Adds each letter of a last name to an array, then removes the first
element one by one until the array is empty."""


def get_letters():
    name = input("Enter your last name (press Enter for BARTIDO): ").strip().upper()
    if not name:
        name = "BARTIDO"
    return [ch for ch in name if ch.isalpha()]


def show(items):
    return " ".join(items) if items else "EMPTY"


def main():
    letters = get_letters()
    array = []

    print("\n=== ARRAY ===")
    for letter in letters:
        array.append(letter)                      # insert at the end
        print(f"Inserted: {letter}   Array: {show(array)}")

    print(f"\nAdded: {show(array)}\n")

    while array:
        removed = array.pop(0)                    # delete the first element
        print(f"Removed: {removed}")
        print(f"Remaining: {show(array)}")


if __name__ == "__main__":
    main()