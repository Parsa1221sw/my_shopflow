import app.cli.func as func
def customer_menu(customer_service , order_service):
    while(1):
        print()
        print("1.add customer")
        print("2.show customer")
        print("0.close")
        number = func.try_or_exept_integer_all_menu(0,2)
        if number ==1:
            add_customer(customer_service)

        elif number ==2:
            show_customer(customer_service)
        elif number ==0:
            return 0
def show_customer(customer_service):
    while(1):
        print()
        print("1.find customer by id")
        print("0.close")
        print("enter : ")   
        number = func.try_or_exept_integer_all_menu(0,1)
        if number ==0:
            return 0
        elif number ==1:
            print("pleas enter customer id :")
            num = func.try_or_exept_integer_all_menu(1, )
            obj = customer_service.find_customer_by_id(num)
            if obj == 0:
                print("this id not exist!!")
                continue
            else:
                print("custome id :",obj.customer_id)
                print("name :", obj.name)
                print("last name :",obj.last_name)
                print("phone :",obj.phone)
                print("email :",obj.email)
                print()
                print("1.change\n0.exit\nenter : ")
                flag = func.try_or_exept_integer_all_menu(0,1)
                if flag ==0:
                    continue
                else:
                    while(1):
                        print("1.change name\n2.change last name\n3.change phone\n4.change email\n0.close")
                        flag2 = func.try_or_exept_integer_all_menu(0,4)
                        if flag2==1:
                            namee = input("enter new name : ")
                            customer_service.update_customer(num , name = namee)
                        elif flag2 ==2:
                            last_namee = input("enter new last name : ")
                            customer_service.update_customer(num , last_name = last_namee)
                        elif flag2 ==3:
                            phonee = input("enter new phone :")
                            customer_service.update_customer(num , phone = phonee)
                        elif flag2==4:
                            emaile = input("enter new email : ")
                            customer_service.update_customer(num , email  = emaile)
                        elif flag2==0:
                            break
        
def add_customer(customer_service):
    name = input("name : ")
    last_name = input("last name : ")
    phone = input("phone : ") 
    email = input("email(if you want dont needed) : ") or None
    customer_service.add_customer(name , last_name, phone , email)
