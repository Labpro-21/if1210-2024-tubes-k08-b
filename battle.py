import random
random_number = random.randint(1, 10)

def read_csv(path) :
    field = ''
    row = []
    data =[]
    with open(path) as file :
            for char in file.read():
                if char == ',':
                    row.append(field)
                    field=''
                elif char=="\n" :
                    row.append(field)
                    data.append(row)
                    field=''
                    row=[]
                else :
                    field += char
            row.append(field)
            data.append(row)
    return data

def choose(path) :
    file = read_csv(path)
    print("=======PLEASE CHOOSE A MONSTER=======")
    for i in range(len(file)-1) :
        print(f"{i+1}. {file[i+1][1]}")
    chosen = int(input("-------->"))
    return chosen

def opening() :
    file1 = read_csv("enemymonster.csv")
    print(f"{file1[random_number][1]} TELAH DATANG HAHAHA")

def decoy() :
    1+1

def battle(function1,function2) :
    file1 = read_csv("enemymonster.csv")
    file2 = read_csv("yourmonster.csv")

    function1()
    chosen = choose("yourmonster.csv")
    function2()

    #PROGRAM UTAMA ==========================================================
    print("="*100)
    print(f"{file2[chosen][1]} SIAP MEMBANTU")

    enemyhealth = int(file1[random_number][2])
    enemyattack = int(file1[random_number][3])
    yourhealth = int(file2[chosen][2])
    yourattack = int(file2[chosen][3])
    strenghtindex = 0
    resindex = 0
    n=1
    while True :
        print("="*100)
        print(f"ENEMY : {file1[random_number][1]}")
        print(f"HEALTH : {enemyhealth}")
        print(f"ATTACK : {enemyattack}")
        print("="*100)
        print(f"YOUR MONSTER : {file2[chosen][1]}")
        print(f"HEALTH : {yourhealth}")
        print(f"ATTACK : {yourattack}")
        print(f"==========TURN {n}==========")
        print("CHOOSE AN ACTION :")
        print("1. ATTACK")
        print("2. DRINK POTION")
        print("3. QUIT")
        action = int(input("-------->"))
        if action==1 :
            enemyhealth -= yourattack
            print("YOU ATTACKED !!!!!!!!")
            if enemyhealth >= 0 :
                print(f"ENEMY MONSTER HEALTH IS DOWN TO {enemyhealth}")
        elif action==2 :
            print("=======CHOOSE A POTION !=======")
            print("1. STRENGHT")
            print("2. RESILIENSE")
            print("3. HEAL")
            potionchoice = int(input("-------->"))
            if potionchoice==1 :
                strenghtindex += 1
                yourattack += strenghtindex*10/100*yourattack
                print("YOU BECOME STRONGER")
            elif potionchoice==2 :
                resindex +=1
                print("YOU BECOME MORE DURABLE")
            elif potionchoice==3 :
                yourhealth += 300
                print("YOU RESTORED 300 HEALTH")
        elif action==3 :
            break

        if enemyhealth <= 0 : 
            print("="*100)
            print("YOU DEFEATED YOUR ENEMY")
            print("WOHOOOOOO")
            print("="*100)
            break

        print(f"{file1[random_number][1]} ATTACK BACK !!!")
        yourhealth -= (enemyattack - resindex*10/100*enemyattack)
        
        if yourhealth <= 0 :
            print("="*100)
            print("YOU ARE DEAD")
            print("DONT GIVE UP")
            print("="*100)
            break
        n+=1