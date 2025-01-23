# CAFE MANAGEMENT SYSTEM:

# define the menu of restaurant
print("Welcome to Twadda Dhaba!\nHere's your Menu:")
menu = {
    'Sandwich': 100, 'Pizza': 200, 'Noodles': 130, 
    'Cheese pasta': 150, 'Masala Dosa': 120, 
    'Chole kulche': 170, 'Pav bhaji': 140, 'Manchurian': 90
}
for item, price in menu.items():
    print(f"'{item}': Rs {price}")

order_total = 0

while True:
    # while True loop allows the user to add as many items as they like until they type "exit"
    item = input("\nWhat would you like to order? (Type 'exit' to finish): ").strip()
    if item.lower() == 'exit':
        break
    if item in menu:
        order_total += menu[item]
        print(f"{item} added to your order. Total so far: Rs {order_total}")
    else:
        print(f"Sorry, {item} is not available. Please choose from the menu.")

print(f"\nYour final total is: Rs {order_total}.\nThank you for visiting!\n Please Visit Again!")