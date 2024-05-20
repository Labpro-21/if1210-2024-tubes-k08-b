import time
from src.RandomNumberGenerator import RNG

# fungsi prob untuk menghasilkan kemungkinan muncul masing-masing item
def prob(RNG):
    if 1 <= RNG <= 40:
        return 0
    elif 41 <= RNG <= 65:
        return 1
    elif 66 <= RNG <= 80:
        return 2
    elif 81 <= RNG <= 95:
        return 3
    elif 96 <= RNG <= 100:
        return 4

# fungsi gacha untuk mengimplementasi probabilitas acak untuk mendapat reward
def gacha(id, coin, monsInv, yourMonsInv):
    icon = ['TOPI', 'PEDANG', 'BAJU', 'CELANA', 'JAM']  
    iconValue = [60, 80, 120, 170, 300]                  # menunjukkan value masing-masing icon sesuai dengan index array icon secara berurut
    RNG1 = RNG(1, 100)                                   # memberi range RNG masing-masing item
    time.sleep(0.2)                                      # men-delay waktu karena RNG yang digunakan berdasar time
    RNG2 = RNG(1, 100)
    time.sleep(0.1)                               
    RNG3 = RNG(1, 100)
    
    indexItem1 = prob(RNG1)                               
    indexItem2 = prob(RNG2)
    indexItem3 = prob(RNG3)
    totalcoin = iconValue[indexItem1] + iconValue[indexItem2] + iconValue[indexItem3]
    print("==========================")
    print(f"{icon[indexItem1]} | {icon[indexItem2]} | {icon[indexItem3]}")
    print("==========================")

    if indexItem1 == indexItem2 and indexItem2 == indexItem3:
        print('JACKPOT!! ANDA MENDAPATKAN GORLOCK THE DESTROYER! DESTROY EVERYTHING!')
        if any(item[1] == "Gorlock" for item in monsInv):
            print('GORLOCK SUDAH ANDA MILIKI, GORLOCK AKAN DIUBAH KE O.W.C.A Coin sebanyak 2000 Coin')
            coin += 2000
        else:
            monsInv.append([str(id),"Gorlock",'1'])                                      # append Gorlock ke list monsterInventory
            yourMonsInv.append([str(id),"Gorlock",'1'])                                  # append Gorlock ke list yourMonsterInventory
    else:
        print(f"ANDA TIDAK DAPAT JACKPOT, TAPI ANDA DAPAT {totalcoin} COIN !!!")
        coin  += totalcoin
    return coin

# fungsi jackpot untuk menjalankan program jackpot
def jackpot(id, coin,  monsInv , yourMonsInv):
    coin  = int(coin) 
    print("SELAMAT DATANG DI JACKPOT 888!!!")
    print("ANDA DAPAT MENDAPATKAN GORLOCK THE DESTROYER DENGAN HARGA 500 COIN")
    print(f"COIN ANDA SAAT INI SEJUMLAH {coin} ")
    print("APAKAH ANDA INGIN MENCOBA KEBERUNTUNGAN ANDA???")

    while True:
        inp = input("(Y/N)----->").lower()
        if inp == 'y':
            confirm = input("APAKAH ANDA YAKIN? (Y/N) :").lower()
            if confirm == 'y':
                if coin  >= 500:
                    coin  = gacha(id, coin,  monsInv, yourMonsInv)
                    coin  -= 500
                    print(f'COIN ANDA TERSISA {coin} ')
                    print("APAKAH ANDA INGIN MELANJUTKAN??", end=" ")
                else:
                    print("YAH COIN ANDA TIDAK CUKUP")
                    print("SILAKAN COBA JACKPOT DI WAKTU LAIN")
                    break
            elif confirm == 'n':
                return coin
            else:
                print("Masukkan input yang benar")
        elif inp == 'n':
            return coin
        else:
            print("Masukkan input yang benar")