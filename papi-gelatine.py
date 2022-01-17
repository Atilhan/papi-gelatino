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

topping_price = 0
cone = 0
cup = 0
bolletjes_price = 0.95
horn_price = 1.25
reciept = f'---[Papi Gelato]---\n'
total = 0

def icecream():
    choice = ""
    cone_cup = ""
    global cone,amount_icecream_balls,cup,topping_price,toppings

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


#-----------------------Function Execute--------------------#
icecream()

