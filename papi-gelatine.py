# #student 99024233
# #papi.gelato

# def intro():
#     print('Welkom bij Papi Gelatine je mag alle smaken kiezen zolang het maar vanille ijs is.')

# def sorry():
#     print("Sorry dat begrijp ik niet")

# def groot():
#     print ('Sorry zulke grote bakken hebben we niet!')

# def ice_cream():
#     global cone_cup
#     global amount

#     amount = int (input ('Hoeveel bolletjes wilt u ?'))
#     if amount <= 3:
#         cone_cup = input (f'Wilt u deze {amount} bolletje(s) in een hoorntje of een bakje?')
#         if cone_cup == "bakje":
#                 choice = input (f'Hier is uw {cone_cup} met {amount} bolletje(s). Wilt u nog meer bestellen? (Y/N)')
#                 if choice.lower() == 'y':
#                     ice_cream()
#                 else:
#                     print ('Bedankt! en tot ziens !')
#                     exit

#         elif cone_cup == "hoorntje":
#             choice = input (f'Hier is uw {cone_cup} met {amount} bolletje(s). Wilt u nog meer bestellen? (Y/N)')
#             if choice.lower() == "y":
#                 ice_cream()
#             else:
#                 print ('Bedankt! en tot ziens !')
#                 exit
#         else:
#             sorry()
#             ice_cream()

#     elif amount <= 8:
#         print (f'Dan krijgt u van mij een bakje met {amount} bolletjes”')

#     elif amount > 8:
#         groot()
#         ice_cream()

# ice_cream()


#-----------------------------------Remake-------------------------------#

print('Welkom bij Papi Gelatine je mag alle smaken kiezen zolang het maar vanille ijs is')

# def stap_1():
#     repeat = True 
#     while repeat:
#         repeat = False
#         aantal = int(input("Hoeveel bolletjes wilt u ?"))
#         if aantal <= 3:
#             stap_2(aantal)
#         elif aantal > 3 and aantal <= 8:
#             print (f'Dan krijgt u van mij een bakje met {aantal}  bolletjes ')
#         elif aantal > 8:
#             print ('Sorry zulke grote bakken hebben we niet')
#             repeat = True
#         else:
#             repeat = True
#             print('Dat begrijp ik niet')

# def stap_2(aantal_2):
#     bol_bak = input(f'Wilt u deze {aantal_2} in A) een hoorntje of B) een bakje?')



# stap_1()
import time,os,sys
from tkinter.constants import W

def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()

A,B,C,D = False,False,False,False
business = False
private = False
taste_liter = 0

horn_price = 1.25
cup_price = 0.75
icecream_ball_price = 0.95
cone = 0
cup = 0
x = 1
total = 0
reciept = f'-------[Papi Gelatine]-------\n'

def icecream():
    choice = ""
    cone_cup = ""
    global cone,amount_icecream_balls,cup,topping_price,toppings,reciept,x

    clearScreen(0)
    print_slow("Welcome to Papi Gelatine\n")
    business_private = input("Hello, did you come to order for \n 1. Business\n 2. Private\n ")
    clearScreen(1)

    if business_private == "1":
        business_private = True
        amount_icecream_balls = int(input("How many ice cream balls would you like ?\n"))
        if amount_icecream_balls <= 8: 
            i = 1
            while i <= amount_icecream_balls:
                flavours = input ("What kind of flavour would you like for your" +str(i) + "\n 1.Strawberry\n 2.Chocolate\n 3. Vanille\n")
                clearScreen(1)
                if flavours >= 1 and flavours <= 3:
                    i+=1
                else:
                    print_slow("Sorry that is currently not available.")
                    i += 0
                    clearScreen(2)
                    icecream()
        else:
            print_slow("Sorry, we don't have any bigger cups.\n")
            clearScreen(1)
            icecream()
        if amount_icecream_balls <= 3:
            cone_cup = input(f"Would you like a Cone or a Cup for your ice cream balls?\n")
        elif amount_icecream_balls <= 8:
            print_slow(f"Here is your cup with {amount_icecream_balls} ice cream balls\n")
            cup = 1
        elif amount_icecream_balls > 8:
            print_slow ("Sorry we don't have any bigger cups.\n")
            clearScreen(1)
            icecream(1)
        else:
            print_slow("Sorry, the option you chose is not available.")
            clearScreen(2)
            icecream()
        clearScreen(1)
        icrecream_bolletjes_kosten = round (amount_icecream_balls * icecream_ball_price,2) # afgerond op 2 decimaal
        if cone_cup == "cone":
            cone = 1
        elif cone_cup == "cup":
            cup = 1
        cup_cost = cup_price * cup
        horn_cost = horn_price * cone
        toppings = input("What toppings would you like on your ice cream ?\n A. Nothing \n B. Cream \n C. Sprinkles\n D. Caramel\n").lower()

        if toppings == "a":
            A = True
            topping_price = 0
        elif toppings == "b":
            B = True
            topping_price = 0.50
        elif toppings == "c":
            C = True
            topping_price = 0.30
        elif toppings == "d":
            D = True
            if cone == 1:
                topping_price = 0.60
            else:
                topping_price = 0.90
        else:
            print_slow("Sorry, I didn't quite get that ?\n")
            clearScreen(2)
            icecream()
        choice = input(f"here is your order with {amount_icecream_balls} ice cream balls. Would you like to order again ?\n")



#-----------------------Function Execute--------------------#
icecream()

