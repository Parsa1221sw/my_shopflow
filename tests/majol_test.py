from app.majol.customer import Customer
from app.majol.product import Product
from app.majol.order import Order
from app.majol.order_item import Order_items

def test_customer_majol_class():
    customer1 = Customer(3, "parsa" , "fathollahi ", "0432342323")
    assert customer1.name == "parsa"
    assert customer1.email == None

def test_order_majol_class():
    order1 = Order(2,4,"just test" , 342)
    assert order1.total_price == 342
    assert order1.order_id == 2

def test_product_majol_class():
    product1 = Product(23, "laptop" , "just test" , 221 , 123 , "just test")
    assert product1.product_id == 23
    assert product1.quantity == 221