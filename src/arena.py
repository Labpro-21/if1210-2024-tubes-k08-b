from src.battle import *
from src.RandomNumberGenerator import *

def arena(monsterdata,monsterinventory,yourmonsterdata,userinventory) :
    #deklarasi variabel
    reward = [20,35,50,75,90]  #coins gain from defeating each stage
    coins=0
    totaldamageTaken = 0
    totaldamageDealt = 0

    print("DO YOU WANT TO ENTER THE ARENA? (Y/N)") #double cek dari user
    inp = input("--->")
    if inp.lower()=="n" : #jika tidak jadi
        print("SEE U ANOTHER DAY")
    elif inp.lower()=="y" :   
        print("==========WELCOME TO THE ARENA==========")
        print("RULES :")
        print("1. THERE WILL BE A TOTAL OF 5 STAGES IN THE ARENA, EACH STAGE")
        print("   YOU HAVE TO FIGHT A MONSTER WITH EACH STAGE THE MONSTER WILL GET STRONGER")
        print("2. DEFEATING A MONSTER IN EACH STAGE WILL REWARD YOU WITH COINS, THE HIGHER")
        print("   THE STAGE THE BIGGER THE REWARD")
        print("3. IF YOU LOSE ONCE, THE ARENA WILL BE OVER, IF YOU WIN ALL THE WAY")
        print("   TO THE FIFTH STAGE YOU WILL GET MAXIMUM COINS")
        
        chosen = choose(yourmonsterdata) #fungsi untuk memilih monster dari pilihan monsterinventory
        stage = 1
        for i in range(5) : #pemanggilan fungsi battle sebanyak maksimum 5 kali
            random_number = RNG(1,len(monsterdata))
            enemylevel = i+1  #level monster musuh sesuai nomor stage
            print(f"--------->>>STAGE {i+1}<<<---------")
            opening(monsterdata,random_number)
            coin,damageTaken,damageDealt = battle(monsterdata,monsterinventory,yourmonsterdata,userinventory,chosen,random_number,enemylevel,'arena')
            totaldamageTaken += damageTaken
            totaldamageDealt += damageDealt

            if coin==0 : #coin==0 di arena hanya terjadi saat monster kita kalah
                print("ARENA IS OVER, TRY AGAIN")
                break
            else :  #monster kita menang
                stage += 1

        for i in range(1,stage) :
            coins += reward[i-1]
        
        if stage==6 :   #jika berhasil sampai ke stage terakhir dan menang akan mendapatkan bonus 50 coin
            print("CONGRATULATION YOU MADE IT ALL THE WAY!!!!")
            print("HERE A BONUS 50 COINS FOR YOU!!!")
            coins += 50

        #STATISTIK ARENA
        print("==========================================")
        print("STATISTICS FROM THE ARENA :")
        print(f"NUMBER OF STAGE : {stage-1}")
        print(f"TOTAL COIN GAINED FROM THE ARENA : {coins}")
        print(f"TOTAL DAMAGE TAKEN : {totaldamageTaken}")
        print(f"TOTAL DAMAGE DEALT : {totaldamageDealt}")
        print("==========================================")
    else :
        print("Masukkan input yg benar(Y/N)--->")
    return coins