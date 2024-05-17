from RandomNumberGenerator import *
import time
def cekrng(RNG) :
    if RNG>=1 and RNG<=40 :
        item = 0
    elif RNG>=41 and RNG<=65 :
        item = 1
    elif RNG>=66 and RNG<=80 :
        item = 2
    elif RNG>=81 and RNG<=95 :
        item = 3
    elif RNG>=96 and RNG<=100 :
        item = 4
    return item

def gacha(yourcoin) :
    yourcoin = int(yourcoin)
    icon = ['TOPI', 'PEDANG', 'BAJU', 'CELANA', 'JAM' ]
    value = [50,100,150,200,250,400]
    RNG1 = RNG(1,100)
    time.sleep(2/10)
    RNG2 = RNG(1,100)
    time.sleep(1/10)
    RNG3 = RNG(1,100)
    item1 = cekrng(RNG1)
    item2 = cekrng(RNG2)
    item3 = cekrng(RNG3)
    totalcoin = value[item1]+value[item2]+value[item3]
    print(f"{icon[item1]} | {icon[item2]} | {icon[item3]}")
    prize = False
    if prize == False :
        if item1==item2 and item2==item3 :
            print('SELAMATT!! ANDA MENDAPATKAN GORLOCK THE DESTROYER! DESTROY EVERYTHING!')
            prize == True
        else :
            print(f"ANDA TIDAK DAPAT JACKPOT, TAPI ANDA DAPAT {totalcoin} COINS !!!")
            yourcoin += totalcoin
    elif prize == True :
        if item1==item2 and item2==item3 :
            print('SELAMATT!! GORLOCK SUDAH ANDA MILIKI, GORLOCK AKAN DIUBAH KE O.W.C.A Coin sebanyak 1000 Coin')
            yourcoin += 1000
        else :
            print(f"ANDA TIDAK DAPAT JACKPOT, TAPI ANDA DAPAT {totalcoin} COINS !!!")
            yourcoin += totalcoin

def jackpot(yourcoin) :
    coin=yourcoin
    print("SELAMAT DATANG DI JACKPOT 888!!!")
    print("ANDA DAPAT MENDAPATKAN GORLOCK THE DESTROYER DENGAN HARGA 400 COIN")
    print("APAKAH ANDA INGIN MENCOBA KEBERUNTUNGAN ANDA???")
    while True :
        inp = input("(Y/N)----->")
        if inp == 'Y' :
            confirm = input("APAKAH ANDA YAKIN? (Y/N) :")
            if confirm == 'Y' :
                if coin >= 400 :
                    gacha(yourcoin)
                    coin-=400
                else :
                    print("COIN TIDAK CUKUP")
            else :
                print("OK")