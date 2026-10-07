

class Product:
    def __init__(self , product_id , name , category , quantity , price  , information):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.information = information

    def change_price(self, new_price):
        if new_price <=0 :
            raise ValueError ("price can not be negetive!!")
        self.price = new_price
    def change_quantity(self, new_quantity):
        if new_quantity <0:
            raise ValueError("quantity can not be negetive!!")
        self.quantity = new_quantity
    def validation_of_quantity_befor_sold(self, number_of_order):
        if number_of_order> self.quantity:
            return False
        else: 
            return True

    def __str__(self):
        return f"""product id : {self.product_id}\nname : {self.name}\n
          category : {self.category}\nquantity : {self.quantity}\n price : {self.price}
          \ninformation : {self.information}"""
    def merge_for_json_type(self):
        data = {
            "name" : self.name , 
            "category" : self.category,
            "quantity" : self.quantity,
            "price" : self.price,
            "information" : self.information
        }
        return data