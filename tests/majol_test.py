from app.majol.customer import Customer
from app.majol.product import Product
from app.majol.order import Order
from app.majol.order_item import Order_item

def test_customer_majol_class():
    customer1 = Customer(3, "parsa" , "fathollahi ", "0432342323")
    assert customer1.name == "parsa"
    assert customer1.email == None
    assert "parsa" in str(customer1)

def test_order_majol_class():
    order1 = Order(2,4, "2020-01-01" , "active")
    assert order1.date == "2020-01-01"
    assert order1.order_id == 2

def test_product_majol_class():
    product1 = Product(23, "laptop" , "just test" , 221 , 123 , "just test")
    assert product1.price == 123
    product1.change_price(33)
    assert product1.product_id == 23
    assert product1.quantity == 221
    assert product1.price == 33

def test_order_item_majol_class():
    product1 = Product(23, "laptop" , "just test" , 221 , 123 , "just test")
    order_item1 = Order_item(23,product1 , 12 , 123)
    assert product1.validation_of_quantity_befor_sold(12) == True
    assert order_item1.total_price_this_order_items()== (12*123)
    assert order_item1.product.name== "laptop"
    assert order_item1.item_price ==123