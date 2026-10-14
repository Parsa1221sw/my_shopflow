import app.cli.main_menu as real



def try_or_exept_integer_main_menu( first_number , last_number ):
    while(1):
        try:
            number = int(input())
            if not(number>= first_number and number <= last_number):
                raise ValueError("this number not exept pleas enter right!\n")     
            return number
        except ValueError as e:
            print(e)
            print()


def try_or_exept_integer_all_menu( first_number , last_number =float('inf')):
    while(1):
        try:
            number = int(input())
            if not(number>= first_number and number <= last_number):
                raise ValueError("this number not exept pleas enter right!\n")     
            return number
        except ValueError as e:
            print(e)
            print("enter")
            