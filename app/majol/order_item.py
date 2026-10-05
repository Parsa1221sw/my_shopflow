


class Order_item:
    def __init__(self, order_item_id  , order_id , product_id , quantity , price ):
        self.order_item_id = order_item_id
        self.product_id = product_id
        self.item_quantity = quantity
        self.item_price = price
        self.order_id = order_id

    def total_price_this_order_items(self):
        return self.item_price *self.item_quantity
    