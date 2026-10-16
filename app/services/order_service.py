from app.majol.order import Order
from app.majol.order_item import Order_item
from app.services.customer_service import Customer_Service
from app.services.product_service import Product_Service
from app.repositories.order_repository import Order_Repository
from app.repositories.order_item_repository import Order_Item_Repository

class Order_Service():
    def __init__(self , customer_servicc , product_servicec,
                 order_repo_a = "order.json",order_rep_item_a ="order_item.json",
                 produt_a = "product.json",customer_ad ="customer.json" , ):
        self.order_data = []
        self.order_item_id_counter = []
        self.customer_service = customer_servicc 
        self.product_service = product_servicec 
        self.order_repository = Order_Repository()
        self.order_item_repository = Order_Item_Repository()
        self.add_order_from_repository()
        self.get_order_item_from_repository()

    def add_order_from_repository(self):
        data = self.order_repository.get_order_json()
        for i , j in data.items():
            self.load_orders_from_json( int(i) , j["customer_id"] , j["date"], j["status"])

    def load_orders_from_json(self , order_id , customer_id , date , status):
        new_order_load = Order(order_id ,customer_id ,date, status)
        self.order_data.append(new_order_load)

    def add_order(self  ,customer_id, date , status , flag2=-1):
        obj = self.customer_service.find_customer_by_id(customer_id)

        if obj ==0:
            return ",,,this customer id not exist!"
        if flag2==-1:
            self.add_order_from_repository()
            flag3 = 1
            for i in self.order_data:
                if i.order_id== flag3:
                    flag3+=1
                else:
                    flag2 = flag3
                    break
            if flag2 ==-1:
                flag2 = len(self.order_data)+1
                    
        obj2 = Order(flag2,customer_id, date , status)
        self.order_data.append(obj2)
        type_json = obj2.merge_dic_for_json_type()
        self.order_repository.add_order(str(flag2) , type_json)
        return 0
    def get_order_item_from_repository(self):
        data = self.order_item_repository.get_order_items_json()
        for i , j in data.items():

            for k in self.order_data:
                if int(j["order_id"]) == k.order_id:
                    new_data = self.load_order_item_from_repository(int(i) ,j["order_id"], j["product_id"], j["quantity"],j["price"])
                    k.add_items(new_data)
                    self.order_item_id_counter.append(int(i))
    def load_order_item_from_repository(self ,order_item_id,order_id,product_id,quantity,price):
        new_item_order = Order_item(order_item_id,order_id,product_id,quantity,price)
        return new_item_order

    def add_order_item(self , order_id   , product_id , quantity, flag2=-1 ):
        order_obj = self.find_order_by_id(order_id)

        if order_obj ==0:
            return "this order id not exist!"
        
        product_obj = self.product_service.find_product_by_id(product_id)
        if product_obj == 0:
            return "this product id not exist!"
        
        is_valid= product_obj.validation_of_quantity_befor_sold(quantity)
        if is_valid == False:
            return "more than exist!"
        elif is_valid== True:
            if flag2==-1:
                self.add_order_from_repository()
                flag3 = 1
                for i in self.order_item_id_counter:
                    if i== flag3:
                        flag3+=1
                    else:
                        flag2 = flag3
                        break
                if flag2 ==-1:
                    flag2 = len(self.order_item_id_counter)+1
            new_item = Order_item(flag2 ,order_id , product_id , quantity , product_obj.price)
            order_obj.add_items(new_item)
            product_obj.quantity -=quantity
            self.product_service.change_quantity(product_id, product_obj.quantity)
            self.order_item_repository.add_order_item(str(flag2) , new_item.merge_dict_for_json_type())

    def remove_order(self, id):
        obj = self.find_order_by_id(id)
        if obj ==0:
            return "this order id not exist!"
        else:
            for i in obj.items:
                self.order_item_repository.delete_order_item(i.order_item_id)
            self.order_data.remove(obj)
            self.order_repository.delete_order(id)

    def remove_order_item(self, order_id , order_item_id):
        obj = self.find_order_item(order_id , order_item_id)
        if obj =="this order item not exist":
            return "this order item not exist"
        if obj =="this order id not exist!":
            return "this order id not exist!"
        obj2 = self.find_order_by_id(order_id)
        obj2.total_price -= obj.total_price_this_order_items()
        obj3 =self.product_service.find_product_by_id(obj.product_id)
        new_quantity = obj3.quantity + (obj.quantity)
        self.product_service.change_quantity(obj.product_id ,new_quantity)
        self.order_item_repository.delete_order_item(order_item_id)
        obj2.items.remove(obj)
        
    def find_order_item(self , order_id , order_item_id):

        obj = self.find_order_by_id(order_id)
        if obj ==0:
            return "this order id not exist!"
        
        order_item = obj.find_item_by_id(order_item_id)

        if order_item == 0:
            return "this order item not exist"
        return order_item
        
    def find_order_by_id(self , id):
        for i in self.order_data:
            if i.order_id== id:
                return i
        return 0