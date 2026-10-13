import json
from pathlib import Path

class Customer_Repository():
    def __init__(self , adress = "customer.json"):
        self.adress = adress

    def get_order_json(self):
        base_adress = Path(__file__).resolve().parents[2]
        adress = base_adress / "data" / self.adress
        with open (adress, "r") as file:
            data = json.load(file)
            return data

    def push_order_json(self, data):
        base_adress = Path(__file__).resolve().parents[2]
        adress = base_adress / "data" / self.adress
        with open (adress, "w") as file:
            json.dump(data , file , indent= 4)

    def add_customer(self , id , new_data):
        data = self.get_order_json()
        data[id] = new_data
        self.push_order_json(data)

    def delete_customer(self, id):
        data = self.get_order_json()
        del data[str(id)]
        self.push_order_json(data)

    def find_customer_by_id(self, id):
        data = self.get_order_json()
        id = str(id)
        for i, j in data.items():
            if i == id:
                return dict(j)
        return "this customer id not exist!"
        