from app.services.product_service import Product_Service
from app.majol.product import Product


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