import json
from pathlib import Path

class Product_Repository():

    def __init__(self , adress ="product.json" ):
        self.adress = adress

    def get_product_json(self):
        base_adress = Path(__file__).resolve().parents[2]
        adress = base_adress / "data" / self.adress
        with open (adress, "r") as file:
            data = json.load(file)
            return data

    def add_product(self, product_id,new_data):
        data = self.get_product_json()
        data[product_id] = new_data
        self.push_product_json(data)
    

    def push_product_json(self, data):
        base_adress = Path(__file__).resolve().parents[2]
        adress = base_adress / "data" / self.adress
        with open (adress, "w") as file:
            json.dump(data , file , indent= 4)


    def find_product_by_id(self, product_id):
        data = self.get_product_json()
        id = str(product_id)
        for i , j in data.items():
            if i == id:
                return  dict(j)
        return "this product not exist!"

    def delete_product(self , product_id):
        data = self.get_product_json()
        del data[str(product_id)]
        self.push_product_json(data)

