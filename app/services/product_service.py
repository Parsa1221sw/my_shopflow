from app.majol.product import Product
from app.repositories.product_repository import Product_Repository

class Product_Service():
    
    def __init__(self , json_file_name = None):
        if json_file_name == None:
            self.product_repositoty = Product_Repository()
        else:
            self.product_repositoty = Product_Repository(json_file_name)
        self.products = []
        self.get_data_from_repository()
    def get_data_from_repository(self ):
        data = self.product_repositoty.get_product_json()
        for key , item in data.items():
            self.load_product(int(key) ,item["name"],item["category"],item["quantity"],item["price"],item["information"])

    def add_product(self,new_product_id,new_name,new_category,new_quantity,new_price,new_information):
        new_product = Product(new_product_id,new_name,new_category,new_quantity,new_price,new_information)
        self.products.append(new_product)
        data = new_product.merge_for_json_type()
        self.product_repositoty.add_product( new_product_id, data)

    def load_product(self,new_product_id,new_name,new_category,new_quantity,new_price,new_information):
        new_product = Product(new_product_id,new_name,new_category,new_quantity,new_price,new_information)
        self.products.append(new_product)
        

    def remove_product(self ,id):
        obj = self.find_product_by_id(id)
        if obj==0:
            return "this id not exist"
        self.products.remove(obj)
        self.product_repositoty.delete_product(id)

    def update_product(self, id, name= None , category= None , price = None, information = None):
        
        obj = self.find_product_by_id(id)
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

        self.product_repositoty.delete_product(id)
        data = obj.merge_for_json_type()
        self.product_repositoty.add_product(id ,data )

    def change_quantity(self , id , new_new_quantity):
        
        obj = self.find_product_by_id(id)
        if obj==0:
            return "this id not exist"
        obj.change_quantity(new_new_quantity)
        self.product_repositoty.delete_product(id)
        data = obj.merge_for_json_type()
        self.product_repositoty.add_product(id , data)

    def find_product_by_id(self , productid):
        for i in self.products:
            
            if i.product_id == productid:
                return i
        return 0