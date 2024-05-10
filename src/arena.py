from battle import *

def arena() :
    coins = 0
    for i in range(5) :
        print(f"===============================ROUND {i+1}===================================")
        coin = battle(choose())
        if coin == 0 :
            break 
        coins +=coin
    print(f"YOU ACCUMULATED {coins} coins")
    return coins