from app.services.product_service import Product_Service
from app.majol.product import Product
from app.services.customer_service import Customer_Service
from app.majol.customer import Customer
from app.services.order_service import Order_Service
from app.majol.order import Order

def test_product_service_class():
    service1 = Product_Service("product_test.json")
    service1.add_product(22, "ps5" , "just test" , 120,500 , "just test")    
    service1.add_product(23, "laptop" , "just test" , 100 , 123 , "just test")
    service1.add_product(13, "mobile" , "just test" , 100 , 200 , "just test")
    service1.remove_product(13)

    obj = service1.find_product_by_id(13)
    assert obj == 0

    service1.update_product(23,name ="ali" ,price = 315  )
    obj2 = service1.find_product_by_id(23)
    assert obj2.price == 315
    assert obj2.quantity == 100
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

    service1 = Customer_Service()
    service1.add_customer(3, "parsa" , "fathollahi ", "0432342323")
    service1.add_customer(111, "parsa" , "fathollahi ", "0432342323")
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

def test_order_service_class():
    service = Order_Service()
    service.add_order(12 , 32 ,"2026-01-01", "active" )
    service.add_order(13 , 111 ,"2026-05-21", "active" )
    obj1 = service.find_order_by_id(12)
    assert obj1 != 0
    assert obj1.order_id == 12
    assert obj1.status == "active"
    obj2 = service.add_order(11 , 212 , "test" , "test2")
    assert obj2 == "this customer id not exist!"
    service.remove_order(12)
    obj3 = service.find_order_by_id(12)
    assert obj3 == 0
    obj4 =service.add_order_item(14 , 1 , 23 , 3 )
    assert obj4 == "this order id not exist!"
    obj5 =service.add_order_item(13, 1 , 20 , 3 )
    assert obj5 =="this product id not exist!"

    obj6 =service.add_order_item(13, 1 , 3, 520)
    assert obj6 =="more than exist!"
    service.add_order_item(13, 1 ,3 ,3)
    obj7 = service.product_service.find_product_by_id(3)
    assert obj7.quantity == 197
    obj8 = service.find_order_by_id(13)
    assert obj8.total_price == 3 * (99.99)
    service.add_order_item(13 , 2 , 22 ,2)
    obj9= service.find_order_by_id(13 )
    obj10 = obj9.find_item_by_id(1)
    obj11 = obj9.find_item_by_id(2)
    for i in obj9.items:
        print(
        "order_item_id =", i.order_item_id,
        "product_id =", i.product_id,
        "quantity =", i.item_quantity
        )
    assert obj11.product_id == 22
    assert obj10.item_quantity== 3

#service1.add_product(23, "laptop" , "just test" , 221 , 123 , "just test")
#service1.add_product(22, "ps5" , "just test" , 120,500 , "just test")    
