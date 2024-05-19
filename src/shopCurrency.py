from monsterManagement import cekint
potionID = ["Type", "Healing Potion", "Resilience Potion", "Strength Potion", "Monster Ball"]

#FUNGSI UNTUK MENYUSUN LIST POTION SHOP
def sortPotion(potionShop):
    if potionShop[1][0] == "Resilience Potion":
            potionShop[1][0],potionShop[2][0] = potionShop[2][0],potionShop[1][0]
    if potionShop[3][0] == "Resilience Potion":
            potionShop[3][0],potionShop[2][0] = potionShop[2][0],potionShop[3][0]
    if potionShop[4][0] == "Resilience Potion":
            potionShop[4][0],potionShop[2][0] = potionShop[2][0],potionShop[4][0]
    if potionShop[1][0] == "Strength Potion":
            potionShop[1][0],potionShop[3][0] = potionShop[3][0],potionShop[1][0]
    if potionShop[4][0] == "Strength Potion":
            potionShop[4][0],potionShop[3][0] = potionShop[3][0],potionShop[4][0]
    if potionShop[1][0] == "Monster Ball":
            potionShop[1][0],potionShop[4][0] = potionShop[4][0],potionShop[1][0]
    return potionShop

#TAMPILAN KASIR
def shopInterface():
    print(" ▀▄▀▄▀▄  SHOP  ▄▀▄▀▄▀    ▂███████▂   _____  ")
    print(" |__∆|___|_∆_|_|_|∆|      ██ █ ██    |$___|  ")
    print(" |___|__∆|___|_|∆|_|     ███▀▀▀███   __||_   ")
    print(" |∆__|___|∆__|∆|_|_|      ███████   /_____\  ")
    print(" |___|_∆_|___|_|∆|_|  ██████████████ KASIR ██")
    print(" ===================  ███████████████████████")
    return

def shopOpen(role,potionShop,coin,userinventory,monsterdata,monstershop,yourmonsterdata,monsterinventory):
    yourcoin = coin
    if role == "agent": #jika role agent
        print("    ↤↤↤↤↤ SELAMAT DATANG DI SHOP!!! ↦↦↦↦↦")
        print()
        shopInterface()  #tampilkan kasir 
        print()
        while True:
            pilihMenu = input(">>> Pilih aksi (lihat/beli/keluar): ")
            if pilihMenu.lower() == "lihat":
                lihat_pilih = input(">>> Mau lihat apa? (monster/item): ")
                lihatSelesai = False
                while lihat_pilih != "monster" and lihat_pilih != "item":
                    lihat_pilih = input(">>> Pilih antara monster/item: ") #jika input bukan monster/item
                if lihat_pilih.lower() == "monster" :
                    print("ID | Type\t| ATK Power\t| DEF Power\t| HP\t| Stok\t| Harga")
                    for i in range(1,len(monstershop)): # Menampilkan setiap monster yang tersedia di Shop
                        idMonsterLihat=int(monstershop[i][0])
                        print(f"{monsterdata[idMonsterLihat][0]}  | {monsterdata[idMonsterLihat][1]}\t| {monsterdata[idMonsterLihat][2]}\t\t| {monsterdata[idMonsterLihat][3]}\t\t| {monsterdata[idMonsterLihat][4]}\t| {monstershop[i][1]}\t| {monstershop[i][2]}")
                elif lihat_pilih.lower() == "item":
                    print("ID | Type\t\t| Stok\t| Harga")
                    for i in range(1,len(potionShop)): # Menampilkan setiap potion yang tersedia di Shop
                        if potionShop[i][0] == "Healing Potion":
                            idPotion = 1
                        elif potionShop[i][0] == "Resilience Potion":
                            idPotion = 2
                        elif potionShop[i][0] == "Strength Potion":
                            idPotion = 3
                        elif potionShop[i][0] == "Monster Ball":
                            idPotion = 4
                        print(f"{idPotion}  | {potionShop[i][0]}\t| {potionShop[i][1]}\t| {potionShop[i][2]}")
                    lihatSelesai == True
            elif pilihMenu.lower() == "beli":
                print(f"Jumlah O.W.C.A Coin-mu sekarang {yourcoin}.")
                print()
                beliType = input(">>> Mau beli apa? (monster/item): ")
                while beliType.lower() != "monster" and beliType.lower() != "item":
                    beliType = input(">>> Pilih antara monster/item: ") #jika input bukan monster/item
                if beliType.lower() == "monster":
                    while True:
                        transactionStatus = 0
                        idMonsterBeli = (input(">>> Masukkan id monster: "))
                        #validasi input
                        for i in monstershop :
                            if idMonsterBeli== i[0] : #jika id monster terdapat dishop
                                break
                        else :
                            print("Id monster tersebut tidak tersedia")  #jika id tidak ada dishop
                            continue
                        idMonsterBeli = int(idMonsterBeli)
                        for i in yourmonsterdata :  #cek jika monster tersebut sudah dimiliki
                            if monsterdata[idMonsterBeli][1] == i[1] :
                                print("Monster sudah dimiliki")
                                break
                        else : #jika belum
                            for i in monstershop :
                                if i[0]==str(idMonsterBeli) :
                                    if yourcoin >= int(i[2]) : #jika coin cukup untuk membeli
                                        print("monster berhasil ditambahkan")
                                        yourcoin -= int(i[2])
                                        yourmonsterdata.append([userinventory[0][0],monsterdata[idMonsterBeli][1],'1'])
                                        monsterinventory.append([userinventory[0][0],monsterdata[idMonsterBeli][1],'1'])
                                        monsterShopLocation = 0
                                        for i in monstershop : #stok berkurang satu (dimasukkan ke list monstershop)
                                            if i[0]==str(idMonsterBeli) :
                                                monstershop[monsterShopLocation][1] = str(int(monstershop[monsterShopLocation][1])-1)
                                                break
                                            monsterShopLocation += 1
                                        transactionStatus = 1
                                        break
                                    else : #jika coin tidak cukup
                                        print("Maaf O.W.C.A. Coin-mu kurang.")
                                        break
                        if transactionStatus == 1 : #jika transaski sukses
                            break
                    print()
                elif beliType.lower() == "item": 
                    while True :
                        idPotion = (input(">>> Masukkan id item: "))
                        #validasi input id
                        for i in range(1,5) :
                            if idPotion == str(i) : #jika idinput == 1/2/3/4
                                break
                        else :
                            print("Id tersebut tidak tersedia") #jika idinput selain 1/2/3/4
                            continue
                        idPotion=int(idPotion)
                        while True :
                            jumlahPotionBeli = (input(">>> Masukkan jumlah: "))
                            if cekint(jumlahPotionBeli) : #jika input adalah integer
                                if int(potionShop[idPotion][1]) >0 : #jika stok tersedia
                                    jumlahPotionBeli=int(jumlahPotionBeli)
                                    if jumlahPotionBeli>int(potionShop[idPotion][1]):
                                        print("Stock tidak cukup") #jika jumlah yg dibeli melebihi stok
                                    else : 
                                        if yourcoin >= (jumlahPotionBeli * int(potionShop[idPotion][2])): #jika coinmu cukup
                                            print(f"Berhasil membeli item: {jumlahPotionBeli} {potionShop[idPotion][0]}. Item sudah masuk ke inventory-mu!")
                                            print()
                                            userinventory[idPotion-1][2]=str(int(userinventory[idPotion-1][2])+jumlahPotionBeli)
                                            yourcoin-=(jumlahPotionBeli * int(potionShop[idPotion][2]))
                                            #stok berkurang satu
                                            potionShop[idPotion][1]=str(int(potionShop[idPotion][1])-jumlahPotionBeli)
                                            break
                                        else : #jika coinmu kurang
                                            print("Maaf O.W.C.A Coin-mu kurang.")
                                            break
                                else : #jika stok habis
                                    print("Stock Potion habis!")
                                    break
                            else : #jika input bukan integer
                                print("Tolong masukkan integer yang benar")
                        break
            elif pilihMenu.lower()=="keluar": # pilihMenu == "keluar"
                print(f"Sampai bertemu lagi, User!")
                return yourcoin
            else :
                print("Aksi tidak diketahui")
    else :
        print("anda tidak memiliki akses")
def shopmanagement(potionShop,monstershop,monsterdata)   :
        print("   ↤↤↤↤ SELAMAT DATANG KEMBALI ADMIN! ↦↦↦↦")
        print()
        shopInterface()
        print()
        while True:
            pilihMenu = input(">>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")
            if pilihMenu == "lihat":
                lihat_pilih = input(">>> Mau lihat apa? (monster/potion): ")
                while lihat_pilih != "monster" and lihat_pilih != "potion":
                    lihat_pilih = input(">>> Pilih antara monster/potion: ")
                if lihat_pilih == "monster":
                    print("ID | Type\t| ATK Power\t| DEF Power\t| HP\t| Stok\t| Harga")
                    for i in range(1,len(monstershop)): # Menampilkan setiap monster yang tersedia di Shop
                        idMonsterLihat=int(monstershop[i][0])
                        print(f"{monsterdata[idMonsterLihat][0]}  | {monsterdata[idMonsterLihat][1]}\t| {monsterdata[idMonsterLihat][2]}\t\t| {monsterdata[idMonsterLihat][3]}\t\t| {monsterdata[idMonsterLihat][4]}\t| {monstershop[i][1]}\t| {monstershop[i][2]}")
                elif lihat_pilih == "potion":
                    print("ID | Type\t\t| Stok\t| Harga")
                    for i in range(1,len(potionShop)): # Menampilkan setiap potion yang tersedia di Shop
                        if potionShop[i][0] == "Healing Potion":
                            idPotion = 1
                        elif potionShop[i][0] == "Resilience Potion":
                            idPotion = 2
                        elif potionShop[i][0] == "Strength Potion":
                            idPotion = 3
                        elif potionShop[i][0] == "Monster Ball":
                            idPotion = 4
                        print(f"{idPotion}  | {potionShop[i][0]}\t| {potionShop[i][1]}\t| {potionShop[i][2]}")

            elif pilihMenu == "tambah":
                idMonsterShop = []
                for i in range(1,len(monstershop)):
                    idMonsterShop.append(monstershop[i][0])
                idMonsterData = []
                for i in range(1,len(monsterdata)):
                    idMonsterData.append(monsterdata[i][0])
                tambah_pilih = input("Mau tambah apa? (monster/potion): ")
                while tambah_pilih != "monster" and tambah_pilih != "potion":
                    tambah_pilih = (input(">>> Pilih antara monster/potion: "))
                if tambah_pilih == "monster":
                    print("ID | Type\t\t| ATK Power\t| DEF Power\t| HP\t|")
                    for i in range(1,len(monsterdata)): # Menampilkan setiap monster yang tersedia di Shop
                        if monsterdata[i][0] in idMonsterShop:
                            continue
                        else:
                            idMonsterLihat=int(monsterdata[i][0])
                            print(f"{i}  | {monsterdata[idMonsterLihat][1]}\t\t| {monsterdata[idMonsterLihat][2]}\t\t| {monsterdata[idMonsterLihat][3]}\t\t| {monsterdata[idMonsterLihat][4]}\t|")
                    print()
                    idMonsterTambah = input(">>> Masukkan id monster: ")
                    while idMonsterTambah in idMonsterShop or idMonsterTambah not in idMonsterData:
                        if idMonsterTambah not in idMonsterData:
                            print("ID tidak valid! Pilih ID yang terdapat pada tabel!")
                            idMonsterTambah = (input(">>> Masukkan id monster: "))
                        elif idMonsterTambah in idMonsterShop:
                            print("Monster sudah ada di Shop!")
                            idMonsterTambah = (input(">>> Masukkan id monster: "))
                    stokMonsterTambah = int(input(">>> Masukkan stok awal: "))
                    hargaMonsterTambah = int(input(">>> Masukkan harga: "))
                    addMonsterShop = [idMonsterTambah,str(stokMonsterTambah),str(hargaMonsterTambah)]
                    monstershop.append(addMonsterShop)
                    print(f"{monsterdata[int(idMonsterTambah)][1]} telah berhasil ditambahkan ke dalam Shop!")
                elif tambah_pilih == "potion":
                    potionFound = False
                    countFalse = 0
                    print("ID | Type")
                    for i in range(1,4):
                        for j in range(1,len(potionShop)):
                            if potionID[i] in potionShop[j][0]:
                                potionFound = True
                                break
                            else:
                                potionFound = False
                                continue
                        if potionFound == False:
                            print(f"{i}  | {potionID[i]}")
                            countFalse += 1
                    if countFalse == 0:
                        print("Semua Potion sudah tersedia pada Shop!")
                        print()
                    else:
                        idPotionTambah = int(input(">>> Masukkan id potion (1-4): "))
                        while (idPotionTambah < 1 or idPotionTambah > 4):
                            print("id tidak valid!")
                            idPotionTambah = int(input(">>> Masukkan id potion (1-4): "))
                        stokPotionTambah = int(input("Masukkan stok awal: "))
                        hargaPotionTambah = int(input("Masukkan harga: "))
                        newPotion = [potionID[idPotionTambah],str(stokPotionTambah),str(hargaPotionTambah)]
                        potionShop.append(newPotion)
                        sortPotion(potionShop)
                        print(f"{potionID[idPotionTambah]} telah berhasil ditambahkan ke dalam Shop!")
                        print()

            elif pilihMenu == "ubah":
                ubah_pilih = input("Mau ubah apa? (monster/potion): ")
                while ubah_pilih != "monster" and ubah_pilih != "potion":
                    ubah_pilih = (input(">>> Pilih antara monster/potion: "))
                if ubah_pilih == "monster":
                    idMonsterUbah = (input(">>> Masukkan id monster: ")) # Nanti nambahin validasi
                    stokMonsterBaru = (input(">>> Masukkan stok baru: "))
                    hargaMonsterBaru = (input(">>> Masukkan harga baru: "))
                    pesanUbah = f"{monsterdata[int(idMonsterUbah)][1]} telah berhasil diubah "
                    if (stokMonsterBaru != ""):
                        pesanUbah += f"dengan stok baru sejumlah {int(stokMonsterBaru)}"
                        for i in range(len(monstershop)) :
                            if monstershop[i][0]==(idMonsterUbah) :
                                monstershop[i][1]=str(stokMonsterBaru)
                    if (stokMonsterBaru != "") and (hargaMonsterBaru != ""):
                        pesanUbah += " dan "
                    if (hargaMonsterBaru != ""):
                        pesanUbah += f"dengan harga baru {int(hargaMonsterBaru)}"
                        for i in range(len(monstershop)) :
                            if monstershop[i][0]==(idMonsterUbah) :
                                monstershop[i][2]=str(hargaMonsterBaru)
                    pesanUbah += "!"
                    print(pesanUbah)
                elif ubah_pilih == "potion":
                    idPotionUbah = int((input(">>> Masukkan id potion: ")))
                    while idPotionUbah < 1 or idPotionUbah > 4:
                        print("ID tidak valid!")
                        idPotionUbah = int((input(">>> Masukkan id potion: ")))
                    stokPotionBaru = int((input(">>> Masukkan stok baru: ")))
                    hargaPotionBaru = int((input(">>> Masukkan harga baru: ")))
                    pesanUbah = f"{potionID[int(idPotionUbah)]} telah berhasil diubah "
                    if (stokPotionBaru != ""):
                        pesanUbah += f"dengan stok baru sejumlah {stokPotionBaru}"
                    if (stokPotionBaru != "") and (hargaPotionBaru != ""):
                        pesanUbah += " dan "
                    if (hargaPotionBaru != ""):
                        pesanUbah += f"dengan harga baru {hargaPotionBaru}"
                    pesanUbah += "!"
                    for i in range(1,len(potionShop)):
                        if potionShop[i][0] == potionID[idPotionUbah]:
                            potionShop[i] = [potionID[idPotionUbah],stokPotionBaru,hargaPotionBaru]
                        else:
                            continue
                    print(pesanUbah)
                    print()

            elif pilihMenu == "hapus":
                hapusPilih = input(">>> Mau hapus apa? (monster/potion): ")
                while hapusPilih != "monster" and hapusPilih != "potion":
                    hapusPilih = (input(">>> Pilih antara monster/potion: "))
                if hapusPilih == "monster":
                    idMonsterHapus = int(input(">>> Masukkan id monster: "))
                    idMonsterShop = []
                    for i in range(1,len(monstershop)):
                        idMonsterShop.append(monstershop[i][0])
                    idMonsterData = []
                    for i in range(1,len(monsterdata)):
                        idMonsterData.append(monsterdata[i][0])
                    if str(idMonsterHapus) not in idMonsterShop:
                        print("Monster dengan ID tersebut tidak ada pada Shop!")
                        idMonsterHapus = int(input(">>> Masukkan id monster: "))
                    
                    yakinHapus = input(f"Apakah anda yakin ingin menghapus {monsterdata[idMonsterHapus][1]} dari Shop (y/n)? ")
                    if yakinHapus == "y":
                        newMonsterList = [['monster_id','stock','price']]
                        for i in range(1,len(monstershop)):
                            if monstershop[i][0] == str(idMonsterHapus):
                                continue
                            else:
                                newMonsterList.append(monstershop[i])
                        monstershop = newMonsterList
                        print(f"{monsterdata[idMonsterHapus][1]} telah berhasil dihapus dari Shop!")
                    else:
                        print("Penghapusan dibatalkan!")
                        print()
                        continue
                elif hapusPilih == "potion":
                    idPotionHapus = int(input(">>> Masukkan id potion: "))
                    yakinHapus = input(f"Apakah anda yakin ingin menghapus {potionID[idPotionHapus]} dari Shop (y/n)? ")
                    if yakinHapus == "y":
                        print(potionShop)
                        newPotionList = []
                        for i in range(len(potionShop)):
                            if potionShop[i][0] == potionID[idPotionHapus]:
                                continue
                            else:
                                newPotionList.append(potionShop[i])
                                print(newPotionList)
                        potionShop = newPotionList
                        print(potionShop)
                        print(f"{potionID[int(idPotionHapus)]} telah berhasil dihapus dari Shop!")
                        print()
                    else:
                        print("Penghapusan dibatalkan!")
                        print()
                        continue

            else: # pilihMenu == "keluar"
                print("Sampai bertemu lagi Admin!")
                return monstershop,potionShop

# shopOpen("agent")
# shopOpen("admin")