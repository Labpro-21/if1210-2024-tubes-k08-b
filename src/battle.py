import random

from readwritecsv import * 
from potion import *
from RandomNumberGenerator import *

def choose(yourmonsterdata) :
    while True :
        print("=======PLEASE CHOOSE A MONSTER=======")
        x=0
        for i in yourmonsterdata :
            print(f"{x+1}. {i[1]}")
            x+=1
        chosen = input("-------->")
        k=0
        for i in range(1,len(yourmonsterdata)+1) :
            if str(i)==chosen :
                k=1
                break
        if k==1 : break
        else :
            print(f'pilihan ke-{chosen} tidak tersedia')
    return int(chosen)
    
        

def opening(monsterdata,random_number) :
    name = monsterdata[random_number][1]
    print(f'{name} telah datang !!!!!!!!!!!')
   
def battle(monsterdata,yourmonsterdata,userinventory,chosen,random_number) :
    file1 = monsterdata
    file2 = yourmonsterdata

    used_pot=[0,0,0]
    level=yourmonsterdata[chosen-1][2]
    name=yourmonsterdata[chosen-1][1]
    #PROGRAM UTAMA ==========================================================
    print("="*100)
    print(f'{name} siap membantu')
    
    x=0
    for i in monsterdata :
        if i[1]==name :
            break
        x+=1
    
    yourattack = int(file1[x][2]) + (int(level)-1)*(5/100)*int(file1[x][2])
    yourdefense = int(file1[x][3]) + (int(level)-1)*(5/100)*int(file1[x][3])
    yourhealth = int(file1[x][4]) + (int(level)-1)*(5/100)*int(file1[x][4])
    
    
    enemyhealth = int(file1[random_number][4])
    enemyattack = int(file1[random_number][2])
    enemydefense = int(file1[random_number][3])
    '''yourhealth = int(file2[chosen][2])+(5/100)*(int(file2[chosen][5])-1)*int(file2[chosen][2])
    yourattack = int(file2[chosen][3])+(5/100)*(int(file2[chosen][5])-1)*int(file2[chosen][3])
    yourdefense = int(file2[chosen][4])+(5/100)*(int(file2[chosen][5])-1)*int(file2[chosen][4])
    yourlevel =  int(file2[chosen][5])'''
    n=1
    while True :
        print(f"=====================TURN {n}======================")
        print("="*100)
        print(f"ENEMY : {file1[random_number][1]}")
        print(f"HEALTH : {enemyhealth}")
        print(f"ATTACK : {enemyattack}")
        print(f"DEFENSE : {enemydefense}")
        print("="*100)
        print(f"YOUR MONSTER : {name}")
        print(f"HEALTH : {yourhealth}")
        print(f"ATTACK : {yourattack}")
        print(f"DEFENSE : {yourdefense}")
        print(f"LEVEL : {level}")
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
                print(jumlahpot(userinventory))
                print("1. STRENGHT")
                print(f"   you have : {jumlahpot(userinventory)[0]}")
                print("2. RESILIENSE")
                print(f"   you have : {jumlahpot(userinventory)[1]}")
                print("3. HEAL")
                print(f"   you have : {jumlahpot(userinventory)[2]}")
                print("4. CANCEL")
                potionchoice = int(input("-------->"))
                newstat = potion(jumlahpot(userinventory),lokasipot(userinventory),used_pot,userinventory,yourattack,yourdefense,yourhealth,100000,name,potionchoice)
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
        yourhealth -= (enemyattack - (yourdefense/100)*enemyattack)
        print(f"{name} HEALTH IS DOWN TO {yourhealth}")
        
        if yourhealth <= 0 :
            print("="*100)
            print("YOU ARE DEAD")
            print("DONT GIVE UP")
            print("="*100)
            return 0
            break
        n+=1