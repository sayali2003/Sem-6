import random

class OrderBot:
    def __init__(self):
        self.orders = {}

    def generate_order_number(self):
        return ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=8))

    def place_order(self, item):
        order_number = self.generate_order_number()
        self.orders[order_number] = {"item": item, "status": "Processing"}
        return order_number

    def track_order(self, order_number):
        if order_number in self.orders:
            return self.orders[order_number]["status"]
        else:
            return "Order not found."

# Sample usage
bot = OrderBot()

while True:
    print("1. Place Order")
    print("2. Track Order")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter item to order: ")
        order_number = bot.place_order(item)
        print(f"Order placed successfully. Your order number is: {order_number}")
    elif choice == '2':
        order_number = input("Enter your order number: ")
        status = bot.track_order(order_number)
        print(f"Order status: {status}")
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
