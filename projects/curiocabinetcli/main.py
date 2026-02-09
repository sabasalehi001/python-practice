import json

def add_item(inventory):
    name = input("Item name: ").strip()
    if not name:
        print("Error: Item name cannot be empty.")
        return
    
    while True:
        try:
            quantity = int(input("Quantity: "))
            if quantity < 0:
                print("Error: Quantity must be a non-negative integer.")
            else:
                break
        except ValueError:
            print("Error: Invalid quantity. Please enter an integer.")

    inventory[name] = quantity
    print("Item added!")

def view_inventory(inventory):
    if not inventory:
        print("Your cabinet is empty.")
        return
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def search_item(inventory):
    search_term = input("Enter item name to search for: ").strip()
    if not search_term:
        print("Error: Search term cannot be empty.")
        return
    
    if search_term in inventory:
        print(f"{search_term}: {inventory[search_term]}")
    else:
        print("Item not found.")

def update_quantity(inventory):
    item_name = input("Enter item name to update: ").strip()
    if item_name not in inventory:
        print("Item not found in inventory.")
        return
    
    while True:
        try:
            new_quantity = int(input("Enter new quantity: "))
            if new_quantity < 0:
                print("Error: Quantity must be a non-negative integer.")
            else:
                break
        except ValueError:
            print("Error: Invalid quantity. Please enter an integer.")

    inventory[item_name] = new_quantity
    print("Quantity updated!")


def main():
    inventory = {}
    while True:
        print("\nCurioCabinetCLI")
        command = input("Enter command (add, view, search, update, exit): ").lower().strip()
        if command == "add":
            add_item(inventory)
        elif command == "view":
            view_inventory(inventory)
        elif command == "search":
            search_item(inventory)
        elif command == "update":
            update_quantity(inventory)
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
