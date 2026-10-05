from app.majol.product import Product
from app.repositories.product_repository import Product_Repository

class Product_Service():
    products = []
    product_repositoty = Product_Repository()

    @classmethod
    def get_data_from_repository(cls):
        data = cls.product_repositoty.get_product_json()
        for key , item in data:
            cls.load_product(key ,item["name"],item["category"],item["quantity"],item["price"],item["information"])

    @classmethod
    def add_product(cls,new_product_id,new_name,new_category,new_quantity,new_price,new_information):
        new_product = Product(new_product_id,new_name,new_category,new_quantity,new_price,new_information)
        cls.products.append(new_product)
        data = new_product.merge_for_json_type()
        cls.product_repositoty.add_product( new_product_id,data)

    @classmethod
    def load_product(cls,new_product_id,new_name,new_category,new_quantity,new_price,new_information):
        new_product = Product(new_product_id,new_name,new_category,new_quantity,new_price,new_information)
        cls.products.append(new_product)
        

    @classmethod
    def remove_product(cls ,id):
        obj = cls.find_product_by_id(id)
        if obj==0:
            return "this id not exist"
        cls.products.remove(obj)
        cls.product_repositoty.delete_product(id)
    @classmethod
    def update_product(cls , id, name= None , category= None , price = None, information = None):
        
        obj = cls.find_product_by_id(id)
        if obj==0:
            return "this id not exist"
        
        if name == None:
            pass
        else:
            obj.name = name
        if category == None:
            pass
        else:
            obj.category = category
        if price ==None:
            pass
        else:
            obj.change_price(price)
        if information == None:
            pass
        else:
            obj.information = information
    @classmethod
    def change_quantity(cls , id , new_new_quantity):
        
        obj = cls.find_product_by_id(id)
        if obj==0:
            return "this id not exist"
        obj.change_quantity(new_new_quantity)

    @classmethod
    def find_product_by_id(cls , productid):
        for i in cls.products:
            
            if i.product_id == productid:
                return i
        return 0