def add_trinket(inventory):
    name = input("Enter trinket name: ")
    while True:
        try:
            quantity = int(input("Enter initial quantity: "))
            if quantity < 0:
                print("Quantity must be non-negative.")
            else:
                break
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    inventory[name] = quantity
    print("Trinket added!")


def view_trinkets(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    print("Trinkets:")
    for name, quantity in inventory.items():
        print(f"- {name}: {quantity}")

def update_trinket_quantity(inventory):
    name = input("Enter trinket name to update: ")
    if name not in inventory:
        print("Trinket not found.")
        return
    while True:
        try:
            quantity = int(input("Enter new quantity: "))
            if quantity < 0:
                print("Quantity must be non-negative.")
            else:
                break
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    inventory[name] = quantity
    print("Quantity updated!")


def main():
    inventory = {}

    while True:
        print("\nWelcome to TrinketTracer!\n")
        print("Options:")
        print("1. Add Trinket")
        print("2. View Trinkets")
        print("3. Update Trinket Quantity")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            add_trinket(inventory)
        elif choice == '2':
            view_trinkets(inventory)
        elif choice == '3':
            update_trinket_quantity(inventory)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
