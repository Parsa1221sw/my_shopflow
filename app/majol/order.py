


class Order:
    def __init__(self, order_id ,customer_id, date , status ):
        self.order_id = order_id
        self.customer_id = customer_id
        self.date = date
        self.total_price = 0
        self.status = status
        self.items = []

    def add_items(self, new_item):
        self.items.append(new_item)
        self.total_price += new_item.total_price_this_order_items()
        
    def find_item_by_id(self, id):
        for i in self.items:
            if i.order_item_id==id:
                return i
        return 0