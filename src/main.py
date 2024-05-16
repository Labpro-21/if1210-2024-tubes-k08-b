from load import *
from battle import *
from arena import*
from RandomNumberGenerator import *
from inventory import *
from shopCurrency import *
from help import *
from laboratory import *
import time

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
        if command =="login" :
            while True :
                userinventory,yourmonsterinventory,role,coins = login(user,inventory,monsterinventory)
                if userinventory != 0 and role != 0 and coins !=0 and yourmonsterinventory !=0 :
                    loginstatus = True
                    break
        elif command =='register' :
            userinventory,yourmonsterinventory,role,coins = register(user,inventory,monsterinventory,monster)
            loginstatus = True
        elif command =="help" :
            help(loginstatus,"belumlogin")
        else :
            print(f"command '{command}' tidak ada.")
        if loginstatus==True :
            if role=='agent':
                while True :
                    id = int(userinventory[0][0])
                    command = input("--->")
                    if command == 'battle' :
                        random_number = RNG(1,5)
                        time.sleep(2/10)
                        random_level = RNG(1,5)
                        opening(monster,random_number)
                        chosen=choose(yourmonsterinventory)
                        coin = battle(monster,monsterinventory,yourmonsterinventory,userinventory,chosen,random_number,random_level,'battle')
                        coins+=coin
                        user[id][4]=str(coins)
                        print(userinventory)
                    elif command == 'arena' :
                        coin = arena(monster,monsterinventory,yourmonsterinventory,userinventory)
                        coins+=coin
                        user[id][4]=str(coins)
                    elif command == 'inventory' :
                        inventoryy(userinventory,yourmonsterinventory,monster,role,coins)
                    elif command == 'logout' :
                        t=0
                        while True :
                            confirm = input("Apakah anda yakin untuk logout?(Y/N)-->")
                            if confirm == "Y" :
                                print("Logout berhasil")
                                t=1
                                break
                            elif confirm =='N' :
                                t=1
                                break
                            else : print("mangsud?")
                        if t==1 :
                                loginstatus=False
                                break
                    elif command == 'Shop' :
                        coins=shopOpen(role,itemshop,coins,userinventory,monster,monstershop,yourmonsterinventory,monsterinventory)
                        user[id][4]=str(coins)
                    elif command == 'help' :
                        help(loginstatus,role)
                    elif command == 'laboratory' :
                        coins = laboratory(yourmonsterinventory,coins,role)
                        user[id][4]=str(coins)
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
                    if command=='help':
                        help(loginstatus,role)
                    elif command=='shop':
                        shopmanagement(itemshop,monstershop,monster)
                    elif command == 'logout' :
                        t=0
                        while True :
                            confirm = input("Apakah anda yakin untuk logout?(Y/N)-->")
                            if confirm == "Y" :
                                print("Logout berhasil")
                                t=1
                                break
                            elif confirm =='N' :
                                t=1
                                break
                            else : print("mangsud?")
                        if t==1 :
                                loginstatus=False
                                break