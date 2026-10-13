


class Order_item:
    def __init__(self, order_item_id  , order_id , product_id , quantity , price ):
        self.order_item_id = order_item_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.order_id = order_id

    def total_price_this_order_items(self):
        return self.price *self.quantity

    def merge_dict_for_json_type(self):
        data = {"order_id":self.order_id , "product_id":self.product_id,
                "quantity": self.quantity,
                "price": self.price
                }
        return data