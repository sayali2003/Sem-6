import random
import nltk
from nltk.tokenize import word_tokenize

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

    def process_input(self, user_input):
        tokens = word_tokenize(user_input.lower())
        if "place" in tokens and "order" in tokens:
            item_index = tokens.index("order") + 1
            if "for" in tokens and item_index < len(tokens) - 1:
                item_index = tokens.index("for") + 1
            item = " ".join(tokens[item_index:])
            order_number = self.place_order(item)
            return f"Order placed successfully. Your order number is: {order_number}"
        elif "track" in tokens and "order" in tokens:
            for token in tokens:
                if token.isdigit():
                    order_number = token
                    status = self.track_order(order_number)
                    return f"Order status: {status}"
                else:
                    return "Order number not found."
        else:
            return "Sorry, I didn't understand that. Please try again."

# Sample usage
bot = OrderBot()
print("Hello! How can I assist you today?")

while True:
    user_input = input("You: ")
    response = bot.process_input(user_input)
    print("Bot:", response)
