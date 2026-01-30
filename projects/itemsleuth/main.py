import json

inventory = {}

def add_item():
    name = input("Enter item name: ").strip()
    if not name:
        print("Item name cannot be empty.")
        return
    while True:
        try:
            quantity = int(input("Enter initial quantity: "))
            if quantity < 0:
                print("Quantity must be a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    inventory[name] = quantity
    print(f"{name} added to inventory. Quantity: {quantity}")


def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def update_quantity():
    name = input("Enter item name to update: ").strip()
    if name not in inventory:
        print("Item not found in inventory.")
        return
    while True:
        try:
            quantity = int(input("Enter new quantity: "))
            if quantity < 0:
                print("Quantity must be a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    inventory[name] = quantity
    print(f"Quantity of {name} updated to {quantity}.")



if __name__ == "__main__":
    print("Welcome to ItemSleuth!")

    while True:
        print("\nChoose an action:")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Quantity")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_quantity()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
