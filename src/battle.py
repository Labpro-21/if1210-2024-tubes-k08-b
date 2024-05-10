import random

from readwritecsv import * 
from potion import *
from RandomNumberGenerator import *
random_number = RNG(1,10)

def choose(path) :
    file = read_csv(path)
    print("=======PLEASE CHOOSE A MONSTER=======")
    for i in range(len(file)-1) :
        print(f"{i+1}. {file[i+1][1]}")
    chosen = int(input("-------->"))
    return chosen

def decoy() :
    1+1

def battle(monsterpath,yourmonsterpath,chosen) :
    file1 = read_csv(monsterpath)
    file2 = read_csv(yourmonsterpath)

    print(f"{file1[random_number][1]} TELAH DATANG HAHAHA")

    #PROGRAM UTAMA ==========================================================
    print("="*100)
    print(f"{file2[chosen][1]} SIAP MEMBANTU")

    enemyhealth = int(file1[random_number][2])
    enemyattack = int(file1[random_number][3])
    enemydefense = int(file1[random_number][4])
    yourhealth = int(file2[chosen][2])+(5/100)*(int(file2[chosen][5])-1)*int(file2[chosen][2])
    yourattack = int(file2[chosen][3])+(5/100)*(int(file2[chosen][5])-1)*int(file2[chosen][3])
    yourdefense = int(file2[chosen][4])+(5/100)*(int(file2[chosen][5])-1)*int(file2[chosen][4])
    yourlevel =  int(file2[chosen][5])
    strenghtindex = 0
    resindex = 0
    n=1
    while True :
        print(f"=====================TURN {n}======================")
        print("="*100)
        print(f"ENEMY : {file1[random_number][1]}")
        print(f"HEALTH : {enemyhealth}")
        print(f"ATTACK : {enemyattack}")
        print(f"DEFENSE : {enemydefense}")
        print("="*100)
        print(f"YOUR MONSTER : {file2[chosen][1]}")
        print(f"HEALTH : {yourhealth}")
        print(f"ATTACK : {yourattack}")
        print(f"DEFENSE : {yourdefense}")
        print(f"LEVEL : {yourlevel}")
        print(f"====================")
        print("CHOOSE AN ACTION :")
        print("1. ATTACK")
        print("2. DRINK POTION")
        print("3. QUIT")
        print("=====================")
        action = int(input("-------->"))
        if action==1 :
            enemyhealth -= (yourattack-(enemydefense/100)*yourattack)
            print("YOU ATTACKED !!!!!!!!")
            if enemyhealth >= 0 :
                print(f"ENEMY MONSTER HEALTH IS DOWN TO {enemyhealth}")
        elif action==2 :
            while True :
                print("=======CHOOSE A POTION !=======")
                print("1. STRENGHT")
                print(f"   you have :{potion_data[1][1]}")
                print("2. RESILIENSE")
                print(f"   you have :{potion_data[2][1]}")
                print("3. HEAL")
                print(f"   you have :{potion_data[3][1]}")
                print("4. CANCEL")
                potionchoice = int(input("-------->"))
                newstat = potion(potion_data,used_Pot_Array,yourattack,yourdefense,yourhealth,100000,file2[chosen][1],potionchoice)
                if potionchoice ==1 :
                    if newstat==0 :
                        continue
                    else :
                        yourattack = newstat
                        break
                elif potionchoice ==2 :
                    if newstat==0 :
                        continue
                    else :
                        yourdefense = newstat
                        break
                elif potionchoice ==3 :
                    if newstat==0 :
                        continue
                    else :
                        yourhealth = newstat
                        break
                elif potionchoice ==4 :
                    break
            if potionchoice == 4 :
                continue

        elif action==3 :
            coin = 0
            return coin
            break

        if enemyhealth <= 0 : 
            print("="*100)
            print("YOU DEFEATED YOUR ENEMY")
            print("WOHOOOOOO")
            print("="*100)
            coin = random.randint(50,100)
            print(f"YEEEEEY YOU GOT {coin} coin")
            return coin
            break

        print(f"{file1[random_number][1]} ATTACK BACK !!!")
        yourhealth -= (enemyattack - resindex*10/100*enemyattack - (yourdefense/100)*enemyattack)
        
        if yourhealth <= 0 :
            print("="*100)
            print("YOU ARE DEAD")
            print("DONT GIVE UP")
            print("="*100)
            return 0
            break
        n+=1
battle("src\enemymonster.csv","src\yourmonster.csv",choose("src\yourmonster.csv"))