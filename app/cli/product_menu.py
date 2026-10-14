import app.cli.func as func
def product_menu(product_service):
    while(True):
        print()
        print("1.add product\n2.show product\n0.close")
        number = func.try_or_exept_integer_all_menu(0,2)
        if number ==1:
            add_product(product_service)
        elif number ==2:
            show_product(product_service)
        elif number ==0:
            break

def show_product(product_service):
    while(True):
        print()
        print("1.find product by id\n0.close")
        number = func.try_or_exept_integer_all_menu(0,1)
        if number ==0:
            break
        elif number ==1:
            print("enter prodcut id : ")
            num = func.try_or_exept_integer_all_menu(0)
            obj = product_service.find_product_by_id(num)
            while(True):
                print("name", obj.name)
                print("category", obj.category)
                print("quantity", obj.quantity)
                print("price", obj.price)
                print("information",obj.information)
                print()
                print("1.change product\n2.delete product\n0.close")
                nuum = func.try_or_exept_integer_all_menu(0,2)
                if nuum==0:
                    break
                elif nuum==2:
                    product_service.remove_product(num)
                    break
                elif nuum ==1:
                    while(True):
                        print("1.change name\n2.change category\n3.change quantity\n4.change price\n5.change information\n0.close")
                        flag = func.try_or_exept_integer_all_menu(0,5)
                        if flag==0 :
                            break
                        elif flag==1:
                            new_name = input("enter new name : ")
                            product_service.update_product(num , name = new_name)
                        elif flag==2:
                            new_category = input("enter new category")
                            product_service.update_product(num , category= new_category)
                        elif flag==3:
                            new_quantity = int(input("enter new quantity : "))
                            product_service.change_quantity(num , new_quantity)
                        elif flag==4:
                            new_price = int(input("enter new price"))
                            product_service.update_product(num ,price= new_price)
                        elif flag ==5:
                            new_information = input("enter new information : ")
                            product_service.update_product(num,information=new_information)



def add_product(product_service):
    name = input("name : ")
    category = input("category : ")
    quantity = int(input("quantity : "))
    price = int(input("price : "))
    information = input("information : ")
    product_service.add_product(new_name= name,new_category= category,new_quantity = quantity,new_price= price,new_information=information)
    