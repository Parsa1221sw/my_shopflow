import app.cli.func as func
from app.cli.product_menu import product_menu
from app.cli.customer_menu import customer_menu
from app.services.order_service import Order_Service
from app.services.product_service import Product_Service
from app.services.customer_service import Customer_Service
from app.cli.order_menu import order_menu
def start_program():
    customer_service = Customer_Service()
    product_service = Product_Service()
    order_service = Order_Service(customer_servicc = customer_service , product_servicec = product_service)
    main_menu(customer_service , product_service ,order_service)
def main_menu(customer_service , product_service , order_service):
    while(1):
        print("shop flow\n")
        print("1.Order")
        print("2.Customer")
        print("3.Product")
        print("0.close")
        print("\nChose : ")
        number = func.try_or_exept_integer_main_menu(0 , 3)
        if number ==1:
            order_menu(order_service)
        elif number ==2:
            customer_menu(customer_service , order_service)
        elif number ==3 :
            product_menu(product_service)    
        elif number ==0:
            break
