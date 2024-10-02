class Order:
    def __init__(self, address):
        self.address = address
        self.order_basket = []

    def add_item(self, item):
        self.order_basket.append(item)

    def format_note(self):
        items = ", ".join(self.order_basket)
        return f"Order for {self.address}: {items}"
    

order = Order("123 high St") 
order.add_item("Hat")
order.add_item("Tea")
print(order.format_note())