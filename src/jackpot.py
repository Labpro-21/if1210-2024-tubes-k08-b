import time
from RandomNumberGenerator import RNG

def cekrng(RNG):
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

def gacha(id, yourcoin,monsInv,yourmonsterinventory):
    icon = ['TOPI', 'PEDANG', 'BAJU', 'CELANA', 'JAM']
    value = [30, 60, 80, 120, 170, 300]
    RNG1 = RNG(1, 100)
    time.sleep(0.2)
    RNG2 = RNG(1, 100)
    time.sleep(0.1)
    RNG3 = RNG(1, 100)

    item1 = 1
    item2 = 1
    item3 = 1
    totalcoin = value[item1] + value[item2] + value[item3]

    print(f"{icon[item1]} | {icon[item2]} | {icon[item3]}")

    if item1 == item2 and item2 == item3:
        print('SELAMAT!! ANDA MENDAPATKAN GORLOCK THE DESTROYER! DESTROY EVERYTHING!')
        if any(item[1] == "Gorlock" for item in monsInv):
            print('SELAMAT!! GORLOCK SUDAH ANDA MILIKI, GORLOCK AKAN DIUBAH KE O.W.C.A Coin sebanyak 1000 Coin')
            yourcoin += 1000
        else:
            monsInv.append([str(id),"Gorlock",'1'])
            yourmonsterinventory.append([str(id),"Gorlock",'1'])
    else:
        print(f"ANDA TIDAK DAPAT JACKPOT, TAPI ANDA DAPAT {totalcoin} COIN !!!")
        yourcoin += totalcoin

    return yourcoin

def jackpot(id, yourcoin, monsInv,yourmonsterinventory):
    yourcoin = int(yourcoin)
    print("SELAMAT DATANG DI JACKPOT 888!!!")
    print("ANDA DAPAT MENDAPATKAN GORLOCK THE DESTROYER DENGAN HARGA 500 COIN")
    print(f"COIN ANDA SAAT INI SEJUMLAH {yourcoin}")
    print("APAKAH ANDA INGIN MENCOBA KEBERUNTUNGAN ANDA???")

    while True:
        inp = input("(Y/N)----->").lower()
        if inp == 'y':
            confirm = input("APAKAH ANDA YAKIN? (Y/N) :").lower()
            if confirm == 'y':
                if yourcoin >= 500:
                    yourcoin = gacha(id, yourcoin, monsInv,yourmonsterinventory)
                    yourcoin -= 500
                    print(f'COIN ANDA TERSISA {yourcoin}')
                    print("APAKAH ANDA INGIN MELANJUTKAN??", end=" ")
                else:
                    print("YAH COIN ANDA TIDAK CUKUP")
                    print("SILAKAN COBA JACKPOT DI WAKTU LAIN")
                    break
            elif confirm == 'n':
                break
            else:
                print("Masukkan input yang benar")
        elif inp == 'n':
            break
        else:
            print("Masukkan input yang benar")
