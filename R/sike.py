class Order:
    def __init__(self):
        self.state = "new"
        self.items = []

    def add_item(self, item):
        if self.state == "new":
            self.items.append(item)
            print(f"Item '{item}' added to the order.")
        else:
            print("Cannot add items to a processed order.")

    def process_order(self):
        if self.state == "new":
            print("Processing order...")
            self.state = "processed"
            print("Order processed successfully.")
        else:
            print("Order has already been processed.")

    def cancel_order(self):
        if self.state == "new":
            print("Cancelling order...")
            self.state = "cancelled"
            print("Order cancelled successfully.")
        else:
            print("Cannot cancel an already processed order.")

# Example Usage:
order1 = Order()

order1.add_item("Product A")
order1.add_item("Product B")
order1.process_order()
order1.add_item("Product C")  # Output: Cannot add items to a processed order.
order1.cancel_order()
order1.cancel_order()  # Output: Cannot cancel an already processed order.
