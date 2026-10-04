

class Customer:
    def __init__(self, customer_id , name , last_name , phone  , email  = None):
        self.customer_id = customer_id
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"""customer id : {self.customer_id}\nname : {self.name}\n
        last name : {self.last_name}\nphone : {self.phone}
        \nemail : {self.email}"""