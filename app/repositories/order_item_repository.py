import json
from pathlib import Path


class Order_Item_Repository():
    def __init__(self , adress = "order_item.json"):
        self.adress = adress

    def get_order_items_json(self):
        base_adress = Path(__file__).resolve().parents[2]
        adress = base_adress / "data" / self.adress
        with open (adress, "r") as file:
            data = json.load(file)
            return data

    def add_order_item(self ,  new_order_item_id , new_data):
        data = self.get_order_items_json()
        data[new_order_item_id] = new_data
        self.push_order_item_json(data)

    def delete_order_item(self , id):
        data = self.get_order_items_json()
        del data[str(id)]
        self.push_order_item_json(data)

    def find_order_item_by_id(self , id):
        data = self.get_order_items_json()
        id = str(id)
        for i , j in data.items():
            if i == id:
                return dict(j)
        return "this order items id not exist!"
    
    def push_order_item_json(self, data):
        base_adress = Path(__file__).resolve().parents[2]
        adress = base_adress / "data" / self.adress
        with open (adress, "w") as file:
            json.dump(data , file , indent= 4)
    