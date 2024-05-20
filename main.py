from src.load import *
from src.battle import *
from src.arena import*
from src.RandomNumberGenerator import *
from src.inventory import *
from src.shopCurrency import *
from src.help import *
from src.laboratory import *
from src.jackpot import *
import time
from src.exit import *
from src.monsterManagement import *
from src.readwritecsv import *

data=load()
if data != [] :
    userData = data[0]
    inventoryData = data[1]
    monsterData = data[2]
    monsInvData = data[3]
    itemShopData = data[4]
    monsShopData = data[5]
    loginStatus = False
    while True :
        print("Ketik 'Help' untuk mendapatkan petunjuk dari Almighty God")
        command = input("---> ")
        if command.lower() == "login" :
            while True :
                userInv, yourMonsInv, role, coin = login(userData, inventoryData, monsInvData)
                if userInv != 0 and role != 0 and coin !=0 and yourMonsInv !=0 :
                    loginStatus = True
                    break
        elif command.lower() == 'register' :
            userInv, yourMonsInv, role, coin = register(userData, inventoryData, monsInvData, monsterData)
            loginStatus = True
        elif command.lower() == "help" :
            help(loginStatus, "belumlogin")
        elif command.lower() == 'save' :
            save(inventoryData, monsterData, userData, monsShopData, itemShopData, monsInvData)
        elif command.lower()=='exit' :
            exit(userData, monsInvData, itemShopData, monsterData, monsShopData, inventoryData)
            break
        else :
            print(f"command '{command}' tidak ada.")
        if loginStatus == True :
            if role.lower() == 'agent':
                while True :
                    id = int(userInv[0][0])
                    print("Ketik 'Help' untuk mendapatkan petunjuk dari Almighty God")
                    command = input("---> ")
                    if command.lower() == 'battle' :
                        randomNumber = RNG(1, len(monsterData))
                        time.sleep(2/10)
                        randomLevel = RNG(1,5)
                        confirm = battlerule()
                        if confirm.lower() == "n" :
                            continue
                        opening(monsterData, randomNumber)
                        chosen = choose(yourMonsInv)
                        battleCoin,damageTaken,damageDealt = battle(monsterData, monsInvData, yourMonsInv, userInv, chosen, randomNumber, randomLevel, 'battle')
                        coin += battleCoin
                        userData[id][4] = str(coin)
                    elif command.lower() == 'arena' :
                        arenaCoin = arena(monsterData, monsInvData, yourMonsInv, userInv)
                        coin += arenaCoin
                        userData[id][4] = str(coin)
                    elif command.lower() == 'inventory' :
                        inventory(userInv, yourMonsInv, monsterData, role, coin)
                    elif command.lower() == 'logout' :
                        while True :
                            confirm = input("Apakah anda yakin untuk logout?(Y/N)--> ")
                            if confirm.lower() == "y" :
                                print("Logout berhasil")
                                loginStatus = False
                                break
                            elif confirm.lower() == 'n' :
                                break
                            else : 
                                print("Masukkan input yang benar")
                        if loginStatus == False :
                            break
                    elif command.lower() == 'shop' :
                        coin = shopOpen(role, itemShopData, coin, userInv, monsterData, monsShopData, yourMonsInv, monsInvData)
                        userData[id][4] = str(coin)
                    elif command.lower() == 'help' :
                        help(loginStatus, role)
                    elif command.lower() == 'laboratory' :
                        coin = laboratory(yourMonsInv, coin, role)
                        userData[id][4] = str(coin)
                    elif command.lower() == 'jackpot' :
                        coin = jackpot(id, coin, monsInvData, yourMonsInv)
                        userData[id][4] = str(coin)
                    else :
                        print(f"command '{command}' tidak ada.")
            elif role == 'admin' :
                while True :
                    print("Ketik 'Help' untuk mendapatkan petunjuk dari Almighty God")
                    command = input("--->")
                    if command.lower() == 'help':
                        help(loginStatus, role)
                    elif command.lower() == 'shop':
                        monsShopData, itemShopData = shopmanagement(itemShopData, monsShopData, monsterData)
                    elif command.lower() == 'logout' :
                        while True :
                            confirm = input("Apakah anda yakin untuk logout?(Y/N)--> ")
                            if confirm.lower() == "y" :
                                print("Logout berhasil")
                                loginStatus = False
                                break
                            elif confirm.lower() == 'n' :
                                break
                            else : 
                                print("Masukkan input yang benar")
                        if loginStatus == False :
                            break
                    elif command.lower() == 'monster' :
                        monsterManagement(monsterData)
                    else :
                        print(f"command '{command}' tidak ada.")