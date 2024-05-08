enemyhealth = 1000
enemyattack = 100
yourhealth = 500
yourattack = 150
strenghtindex = 0
resindex = 0
#FUNGSI =================================================================


#PROGRAM UTAMA ==========================================================
print("PARJO TELAH DATANG HAHAHA")
print("="*100)
print("PIKA SIAP MEMBANTU")


n=1
while True :
    print("="*100)
    print(f"ENEMY : PARJO")
    print(f"HEALTH : {enemyhealth}")
    print("="*100)
    print(f"YOUR MONSTER : PIKA")
    print(f"HEALTH : {yourhealth}")
    print(f"==========TURN {n}==========")
    print("CHOOSE AN ACTION :")
    print("1. ATTACK")
    print("2. DRINK POTION")
    print("3. QUIT")
    action = int(input("-------->"))
    if action==1 :
        enemyhealth -= (yourattack + strenghtindex*10/100*yourattack)
        print("YOU ATTACKED !!!!!!!!")
        print(f"ENEMY MONSTER HEALTH IS DOWN TO {enemyhealth}")
    elif action==2 :
        print("=======CHOOSE A POTION !=======")
        print("1. STRENGHT")
        print("2. RESILIENSE")
        print("3. HEAL")
        potionchoice = int(input("-------->"))
        if potionchoice==1 :
            strenghtindex += 1
            print("YOU BECOME STRONGER")
        elif potionchoice==2 :
            resindex +=1
            print("YOU BECOME MORE DURABLE")
        elif potionchoice==3 :
            yourhealth += 300
            print("YOU RESTORED 300 HEALTH")
    elif action==3 :
        break
    print("PARJO ATTACK BACK !!!")
    yourhealth -= (enemyattack - resindex*10/100*enemyattack)

    if enemyhealth <= 0 : 
        print("="*100)
        print("YOU DEFEATED YOUR ENEMY")
        print("WOHOOOOOO")
        print("="*100)
        break
    elif yourhealth <= 0 :
        print("="*100)
        print("YOU ARE DEAD")
        print("DONT GIVE UP")
        print("="*100)
        break
    n+=1