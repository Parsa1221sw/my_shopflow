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
    while(True):
        print("1.find order by id\n0.close\nchoose :")
        number = func.try_or_exept_integer_all_menu(0,1)
        obj = -1
        flag2=-1
        if number ==0:
            break
        elif number == 1:
            while(True):
                print("enter order id")
                id = func.try_or_exept_integer_all_menu(0)
                obj =order_service.find_order_by_id(id)
                if obj == 0:
                    print("this order id not exist")
                    continue
                else:
                    break
            print("\norder id :", obj.order_id)
            print("customer id :",obj.customer_id )
            print("date :", obj.date)
            print("status : ",obj.status)
            print()
            while(True):
                print("1.show order items\n2.delete order\n3.show total price\n0.close")
                flag = func.try_or_exept_integer_all_menu(0,3)
                if flag==0:
                    break
                elif flag ==2:
                    order_service.remove_order(obj.order_id)
                elif flag ==1:
                    for i in obj.items:
                        print("order_item_id :",i.order_item_id)
                        print("product id :",i.product_id)
                        print("quantity :",i.quantity)
                        print("price :",i.price)
                        print()

                    while(True):
                        print("1.delete order item\n0.close")
                        num = func.try_or_exept_integer_all_menu(0,1)
                        if num ==0:
                            break
                        elif num ==1:
                            while(True):
                                print("enter order item id to deleted.")
                                order_delete = func.try_or_exept_integer_all_menu(0)
                                flag2= order_service.find_order_item(obj.order_id, order_delete)
                                if flag2=="this order item not exist":
                                    print (flag2)
                                    continue
                                order_service.remove_order_item(flag2.order_id ,flag2.order_item_id )
                                break
                elif flag==3:
                    print("total price : ", obj.total_price)

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
        print("1.add order item\n0.close")
        number = func.try_or_exept_integer_all_menu(0,1)
        if number ==0:
            break
        order_id = int(input("order id : "))
        product_id = int(input("product id : "))
        quantity = int(input("quantity : "))
        report= order_service.add_order_item(order_id, product_id ,quantity)        
        if report == 0:
            break
        else:
            print("pleas try aggen product id or order id not exist!!")
            continue