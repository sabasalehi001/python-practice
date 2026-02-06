import json

inventory = {}


def add_item(item_name, quantity):
  """Adds a new item to the inventory or updates the quantity if it exists."""
  if not isinstance(quantity, int) or quantity <= 0:
    print("Invalid quantity. Please enter a positive integer.")
    return

  if item_name in inventory:
    inventory[item_name] += quantity
    print(f"{item_name} quantity updated to {inventory[item_name]}."")
  else:
    inventory[item_name] = quantity
    print(f"{item_name} added to inventory with quantity {quantity}.")


def view_inventory():
  """Displays the current inventory."""
  if not inventory:
    print("Inventory is empty.")
    return

  print("Current Inventory:")
  for item, quantity in inventory.items():
    print(f"- {item}: {quantity}")


if __name__ == "__main__":
  while True:
    print("\nVestmentVault - Garment Inventory Tracker")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      item_name = input("Enter the name of the garment: ").strip()
      if not item_name:
          print("Item name cannot be empty.")
          continue

      try:
        quantity = int(input("Enter the quantity: "))
      except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

      add_item(item_name, quantity)

    elif choice == '2':
      view_inventory()

    elif choice == '3':
      print("Exiting VestmentVault.")
      break

    else:
      print("Invalid choice. Please try again.")
