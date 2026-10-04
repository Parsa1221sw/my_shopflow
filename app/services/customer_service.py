from app.majol.customer import Customer



class Customer_Service():
    customers_data = []
    
    @classmethod
    def add_customer(cls, customer_id , name , last_name , phone  , email  = None):
        new_customer = Customer( customer_id , name , last_name , phone  , email)
        cls.customers_data.append(new_customer)

    @classmethod
    def remove_customer(cls , id):
        obj = cls.find_customer_by_id(id)
        if obj ==0 :
            return "this id not exist!"
        cls.customers_data.remove(obj)

    @classmethod
    def update_customer(cls , id ,name=None,last_name=None ,phone=None ,email=None ):
        obj = cls.find_customer_by_id(id)
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

    @classmethod
    def find_customer_by_id(cls , id):
        for i in cls.customers_data:
            if i.customer_id == id:
                return i
        return 0