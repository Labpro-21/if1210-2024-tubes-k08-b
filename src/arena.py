from src.battle import *
from src.RandomNumberGenerator import *
def arenaart() :
    print(f'''
                                T~~
                                /"
                        T~~     |'| T~~
                    T~~ |    T~ WWWW|
                    |  /"\   |  |  |/\T~~
                    /"\ WWW  /"\ |' |WW|
                    WWWWW/\| /   \|'/\|/"
                    |   /__\/]WWW[\/__\WWWW
                    |"  WWWW'|I_I|'WWWW'  |
                    |   |' |/  -  \|' |'  |
                    |'  |  |LI=H=LI|' |   |
                    |   |' | |[_]| |  |'  |
                    |   |  |_|###|_|  |   |
                    '---'--'-/___\-'--'---' ''')

def arenarule() :
    arenaart()
    print("""
======================WELCOME TO THE ARENA======================
ARENA MEKANISM :
    1. THERE WILL BE A TOTAL OF 5 STAGES IN THE ARENA, EACH STAGE YOU WILL BE BATTLING 
       A RANDOMLY SELECTED MONSTER
    2. YOUR ENEMY LEVEL WILL BE EQUAL TO THE STAGE NUMBER YOUR CURRENTLY ON
    3. DEFEATING EACH STAGE WILL GAVE YOU A REWARD, THE HIGHER THE STAGE, THE
       THE GREATER THE REWARD
    4. IF YOU LOSE ONCE, THE ARENA WILL BE OVER
    5. IF YOU WIN ALL THE WAY, YOU WILL GET A BONUS REWARD
    6. POTIONS EFFECT ONLY LAST TILL THE END OF EACH STAGE
    7. MONSTER BALL IS PROHIBITED IN THE ARENA    """)
    while True :
        confirm = input("PROCEED?(Y/N)--->")
        if confirm.lower() =='y' :
            return confirm
        elif confirm.lower() =='n' :
            return confirm
        else :
            print("BE CLEAR")

def arena(monsterdata,monsterinventory,yourmonsterdata,userinventory) :
    #deklarasi variabel
    reward = [20,35,50,75,90]  #coins gain from defeating each stage
    coins=0
    totaldamageTaken = 0
    totaldamageDealt = 0
    confirm = arenarule()
    if confirm.lower()=="n" : #jika tidak jadi
        print("SEE U ANOTHER DAY")
    else :   
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
                print("STAGE CLEARED")
                print()
                if stage != 6 :
                    print("PREPARING NEXT STAGE")

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
    return coins