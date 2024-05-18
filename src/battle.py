#import module yang dibutuhkan 
from potion import *
from RandomNumberGenerator import *
from monsterball import *

#fungsi untuk memilih monster yg ingin dipakai untuk battle
def choose(yourmonsterdata) :
    while True :
        print("=======PLEASE CHOOSE A MONSTER=======")
        x=0
        for i in yourmonsterdata : #menampilkan seluruh monster yg player punya
            print(f"{x+1}. {i[1]}")
            x+=1
        chosen = input("(1/2/3/dst)--->") #input monster yg ingin dipilih
        k=0
        for i in range(1,len(yourmonsterdata)+1) : 
            if str(i)==chosen :
                k=1
                break #jika monster yg dipilih ada dalam pilihan
        if k==1 : break
        else :
            print(f'pilihan ke-{chosen} tidak tersedia') #jika tidak ada dalam pilihan
    return int(chosen)
    
        
#fungsi untuk menampilkan monster yg akan dilawan
def opening(monsterdata,random_number) :
    name = monsterdata[random_number][1]
    print(f'''=============================================
>>>>>>>>>{name} telah datang !!!<<<<<<<<<
============================================='''
            )
   
def battle(monsterdata,monsterinventory,yourmonsterdata,userinventory,chosen,random_number,random_level,type) :
    file1 = monsterdata

    used_pot=[0,0,0] #potion hanya bisa digunakan sekali

    level=yourmonsterdata[chosen-1][2] #level monster anda
    name=yourmonsterdata[chosen-1][1]  #nama monster anda
    
    #PROGRAM UTAMA ==========================================================
    print("="*100)
    print(f'{name} siap membantu')
    
    indeks=0
    for i in file1 : #mencari indeks monster kita di file monster.csv
        if i[1]==name :
            break
        indeks+=1

    #deklarasi stat variabel 
    originalhealth = int(int(file1[indeks][4]) + (int(level)-1)*(10/100)*int(file1[indeks][4]))
    yourattack = int(int(file1[indeks][2]) + (int(level)-1)*(10/100)*int(file1[indeks][2]))
    yourdefense = int(int(file1[indeks][3]) + (int(level)-1)*(10/100)*int(file1[indeks][3]))
    yourhealth = int(int(file1[indeks][4]) + (int(level)-1)*(10/100)*int(file1[indeks][4]))
    enemyhealth = int(int(file1[random_number][4]) + (random_level-1)*(10/100)*int(file1[random_number][4]))
    enemyattack = int(int(file1[random_number][2]) + (random_level-1)*(10/100)*int(file1[random_number][2]))
    enemydefense = int(int(file1[random_number][3]) + (random_level-1)*(10/100)*int(file1[random_number][3]))
    
    damagetaken=0
    damagedealt=0
    turn=1
    while True :
        #menampilkan stat kedua monster saat battle
        print(f">>>>>>>>>>>>>>>>>TURN {turn}<<<<<<<<<<<<<<<<<<<<")
        print("=============================================")
        print(f"ENEMY : {file1[random_number][1]}")
        print(f"HEALTH : {enemyhealth}")
        print(f"ATTACK : {enemyattack}")
        print(f"DEFENSE : {enemydefense}")
        print(f"LEVEL : {random_level}")
        print("=============================================")
        print(f"YOUR MONSTER : {name}")
        print(f"HEALTH : {yourhealth}")
        print(f"ATTACK : {yourattack}")
        print(f"DEFENSE : {yourdefense}")
        print(f"LEVEL : {level}")
        print("=============================================")
        #menampilkan action yg bisa dilakukan
        print("CHOOSE AN ACTION :")
        print("1. ATTACK")
        print("2. DRINK POTION")
        if type=='battle' : #jika mode battle terdapat option tambahan yaitu monsterball
            print("3. MONSTER BALL ")
            print("4. QUIT")
        elif type=='arena' :
            print("3. QUIT") #jika mode arena tidak ada option monsterball
        print("=====================")
        action = (input("choose an action(1/2/3/4)--->"))
        if action=='1' :
            #ACTION ATTACK
            damage = RNG(yourattack*(70/100),yourattack*(130/100)) 
            if enemyhealth >= (damage-(enemydefense/100)*damage) :  #menghitung damagedealt jika enemy belom mati
                damagedealt += (damage-(enemydefense/100)*damage)
            else : #jika enemy mati maka damagedealt hanya ditambah sebesar sisa darah enemy sebelum mati
                damagedealt += enemyhealth
            enemyhealth -= (damage-(enemydefense/100)*damage) 
            enemyhealth = int(enemyhealth)
            print("=============================================")
            print(">>>>>>>>>>>>>>>YOU ATTACKED !!!<<<<<<<<<<<<<<")
            if enemyhealth > 0 : #JIKA MONSTER BELOM MATI
                print(f"ENEMY MONSTER HEALTH IS DOWN TO {enemyhealth}")
        elif action=='2' :
            #ACTION POTION
            while True :
                print("=======CHOOSE A POTION !=======")
                print("1. STRENGHT")
                print(f"   you have : {jumlahpot(userinventory)[0]}")
                print("2. RESILIENSE")
                print(f"   you have : {jumlahpot(userinventory)[1]}")
                print("3. HEAL")
                print(f"   you have : {jumlahpot(userinventory)[2]}")
                print("4. CANCEL")
                potionchoice = (input("(1/2/3/4)--->"))
                #jika input tidak benar
                if potionchoice!='1' and potionchoice!='2' and potionchoice!='3' and potionchoice!='4' :
                    print(f"Opsi {potionchoice} tidak ada")
                    continue
                #newstat adalah stat baru baik untuk atk/def/hp setelah memakai potion
                newstat = potion(jumlahpot(userinventory),lokasipot(userinventory),used_pot,userinventory,yourattack,yourdefense,yourhealth,originalhealth,name,int(potionchoice))
                if potionchoice =='1' : #ATK potion
                    if newstat==0 : #jika potion tidak bisa digunakan
                        continue
                    else :
                        yourattack = int(newstat)
                        break
                elif potionchoice =='2' : #DEF potion
                    if newstat==0 :
                        continue
                    else :
                        yourdefense = int(newstat)
                        break
                elif potionchoice =='3' : #Heal potion
                    if newstat==0 :
                        continue
                    else :
                        yourhealth = int(newstat)
                        break
                elif potionchoice =='4' : #Cancel
                    break
            if potionchoice == '4' : 
                continue
        elif action=='3' : 
            if type =='battle' : #Jika mode battle action 3 adalah monster ball
                success = monsterball(random_number,random_level,userinventory,monsterdata,monsterinventory,yourmonsterdata)
                if success==1 :
                    return 0,damagetaken,damagedealt
                elif success ==2 : #Jika gagal
                    continue
            elif type =='arena': #Jika mode arena action 3 adalah quit
                print('=============================================')
                print('ANDA MENINGGALKAN PERTANDINGAN')
                print('=============================================')
                coin = 0
                return coin,damagetaken,damagedealt
        elif action=='4' :
            if type=='arena' :
                print("opsi 4 tidak ada")
                continue
            elif type=='battle' :
                print('ANDA MENINGGALKAN PERTANDINGAN')
                coin = 0
                return coin,damagetaken,damagedealt     
        else :
            print(f"opsi {action} tidak ada")
            continue
        
        #Jika musuh darahnya sudah habis
        if enemyhealth <= 0 : 
            print("=============================================")
            print("YOU DEFEATED YOUR ENEMY")
            print("WOHOOOOOO")
            print("="*100)
            coin = RNG(1,50)
            print(f"YEEEEEY YOU GOT {coin} coin")
            print("=============================================")
            return coin,damagetaken,damagedealt
        
        #Jika musuh masih hidup, musuh menyerang balik
        damagemusuh=RNG(enemyattack*(70/100),enemyattack*(130/100))
        print(f">>>>>>>>>>>>>{file1[random_number][1]} ATTACK BACK !!!<<<<<<<<<<<<")
        if yourhealth >= (damagemusuh - (yourdefense/100)*damagemusuh) :
            damagetaken += (damagemusuh - (yourdefense/100)*damagemusuh) #Jika monster kita masih hidup setelah serangan
        else :
            damagetaken += yourhealth #jika monster kita mati setelah serangan
        yourhealth -= (damagemusuh - (yourdefense/100)*damagemusuh)
        yourhealth = int(yourhealth)
        if yourhealth >0 : #jika monster kita masih hidup
            print(f"{name} HEALTH IS DOWN TO {yourhealth}")
        print("=============================================")

        #jika darah monster kita habis
        if yourhealth <= 0 :
            print("=============================================")
            print("YOU ARE DEAD")
            print("DONT GIVE UP")
            print("=============================================")
            return 0,damagetaken,damagedealt
        turn+=1