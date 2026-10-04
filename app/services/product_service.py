from app.majol.product import Product


class Product_Service():
    products = []
    @classmethod
    def add_product(cls,new_product_id,new_name,new_category,new_quantity,new_price,new_information):
        new_product = Product(new_product_id,new_name,new_category,new_quantity,new_price,new_information)
        cls.products.append(new_product)

    @classmethod
    def remove_product(cls ,id):
        obj = cls.find_product_by_id(id)
        if obj==0:
            return "this id not exist"
        cls.products.remove(obj)
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