"""Assignment 9: Product Inventory Management

A shopkeeper wants to manage the stock of a product.

Create a class Product with the following attributes:

Product ID

Product name

Price

Available quantity

Create the following methods:

add_stock() – Increase the available quantity.

sell_product() – Decrease the available quantity.

calculate_stock_value() – Calculate price × available quantity.

display_product() – Display product and stock details.

Sample operations:

Product Name: Laptop
Price: 45000
Initial Quantity: 10
Add Stock: 5
Sell Product: 3

Expected result:

Available Quantity: 12
Total Stock Value: 540000"""

class Product:
    def __init__(self,price,quantity,add,sell):
        self.price = price
        self.quantity = quantity
        self.add = add
        self.sell = sell

    def add_stock(self):
        self.quantity = self.quantity + self.add
        return self.quantity

    def sell_product(self):
        self.quantity = self.add_stock() - self.sell
        return self.quantity

    def calculate_stock_value(self):
        return self.sell_product()*self.price

    def display_product(self):
        return self.calculate_stock_value()

name = input("Enter Product Name: ")
price = int(input("Enter Price: "))
quantity = int(input("Enter Initial Quantity: "))
add = int(input("Enter Add Stock: "))
sell = int(input("Enter Sell Product: "))

name = Product(price,quantity,add,sell)
print()
print("Available Quantity:",name.sell_product())
print("Total Stock Value:",name.display_product())