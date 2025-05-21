#create inventory management system using loops to display the inventory
# and allow the user to add, remove, or update items in the inventory.

# Create a dictionary to store the inventory
inventory = {}
# Function to display the inventory
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
            
# Function to add an item to the inventory
def add_item():
    item = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))
    # Check if the item already exists in the inventory
    # If it does, update the quantity
    # If it doesn't, add the item to the inventory
    if item in inventory: 
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"{quantity} {item}(s) added to the inventory.")
    
# Function to remove an item from the inventory
def remove_item():
    item = input("Enter the item name to remove: ")
    if item in inventory:
        quantity = int(input("Enter the quantity to remove: "))
        if quantity >= inventory[item]:
            del inventory[item]
            print(f"{item} removed from the inventory.")
        else:
            inventory[item] -= quantity
            print(f"{quantity} {item}(s) removed from the inventory.")
    else:
        print(f"{item} not found in the inventory.")
        
# Function to update the quantity of an item in the inventory
def update_item():
    item = input("Enter the item name to update: ")
    if item in inventory:
        quantity = int(input("Enter the new quantity: "))
        inventory[item] = quantity
        print(f"{item} updated to {quantity}.")
    else:
        print(f"{item} not found in the inventory.")
        
# Main function to run the inventory management system
def main():
    while True:
        print("\nInventory Management System")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Item")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            display_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            update_item()
        elif choice == '5':
            print("Exiting the Inventory Management System.")
            break
        else:
            print("Invalid option selected. Please try again.")
            
# Run the main function
main()
    