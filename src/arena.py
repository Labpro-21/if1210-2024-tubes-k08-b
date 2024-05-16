from battle import *
from RandomNumberGenerator import *

def arena(monsterdata,monsterinventory,yourmonsterdata,userinventory) :

    coins=0

    print("DO YOU WANT TO ENTER THE ARENA? (Y/N)")
    inp = input("--------->")
    if inp=="N" :
        print("SEE U ANOTHER DAY")
    elif inp=="Y" :
        print("=====WELCOME TO THE ARENA=====")
        print("RULES :")
        print("1. THERE WILL BE A TOTAL OF 5 STAGES IN THE ARENA, EACH STAGE")
        print("   YOU HAVE TO FIGHT A MONSTER WITH EACH STAGE THE MONSTER WILL GET STRONGER")
        print("2. DEFEATING A MONSTER IN EACH STAGE WILL REWARD YOU WITH COINS, THE HIGHER")
        print("   THE STAGE THE BIGGER THE REWARD")
        print("3. IF YOU LOSE ONCE, THE ARENA WILL BE OVER, IF YOU WIN ALL THE WAY")
        print("   TO THE FIFTH STAGE YOU WILL GET MAXIMUM COINS")
        
        chosen = choose(yourmonsterdata) 

        for i in range(5) :
            random_number = RNG(1,5)
            random_level = RNG(1,5)
            opening(monsterdata,random_number)
            coin = battle(monsterdata,monsterinventory,yourmonsterdata,userinventory,chosen,random_number,random_level,'arena')
            coins += coin
            if coin==0 :
                print(f"YOU MADE IT TO STAGE NUMBER {i+1}, KEEP IMPROVING")
                break

        else :
            print("CONGRATULATION YOU MADE IT ALL THE WAY!!!!")
            print("HERE A BONUS 50 COIN FOR YOU!!!")
            coins += 50
        print(f"YOUR TOTAL COIN GAINED FROM THE ARENA : {coins}")
    return coins

