# class Product:

#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#     def getPrice(self):
#         return f"Price of {self.quantity} {self.name} is {self.quantity * self.price}"
    
# laptop = Product("Laptop",1000,50)
# print(laptop.getPrice())
class OutOfStockError(Exception):
    """Custom exception for handling out-of-stock items."""

    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock."

# Sample Product Inventory
product_inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0,  # Out of stock
    "grapes": 3
}


def purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise OutOfStockError(item)
        else:
            print(f"Purchase successful: {quantity} {item}(s)")
            product_inventory[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory.")

# Testing the Custom Exception
try:
    purchase_item("apple", 3)  # Purchase successful
    purchase_item("orange", 1)  # Raises OutOfStockError
    purchase_item("watermelon", 1)  # Item not available
except OutOfStockError as e:
    print(e)  # Output: