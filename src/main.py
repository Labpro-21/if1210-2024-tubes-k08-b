from load import *
from battle import *
from arena import*
from RandomNumberGenerator import *
from inventory import *
from shopCurrency import *
from help import *
from laboratory import *
from jackpot import *
import time
from exit import *

data=load()
if data != [] :
    user = data[0]
    inventory = data[1]
    monster = data[2]
    monsterinventory = data[3]
    itemshop=data[4]
    monstershop=data[5]
    loginstatus = False
    while True :
        command =  input("--->")
        if command.lower() == "login" :
            while True :
                userinventory,yourmonsterinventory,role,coins = login(user,inventory,monsterinventory)
                if userinventory != 0 and role != 0 and coins !=0 and yourmonsterinventory !=0 :
                    loginstatus = True
                    break
        elif command.lower() == 'register' :
            userinventory,yourmonsterinventory,role,coins = register(user,inventory,monsterinventory,monster)
            loginstatus = True
        elif command.lower() == "help" :
            help(loginstatus,"belumlogin")
        elif command.lower() == 'save' :
            save(inventory,monster,user,monstershop,itemshop,monsterinventory)
        elif command.lower()=='exit' :
            exit(user,monsterinventory,itemshop,monster,monstershop,inventory)
            break
        else :
            print(f"command '{command}' tidak ada.")
        if loginstatus==True :
            if role.lower() == 'agent':
                while True :
                    id = int(userinventory[0][0])
                    command = input("--->")
                    if command.lower() == 'battle' :
                        random_number = RNG(1,len(monster))
                        time.sleep(2/10)
                        random_level = RNG(1,5)
                        opening(monster,random_number)
                        chosen=choose(yourmonsterinventory)
                        coin = battle(monster,monsterinventory,yourmonsterinventory,userinventory,chosen,random_number,random_level,'battle')
                        coins+=coin
                        user[id][4]=str(coins)
                        print(userinventory)
                    elif command.lower() == 'arena' :
                        coin = arena(monster,monsterinventory,yourmonsterinventory,userinventory)
                        coins+=coin
                        user[id][4]=str(coins)
                    elif command.lower() == 'inventory' :
                        inventoryy(userinventory,yourmonsterinventory,monster,role,coins)
                    elif command.lower() == 'logout' :
                        t=0
                        while True :
                            confirm = input("Apakah anda yakin untuk logout?(Y/N)-->")
                            if confirm.lower() == "y" :
                                print("Logout berhasil")
                                t=1
                                break
                            elif confirm.lower() =='n' :
                                t=1
                                break
                            else : print("mangsud?")
                        if t==1 :
                                loginstatus=False
                                break
                    elif command.lower() == 'shop' :
                        coins=shopOpen(role,itemshop,coins,userinventory,monster,monstershop,yourmonsterinventory,monsterinventory)
                        user[id][4]=str(coins)
                    elif command.lower() == 'help' :
                        help(loginstatus,role)
                    elif command.lower() == 'laboratory' :
                        coins = laboratory(yourmonsterinventory,monster,coins,role)
                        user[id][4]=str(coins)
                    elif command.lower() == 'jackpot' :
                        jackpot(id,coins, monsterinventory,yourmonsterinventory)
                    else :
                        print(f"command '{command}' tidak ada.")
                        print(userinventory)
                        print(inventory)
                        print(user)
                        print(monsterinventory)
                        print(yourmonsterinventory)
                        print(itemshop)
                        print(monstershop)
            elif role=='admin' :
                while True :
                    command = input("--->")
                    if command.lower() =='help':
                        help(loginstatus,role)
                    elif command.lower() =='shop':
                        shopmanagement(itemshop,monstershop,monster)
                    elif command.lower() == 'logout' :
                        t=0
                        while True :
                            confirm = input("Apakah anda yakin untuk logout?(Y/N)-->")
                            if confirm.lower() == "y" :
                                print("Logout berhasil")
                                t=1
                                break
                            elif confirm.lower() =='n ' :
                                t=1
                                break
                            else : print("mangsud?")
                        if t==1 :
                                loginstatus=False
                                break