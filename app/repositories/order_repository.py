import json
from pathlib import Path

class Order_Repository():
    def __init__(self , adress = "order.json"):
        self.adress = adress
        
    def get_order_json(self):
        base_adress = Path(__file__).resolve().parents[2]
        adress = base_adress / "data" / self.adress
        with open (adress, "r") as file:
            data = json.load(file)
            return data

    def add_order(self, order_id , new_data):
        data = self.get_order_json()
        data[order_id] = new_data
        self.push_order_json(data)

    def delete_order(self , order_id):
        data = self.get_order_json()
        del data[str(order_id)]
        self.push_order_json(data)

    def find_order_by_id(self , id):
        data=  self.get_order_json()
        id =str(id)
        for i , j in data.items():
           if i== id:
               return dict(j)
        return "this order not exist"

    def push_order_json(self, data):
        empty = []
        for i in data.keys():
            empty.append(int(i))
        empty.sort()
        new_data = {}
        for i in empty:
            new_data[str(i)] = data[str(i)]
        base_adress = Path(__file__).resolve().parents[2]
        adress = base_adress / "data" / self.adress
        with open (adress, "w") as file:
            json.dump(new_data, file , indent= 4)
    