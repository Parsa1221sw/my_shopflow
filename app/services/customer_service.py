from app.majol.customer import Customer
from app.repositories.customer_repository import Customer_Repository


class Customer_Service():

    def __init__(self , adress_data = "customer.json"):
        self.customer_repository = Customer_Repository(adress_data)
        self.customers_data = []
        self.add_customers_from_repository()

    def add_customers_from_repository(self):
        data = self.customer_repository.get_order_json()
        for i , k in data.items():
            self.load_customer_repository_into_list(int(i) , k["name"],k["last_name"],k["phone"],k["email"])

    def load_customer_repository_into_list(self ,customer_id , name , last_name , phone , email):
        new_customer = Customer(customer_id , name, last_name , phone ,email)
        self.customers_data.append(new_customer)

    def add_customer(self , name , last_name , phone  , email  = None):
        customer_id = len(self.customers_data)+1
        new_customer = Customer( customer_id , name , last_name , phone  , email)
        self.customers_data.append(new_customer)
        self.customer_repository.add_customer( customer_id, new_customer.merge_for_repository())

    def remove_customer(self , id):
        obj = self.find_customer_by_id(id)
        if obj ==0 :
            return "this id not exist!"
        self.customers_data.remove(obj)
        self.customer_repository.delete_customer(id)

    def update_customer(self , id ,name=None,last_name=None ,phone=None ,email=None ):
        obj = self.find_customer_by_id(id)
        if obj ==0 :
            return "this id not exist!"
        if name ==None:
            pass
        else:
            obj.name = name
        if last_name ==None:
            pass
        else:
            obj.last_name = last_name
        if phone ==None:
            pass
        else:
            obj.phone = phone
        if email ==None:
            pass
        else:
            obj.email = email 
        self.customer_repository.delete_customer(id)
        self.customer_repository.add_customer(id, obj.merge_for_repository())      

    def find_customer_by_id(self, id):
        for i in self.customers_data:
            if i.customer_id == id:
                return i
        return 0