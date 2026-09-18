from catalog import catalog  # import catalog dictionary

# global variable 
cart = []

# Helper Function
def header(text):
    print("__________________________")
    print(text)
    print("__________________________")

def menu():
    print("Menu")
    print(" 1.- View Catalog")
    print(" 2.- Search Product")
    print(" 3.- View Cart")
    # Add more features
    print(" Q.- Quit")

# Catalog and Cart Functions

def print_catalog():
    header("- Our Catalog -")
    for prod in catalog:         # Ljust means left justify. So 15 spaces to the right
        print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}')

    answer = input("Type ID to add product (N to close): ")
    if answer.lower() == "n":  #.lower forces everything to be lowercase
        return
    else:
        add_product_to_cart(answer)

def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id): # matching what user adds to dictionary "id"
            found = True
            cart.append(prod) # add product to the cart
            print(f'{prod["title"]} added to your cart.')
            break # stop after finding and adding product

    if not found:
        print("**ERROR: Invalid ID")


def search_product():
    text = input("Search Title of Product: ").lower()
    found = False
    for prod in catalog:
        if text in prod["title"].lower():
            found = True
            print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}')
            choice = input("Do you want to add this item to your cart? (y/n)")
            if choice.lower() == "y": # if "y" add product to cart
                add_product_to_cart(prod["id"])
            break  # back to menu
    if not found:
        print("Sorry, this item dosen't exist.")

def view_cart():
    header("Your Cart")
    if not cart: # checking if empty first
        print("Your cart is empty.")
    else:
        for prod in cart:
            print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}')
            cart_total()

"""
1. Create a function calld cart_total():
2. create a variable total
3. loop through the cart items
4. Add the total of all product["price"]
5. print the total
"""
def cart_total():
    total = 0
    for prod in cart:
        total += prod["price"]
        print(f"Total: ${total}")
"""
1. Create a function called clear_cart():
2. clear the cart
3. print a message saying "Your cart has been cleared."
"""


# Main Program Loop
option = ""
while option != "q" and option != "Q":
    header("Welcome to Store")
    menu()

    option = input("Choose an option: ")

    if option == "1":
        print_catalog()
    elif option == "2":
        search_product()
    elif option == "3":
        view_cart()
    elif option == "q" or option == "Q":
        print("Good Bye!")
        break
    else: 
        print("**ERROR: invalid option")
















