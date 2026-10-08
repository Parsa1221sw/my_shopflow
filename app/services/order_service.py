from app.majol.order import Order
from app.majol.order_item import Order_item
from app.services.customer_service import Customer_Service
from app.services.product_service import Product_Service


class Order_Service():
    order_data = []
    product_service = Product_Service("product_test.json")
    @classmethod
    def add_order(cls ,order_id ,customer_id, date , status):
        obj = Customer_Service.find_customer_by_id(customer_id)
        if obj ==0:
            return "this customer id not exist!"
        else:
            obj2 = Order(order_id ,customer_id, date , status)
            cls.order_data.append(obj2)


    @classmethod
    def add_order_item(cls , order_id  , order_item_id , product_id , quantity ):
        order_obj = cls.find_order_by_id(order_id)
        if order_obj ==0:
            return "this order id not exist!"
        
        product_obj = cls.product_service.find_product_by_id(product_id)
        if product_obj == 0:
            return "this product id not exist!"
        
        is_valid= product_obj.validation_of_quantity_befor_sold(quantity)
        if is_valid == False:
            return "more than exist!"
        elif is_valid== True:
            new_item = Order_item(order_item_id ,order_id , product_id , quantity , product_obj.price)
            order_obj.add_items(new_item)
            product_obj.quantity -=quantity
    @classmethod
    def remove_order(cls, id):
        obj = cls.find_order_by_id(id)
        if obj ==0:
            return "this order id not exist!"
        else:
            cls.order_data.remove(obj)
    @classmethod
    def find_order_item(cls , order_id , order_item_id):

        obj = cls.find_order_by_id(order_id)
        if obj ==0:
            return "this order id not exist!"
        
        order_item = obj.find_item_by_id(order_item_id)

        if order_item == 0:
            return "this order item not exist"
        return order_item
        
    @classmethod
    def find_order_by_id(cls , id):
        for i in cls.order_data:
            if i.order_id== id:
                return i
        return 0