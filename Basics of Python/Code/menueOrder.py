# Restaurant Menu and Order System

menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
    "Fries": 100,
    "Coke": 50
}

# Show the menu
def show_menu():
    print("\n--- MENU ---")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")

# Take the customer's order
def take_order():
    order = {}
    for _ in range(5):  # Allow 5 items in one order
        item = input("\nEnter the item name: ").title()
        if item in menu:
            qty = int(input(f"Enter quantity for {item}: "))
            order[item] = order.get(item, 0) + qty
        else:
            print("Item not found in the menu.")
    return order

# Calculate the total bill
def calculate_total(order):
    total = 0
    for item, qty in order.items():
        total += menu[item] * qty
    return total

# Show the final order summary
def show_summary(order):
    print("\n--- ORDER SUMMARY ---")
    for item, qty in order.items():
        print(f"{item} x {qty} = ₹{menu[item] * qty}")
    total = calculate_total(order)
    print(f"Total Bill: ₹{total}")

# Update the menu using simulated switch-case
def update_menu():
    print("\n--- UPDATE MENU ---")
    print("1. Add new item")
    print("2. Change price of existing item")
    choice = int(input("Enter choice (1/2): "))

    if choice == 1:
        new_item = input("Enter new item name: ").title()
        price = int(input("Enter price: "))
        menu[new_item] = price
        print(f"{new_item} added with price ₹{price}")
    elif choice == 2:
        item = input("Enter item name to update: ").title()
        if item in menu:
            new_price = int(input("Enter new price: "))
            menu[item] = new_price
            print(f"Updated {item} price to ₹{new_price}")
        else:
            print("Item not found in menu.")
    else:
        print("Invalid choice.")

# Main program loop
while True:
    print("\n=== RESTAURANT ORDER SYSTEM ===")
    print("1. Show Menu")
    print("2. Take Order")
    print("3. Update Menu")
    print("4. Exit")
    
    option = int(input("Choose an option (1-4): "))
    
    if option == 1:
        show_menu()
    elif option == 2:
        show_menu()
        order = take_order()
        show_summary(order)
    elif option == 3:
        update_menu()
    elif option == 4:
        print("Thank you for using the Restaurant Order System. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
