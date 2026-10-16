import app.cli.func as func



def order_menu(order_service):
    while(True):
        print()
        print("1.show orders\n2.add order\n3add order items\n0.close")
        number = func.try_or_exept_integer_all_menu(0,3)
        if number == 0:
            break
        elif number ==1:
            show_order(order_service)
        elif number ==2:
            add_order(order_service)
        elif number ==3:
            add_order_item(order_service)

def show_order(order_service):
    return 0

def add_order(order_service):
    while(True):
        customer_id = int(input("customer id : "))
        status = input("status : ")
        date = input("date : ")
        report = order_service.add_order(customer_id , date , status,flag2=-1)
        if report == 0:
            break
        else :
            print("this customer id not exist!! try aggen")

def add_order_item(order_service):
    while(True):
        order_id = int(input("order id : "))
        product_id = int(input("product id : "))
        quantity = int(input("quantity : "))
        report= order_service.add_order_item(order_id, product_id ,quantity)        
        if report == 0:
            break
        else:
            print("order id or prodcut id not exist")
            continue