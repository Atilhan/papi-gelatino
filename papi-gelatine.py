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

#print('Welkom bij Papi Gelatine je mag alle smaken kiezen zolang het maar vanille ijs is')

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


# import time,os,sys

# def clearScreen(sleepTime):
#     time.sleep(sleepTime)
#     os.system("cls")

# def print_slow(str):
#     for letter in str:
#         sys.stdout.write(letter)
#         sys.stdout.flush()

# reciept = [""]
# A,B,C,D = False,False,False,False
# business = False
# private = False
# taste_liter = 0

# horn_price = 1.25
# cup_price = 0.75
# icecream_ball_price = 0.95
# cone = 0
# cup = 0
# x = 1
# total = 0
# reciept = f'-------[Papi Gelatine]-------\n'

# def icecream():
#     choice = ""
#     cone_cup = ""
#     global cone,amount_icecream_balls,cup,topping_price,toppings,reciept,x

#     clearScreen(0)
#     print_slow("Welcome to Papi Gelatine\n")
#     business_private = input("Hello, did you come to order for \n 1. Business\n 2. Private\n ")
#     clearScreen(1)

#     if business_private == "1":
#         business_private = True
#         amount_icecream_balls = int(input("How many ice cream balls would you like ?\n"))
#         if amount_icecream_balls <= 8: 
#             i = 1
#             while i <= amount_icecream_balls:
#                 flavours = input ("What kind of flavour would you like for your" +str(i) + "\n 1.Strawberry\n 2.Chocolate\n 3. Vanille\n")
#                 clearScreen(1)
#                 if int(flavours) >= 1 and int(flavours) <= 3:
#                     i+=1
#                 else:
#                     print_slow("Sorry that is currently not available.")
#                     i += 0
#                     clearScreen(2)
#                     icecream()
#         else:
#             print_slow("Sorry, we don't have any bigger cups.\n")
#             clearScreen(1)
#             icecream()
#         if amount_icecream_balls <= 3:
#             cone_cup = input(f"Would you like a Cone or a Cup for your ice cream balls?\n")
#         elif amount_icecream_balls <= 8:
#             print_slow(f"Here is your cup with {amount_icecream_balls} ice cream balls\n")
#             cup = 1
#         elif amount_icecream_balls > 8:
#             print_slow ("Sorry we don't have any bigger cups.\n")
#             clearScreen(1)
#             icecream(1)
#         else:
#             print_slow("Sorry, the option you chose is not available.")
#             clearScreen(2)
#             icecream()
#         clearScreen(1)
#         icrecream_bolletjes_kosten = round (amount_icecream_balls * icecream_ball_price,2) # afgerond op 2 decimaal
#         if cone_cup == "cone":
#             cone = 1
#         elif cone_cup == "cup":
#             cup = 1
#         cup_cost = cup_price * cup
#         horn_cost = horn_price * cone
#         toppings = input("What toppings would you like on your ice cream ?\n A. Nothing \n B. Cream \n C. Sprinkles\n D. Caramel\n").lower()

#         if toppings == "a":
#             A = True
#             topping_price = 0
#         elif toppings == "b":
#             B = True
#             topping_price = 0.50
#         elif toppings == "c":
#             C = True
#             topping_price = 0.30
#         elif toppings == "d":
#             D = True
#             if cone == 1:
#                 topping_price = 0.60
#             else:
#                 topping_price = 0.90
#         else:
#             print_slow("Sorry, I didn't quite get that ?\n")
#             clearScreen(2)
#             icecream()
#         choice = input(f"here is your order with {amount_icecream_balls} ice cream balls. Would you like to order again ?\n")
#         reciept += f"ijsje {x}\nBalls   {amount_icecream_balls} X {format(icecream_ball_price,'.2f')} = {format(icrecream_bolletjes_kosten,'.2f')}\n {'Cones   '+cone+' X '+str(format(horn_price,'.2f'))+' = '+str(format(horn_cost,'.2f')) if cone > 0 else ''} Cup     {cup} X {format(cup_price,'.2f')} = {format(cup_price,'.2f')}\n Topping 1 X {format(topping_price,'.2f')} = {format(topping_price,'.2f')}\n-----------------------------\n"
#         if choice == "y":
#             global total
#             x += 1
#             total += horn_cost + cup_price + icrecream_bolletjes_kosten + topping_price
#             clearScreen(1)
#         elif choice == "n":
#             print_slow ("Thanks and come back anytime !, here is your reciept\n")
#             total += horn_cost + cup_price + icrecream_bolletjes_kosten + topping_price
#             print(f'{reciept} \n total {total}')
#         else:
#             print_slow ("Sorry, I don't understand that")
#     elif business == "2":
#         liters = int(input("How many liters of icecream would you like to order ? \n"))
#         clearScreen(1)
#         i = 1
#         while i <= liters:
#             taste_liter = input('What icecream flavour would you like for' + str(i) + "\n 1. Strawberry.\n 2. Chocolate. \n Vanille.\n ")
#             clearScreen(2)
#             if int(taste_liter) >= 1 and int(taste_liter) <= 3:
#                 i += 1
#             else:
#                 print_slow ('Sorry, currently not available.')
#                 i += 0
#                 clearScreen(2)
#                 icecream()
#             liter_cost = liters * 9.80
#             btw = (liter_cost / 106) * 6
#             print(f"--------[Papi Gelato]--------\n\nLiter  {liters} X €9,80 = {format(liter_cost,'.2f')}\n                -------\n Total           = {format(liter_cost,'.2f')}(9%) BTW         = {format(btw,'.2f')} \n\n----------------------------- ")
#             choice = input(f"Here is your with {liters} liters of icecream. Would you like to order again ? ( Y / N ) \n").lower()
#             if choice == "y":
#                 clearScreen(1)
#             elif choice == "n":
#                 print_slow ('Thank you and come back anytime !')
#                 clearScreen(2)
#             else:
#                 print_slow("Sorry, I don't understand that.")
#         else:
#             print_slow("Sorry, didn't quite get that.")
#     else:
#         print_slow ("Sorry, that is currently not a option we have.")
#         clearScreen(2)
#         icecream()


# #-----------------------Function Execute--------------------#
# icecream()

import time,os,sys

def clear_screen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

taste = ''

price_balls = 0.95
price_cup = 0.75
price_horn = 1.25

amount_cup = 0
amount_horn = 0
total_balls = 0

whipped_cream = 0.50
sprinkles = 0.30
caramel_H = 0.60
caramel_B = 0.90

toppings_1 = 0 #toppings_1
toppings_total = 0 

#==================== Intro / Regular Responses ====================#
def intro():
    print_slow ('Welcome to Papi Gelatine')
    clear_screen(1)
def thanks():
    print_slow ('Thank you & see you again ! ')
    clear_screen(1)
def no_option():
    print_slow ('Unfortunately that is not a option we provide')
    clear_screen(1)
def no_big_cups():
    print_slow ('Unfortunately we do not have any bigger cups')
    clear_screen(1)

#==================== Private or Business ? ====================#

def private_or_business():
    repeat_2 = True #check if irrelivant 
    while repeat_2:

        repeat_2 = False
        choice = input("Hello, would you like to order for \n 1. (A) Private \n 2. (B) Business \n").upper() #check if variable correct or non interrupting 

        if choice == "A" or choice == "B":
            return choice
        
        else:
            no_option()
            clear_screen(2)
            repeat_2 = True

#==================== Business_Receipt ======================#

def business_receipt():
    price_liter_ice = 9.80
    total = (liter_ice * price_liter_ice) #inquire into liter_ice
    btw = (total / 106 * 6)
    print("------------[Papi Gelato------------]")
    print("liter         {} x {:.2f}      = €{:.2f}".format((liter_ice),price_liter_ice,total))#inquire into
    print("totaal                      = €{:.2f}".format(total))
    print("btw (6%)                    = €{:.2f}".format(btw))

#==================== Business_Flavours  ====================#

def business_flavours():
    global liter_ice
    liter_amount = 0
    liter_ice = int (input('How much liters of ice would you like to order ?'))

    for x in range (liter_ice):
        liter_amount += 1
        choice_flavours = input('What flavours would you like for your {} liter ice ? \n S) Strawberry \n C) Chocolate \n V) Vanille').format(liter_amount).upper() #Zsmaken 

        if choice_flavours == "S":
            choice_flavours = "Strawberry"

        elif choice_flavours == "C":
            choice_flavours = "Chocolate"

        elif choice_flavours == "V":
            choice_flavours = "Vanille"
        
        else:
            no_option()
            business_flavours()

#==================== Toppings ====================#

def toppings(cup_horn):
    repeat = True
    while repeat:
        repeat = False
        global toppings , toppings_total
        toppings = input ("What kind of topping would you like ? \n A) Nothing \n B) Whipped Cream \n C) Sprinkles \n D) Caramel Sauce").upper()

        if toppings == "A":
            pass

        elif toppings == "B":
            toppings_1

#==================== Functions Executed ====================#
intro()
private_or_business()