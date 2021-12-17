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

def stap_1():
    repeat = True 
    while repeat:
        repeat = False
        aantal = int(input("Hoeveel bolletjes wilt u ?"))
        if aantal <= 3:
            stap_2(aantal)
        elif aantal > 3 and aantal <= 8:
            print (f'Dan krijgt u van mij een bakje met {aantal}  bolletjes ')
        elif aantal > 8:
            print ('Sorry zulke grote bakken hebben we niet')
            repeat = True
        else:
            repeat = True
            print('Dat begrijp ik niet')

def stap_2(aantal_2):
    bol_bak = input(f'Wilt u deze {aantal_2} in A) een hoorntje of B) een bakje?')



stap_1()



