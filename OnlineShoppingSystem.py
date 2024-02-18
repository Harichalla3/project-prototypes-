class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def display_info(self):
        print(f"{self.name} - ${self.price} | Stock: {self.stock_quantity}")

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        if product.stock_quantity >= quantity:
            item = {"product": product, "quantity": quantity}
            self.items.append(item)
            product.stock_quantity -= quantity
            print(f"{quantity} {product.name}(s) added to the cart.")
        else:
            print(f"Insufficient stock for {product.name}.")

    def remove_product(self, product, quantity=1):
        for item in self.items:
            if item["product"] == product:
                if item["quantity"] >= quantity:
                    item["quantity"] -= quantity
                    product.stock_quantity += quantity
                    print(f"{quantity} {product.name} removed from the cart.")
                    if item["quantity"] == 0:
                        self.items.remove(item)
                else:
                    print(f"Quantity to remove exceeds the items in the cart.")
                return
        print(f"{product.name} not found in the cart.")

    def display_cart(self):
        if not self.items:
            print("Shopping cart is empty.")
            return

        print("Shopping Cart:")
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            print(f"{product.name} - {product.price} x {quantity}")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def checkout(self):
        total = self.calculate_total()
        print(f"Total amount: {total}")
        print("Checkout successful. Thank you for shopping!")
        self.items = []


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.shopping_cart = ShoppingCart()
        self.order_history = []

    def login(self, entered_password):
        return self.password == entered_password

    def add_to_cart(self, product, quantity=1):
        self.shopping_cart.add_product(product, quantity)

    def remove_from_cart(self, product, quantity=1):
        self.shopping_cart.remove_product(product, quantity)

    def view_cart(self):
        self.shopping_cart.display_cart()

    def checkout(self):
        self.shopping_cart.checkout()
        self.order_history.append(self.shopping_cart.items.copy())
        self.shopping_cart.items = []


# Example Usage:

# Create products
product1 = Product(1, "Laptop", 50000, 10)
product2 = Product(2, "Headphones", 500, 20)
product3 = Product(3, "Mouse", 550, 15)

# Create a user
user1 = User("Hari", "password123")

# Login
if user1.login("password123"):
    # Add products to the cart
    user1.add_to_cart(product1, 2)
    user1.add_to_cart(product2, 1)
    user1.add_to_cart(product3, 3)

    # View and remove from the cart
    user1.view_cart()
    user1.remove_from_cart(product2, 1)

    # View the updated cart
    user1.view_cart()

    # Checkout
    user1.checkout()

    # View order history
    print("Order History:")
    for order in user1.order_history:
        print(order)
else:
    print("Login failed.")
