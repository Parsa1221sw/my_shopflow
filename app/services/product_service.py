from app.majol.product import Product
from app.repositories.product_repository import Product_Repository

class Product_Service():
    
    def __init__(self , json_file_name = "product.json"):
        self.product_repositoty = Product_Repository(json_file_name)
        self.products = []
        self.get_data_from_repository()



    def get_data_from_repository(self ):
        self.products = []
        data = self.product_repositoty.get_product_json()
        for key , item in data.items():
            self.load_product(int(key) ,item["name"],item["category"],item["quantity"],item["price"],item["information"])

    def add_product(self,new_name,new_category,new_quantity,new_price,new_information, flag2 =-1):
        if flag2==-1:
            self.get_data_from_repository()
            flag3 = 1
            for i in self.products:
                if i.product_id == flag3:
                    flag3+=1
                else:
                    flag2 = flag3
                    break
            if flag2 ==-1:
                flag2 = len(self.products)+1


 
        new_product = Product(flag2,new_name,new_category,new_quantity,new_price,new_information)
        self.products.append(new_product)
        data = new_product.merge_for_json_type()
        self.product_repositoty.add_product( str(flag2), data)

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
        n_name = obj.name
        n_category = obj.category
        n_quantity = obj.quantity
        n_price = obj.price
        n_information = obj.information
        self.products.remove(obj)
        self.add_product(new_name= n_name,new_category= n_category,new_quantity = n_quantity,new_price= n_price,new_information=n_information,flag2=id)

    def change_quantity(self , id , new_new_quantity):
        
        obj = self.find_product_by_id(id)
        if obj==0:
            return "this id not exist"
        obj.change_quantity(new_new_quantity)
        self.product_repositoty.delete_product(id)
        data = obj.merge_for_json_type()
        n_name = obj.name
        n_category = obj.category
        n_quantity = obj.quantity
        n_price = obj.price
        n_information = obj.information
        self.products.remove(obj)
        self.add_product(new_name= n_name,new_category= n_category,new_quantity = n_quantity,new_price= n_price,new_information=n_information,flag2=id)
    def find_product_by_id(self , productid):
        for i in self.products:
            
            if i.product_id == productid:
                return i
        return 0