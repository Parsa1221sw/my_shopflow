from app.services.product_service import Product_Service
from pathlib import Path
from app.services.customer_service import Customer_Service
from app.services.order_service import Order_Service
import json
def test_customer_service_class2():
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


def test_repository_order_repository_class():
    creat_json_product("order_test.json",file_test_order_json)
    creat_json_product("order_item_test.json", file_test_order_item_json)
    service = Order_Service("order_test.json","order_item_test.json", "product_test.json")
    obj = service.find_order_by_id(1)
    obj3 =service.find_order_by_id(2)
    assert obj3.customer_id ==111
    assert obj.customer_id == 3
    assert obj.status == "active"
    assert obj.total_price == 760
    assert len(obj.items) ==2
    obj2 = obj.find_item_by_id(1)
    assert obj2.quantity == 3
    obj4 = service.add_order(3 , 12 , "2026-01-01" , "active")
    assert obj4=="this customer id not exist!"
    obj4 = service.add_order(3 , 32 , "2026-11-21" , "active")
    obj5 = service.find_order_by_id(3)
    assert obj5.customer_id == 32
    obj6 = service.order_repository.find_order_by_id(3)
    assert obj6["date"] == "2026-11-21"
    service.add_order_item(3 , 3 , 12 , 4 )
    obj6 = service.find_order_by_id(3)
    obj7 = obj6.find_item_by_id(3)
    assert obj7.price == 100
    assert obj7.quantity == 4
    service.remove_order(2)
    obj8 = service.find_order_by_id(2)
    assert obj8 == 0
    obj9 = service.order_repository.find_order_by_id(2)
    assert obj9 == "this order not exist"
    service.remove_order_item(1, 1)
    obj10 = obj.find_item_by_id(1)
    assert obj10 == 0 
    obj11 = service.order_item_repository.find_order_item_by_id(1)
    assert obj11 == "this order items id not exist!"
    service.remove_order(3)
    obj12 = service.find_order_by_id(3)
    assert obj12 ==0

def test_repository_product_repository_class():
    creat_json_product("product_test.json" , file_test_product_json)
    service = Product_Service("product_test.json")
    flag =0
    for i in service.products:
        flag+=1
    assert flag ==2
    obj1 =service.find_product_by_id(3)
    assert obj1.name == "air pod"
    assert obj1.quantity == 120
    service.add_product(12 , "parsa" , "heoman" , 122 , 100 , "test")
    obj2 = service.find_product_by_id(12)
    assert obj2.category == "heoman" 
    assert obj2.price == 100
    obj3_items=service.product_repositoty.find_product_by_id(12)
    assert obj3_items["name"] == "parsa"
    assert obj3_items["information"] == "test"
    obj4 =service.remove_product(111)
    assert obj4 =="this id not exist"
    service.remove_product(23)
    obj5 = service.find_product_by_id(23)
    assert obj5 == 0
    obj6 = service.product_repositoty.find_product_by_id(23)
    assert obj6 == "this product not exist!"
    service.update_product(3 , name = "laptop")
    assert obj1.name == "laptop"
    assert obj1.quantity == 120
    obj7 = service.product_repositoty.find_product_by_id(3)
    assert obj7["name"] == "laptop"
    service.change_quantity(3, 200)
    assert obj1.quantity == 200



def creat_json_product(json_adress , file_to_set):
    base_adress = Path(__file__).resolve().parents[1]
    adress = base_adress / "data" / json_adress
    with open (adress, "w") as file:
        json.dump( file_to_set, file , indent= 4)

file_test_product_json = {
    "3": {
        "name": "air pod",
        "category": "tecknologia",
        "quantity": 120,
        "price": 99.99,
        "information": "color : wite  , nois canceling"
    }
    ,
    "23": {
        "name": "ali",
        "category": "just test",
        "quantity": 500,
        "price": 315,
        "information": "just test"
    }
}    

file_test_order_json ={
    "1" :{
        "customer_id": 3,
        "date" : "2020-01-21",
        "status" : "active"
    },
    "2" :{
        "customer_id": 111,
        "date" : "2026-01-21",
        "status" : "not active"
    }

}
file_test_order_item_json = {
    "1":
    {
        "order_id": 1,
        "product_id" : 12,
        "quantity" : 3,
        "price" : 120
    },
    "2":
    {
        "order_id": 1,
        "product_id" : 3,
        "quantity" : 4,
        "price" : 100
    }

}