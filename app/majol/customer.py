

class Customer:
    def __init__(self, customer_id , name , last_name , phone , email  = None):
        self.customer_id = customer_id
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        