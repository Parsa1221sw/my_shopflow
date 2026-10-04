from app.services.product_service import Product_Service
from app.majol.product import Product
from app.services.customer_service import Customer_Service
from app.majol.customer import Customer

def test_product_service_class():
    service1 = Product_Service()
    service1.add_product(23, "laptop" , "just test" , 221 , 123 , "just test")
    service1.add_product(13, "mobile" , "just test" , 100 , 200 , "just test")
    service1.remove_product(13)

    obj = service1.find_product_by_id(13)
    assert obj == 0

    service1.update_product(23,name ="ali" ,price = 315  )
    obj2 = service1.find_product_by_id(23)
    assert obj2.price == 315
    assert obj2.quantity == 221
    assert obj2.information == "just test"
    assert obj2.product_id == 23

    service1.change_quantity(23, 500)
    assert obj2.quantity ==500
    obj3 = service1.remove_product(100)
    assert obj3 == "this id not exist"
    obj4 = service1.update_product(120 , name = "mohamad")
    assert obj4 == "this id not exist"
    obj5 = service1.change_quantity(32, 5200)
    assert obj5 == "this id not exist"

def test_customer_service_class():
    service1 = Customer_Service
    service1.add_customer(3, "parsa" , "fathollahi ", "0432342323")
    service1.add_customer(32, "ali" , "mohamadi", "39433040", "ali@gmail.com")
    obj1 = service1.find_customer_by_id(3)
    assert obj1.name == "parsa"
    obj2 = service1.find_customer_by_id(1)
    assert obj2 ==0
    service1.remove_customer(3)
    assert obj1 not in service1.customers_data
    obj3 = service1.remove_customer(1)
    assert obj3 =="this id not exist!"
    obj4 = service1.find_customer_by_id(32)
    obj4.name = "sara"
    obj4.email = "sara@gmail.com"
    assert obj4.name == "sara"
    assert obj4.email == "sara@gmail.com"
    service1.update_customer(32 , phone = "0983223232" , last_name = "vali zade")
    assert obj4.phone == "0983223232"
    assert obj4.last_name == "vali zade"
    assert obj4.name == "sara"
    obj5=service1.update_customer(122, name = "aliiii")
    assert obj5 == "this id not exist!"