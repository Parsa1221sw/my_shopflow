


class Order_item:
    def __init__(self, order_item_id , product , quantity , price ):
        self.order_item_id = order_item_id
        self.product = product
        self.item_quantity = quantity
        self.item_price = price

    def total_price_this_order_items(self):
        return self.item_price *self.item_quantity