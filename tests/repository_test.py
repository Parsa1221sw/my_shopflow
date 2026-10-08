from app.services.product_service import Product_Service
from pathlib import Path
import json
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