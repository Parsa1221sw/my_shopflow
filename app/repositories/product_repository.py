import json
from pathlib import Path

class Product_Repository():

    @classmethod
    def get_product_json(cls):
        base_adress = Path(__file__).resolve().parents[2]
        adress = base_adress / "data" / "product.json"
        with open (adress, "r") as file:
            data = json.load(file)
            return data
    @classmethod
    def add_product(cls, product_id,new_data):
        data = cls.get_product_json()
        data[product_id] = new_data
        cls.push_product_json(data)
    
    @classmethod
    def push_product_json(cls, data):
        base_adress = Path(__file__).resolve().parents[2]
        adress = base_adress / "data" / "product.json"
        with open (adress, "w") as file:
            json.dump(data , file , indent= 4)

    @classmethod
    def find_product_by_id(cls, product_id):
        data = cls.get_product_json()
        for i , j in data.items():
            if i == product_id:
                # for this part i will come back and make new string for this
                return i , j
    @classmethod
    def delete_product(cls , product_id):
        data = cls.get_product_json()
        del data[str(product_id)]
        cls.push_product_json(data)

