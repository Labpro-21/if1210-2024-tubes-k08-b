from src.monsterManagement import cekint
itemID = ["Type", "Healing Potion", "Resilience Potion", "Strength Potion", "Monster Ball"]

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
        shopInterface()  #tampilkan kasir
        print()
        while True:
            pilihMenu = input(">>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")
            if pilihMenu.lower() == "lihat":
                lihat_pilih = input(">>> Mau lihat apa? (monster/item): ")
                while lihat_pilih != "monster" and lihat_pilih != "item":
                    lihat_pilih = input(">>> Pilih antara monster/item: ")  #jika input bukan monster/item
                if lihat_pilih == "monster":
                    print("ID | Type\t| ATK Power\t| DEF Power\t| HP\t| Stok\t| Harga")
                    for i in range(1,len(monstershop)): # Menampilkan setiap monster yang tersedia di Shop
                        idMonsterLihat=int(monstershop[i][0])
                        print(f"{monsterdata[idMonsterLihat][0]}  | {monsterdata[idMonsterLihat][1]}\t| {monsterdata[idMonsterLihat][2]}\t\t| {monsterdata[idMonsterLihat][3]}\t\t| {monsterdata[idMonsterLihat][4]}\t| {monstershop[i][1]}\t| {monstershop[i][2]}")
                elif lihat_pilih == "item":
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

            elif pilihMenu.lower() == "tambah":
                idMonsterShop = []
                for i in range(1,len(monstershop)):
                    idMonsterShop.append(monstershop[i][0])   #membuat list yg berisi semua id monster yg terdapat dishop
                idMonsterData = []
                for i in range(1,len(monsterdata)):
                    idMonsterData.append(monsterdata[i][0])    #membuat list yg berisi semua id monster yg terdapat dimonster data
                tambah_pilih = input("Mau tambah apa? (monster/item): ")
                while tambah_pilih != "monster" and tambah_pilih != "item":
                    tambah_pilih = (input(">>> Pilih antara monster/item: "))
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
                    #validasi kevalidan id
                    while idMonsterTambah in idMonsterShop or idMonsterTambah not in idMonsterData:
                        if idMonsterTambah not in idMonsterData:  #jika id tidak ada pada data
                            print("ID tidak valid! Pilih ID yang terdapat pada tabel!")
                            idMonsterTambah = (input(">>> Masukkan id monster: "))
                        elif idMonsterTambah in idMonsterShop:  #jika id sudah ada dishop
                            print("Monster sudah ada di Shop!")
                            idMonsterTambah = (input(">>> Masukkan id monster: "))
                    stokMonsterTambah = (input(">>> Masukkan stok awal: "))
                    while cekint(stokMonsterTambah) == False : #validasi integer
                        print("masukkan integer yg benar")
                        stokMonsterTambah = (input("Masukkan stok awal: "))
                    hargaMonsterTambah = (input(">>> Masukkan harga: "))
                    while cekint(hargaMonsterTambah) == False :  #validasi integer
                        print("masukkan integer yg benar")
                        hargaMonsterTambah = (input("Masukkan harga : "))
                    addMonsterShop = [idMonsterTambah,str(stokMonsterTambah),str(hargaMonsterTambah)]
                    monstershop.append(addMonsterShop)
                    print(f"{monsterdata[int(idMonsterTambah)][1]} telah berhasil ditambahkan ke dalam Shop!")
                elif tambah_pilih == "item":
                    if len(potionShop)!=5 :  #jika itemshop tidak keisi semua
                        print("ID | Type")
                    potionFound = False
                    countFalse = 0
                    for i in range(1,5):
                        for j in range(1,len(potionShop)):
                            if itemID[i] in potionShop[j][0]:
                                potionFound = True
                                break
                            else:
                                potionFound = False
                                continue
                        if potionFound == False:
                            print(f"{i}  | {itemID[i]}")   #menampilkan seluruh item yg tidak ada dishop
                            countFalse += 1
                    if countFalse == 0:   
                        print("Semua Item sudah tersedia pada Shop!")
                        print()
                    else:
                        while True :
                            iditemTambah = (input(">>> Masukkan id item (1-4): "))
                            #validasi integer
                            if cekint(iditemTambah) == False :
                                print("Masukkan integer yang benar")
                                continue
                            #validasi jika id<1 atau>4
                            if (int(iditemTambah) < 1 or int(iditemTambah) > 4):
                                print("id tidak valid!")
                                continue
                            sudahadadishop = True
                            #validasi jika id sudah ada dishop
                            for i in potionShop :
                                if itemID[int(iditemTambah)]==i[0] :
                                    print("Item sudah terdapat di shop")
                                    break
                            else :
                                sudahadadishop =False
                            if sudahadadishop == True :
                                continue                            
                            break
                        stokPotionTambah = (input("Masukkan stok awal: "))
                        #validasi integer
                        while cekint(stokPotionTambah) == False :
                            print("masukkan integer yg benar")
                            stokPotionTambah = (input("Masukkan stok awal: "))
                        hargaPotionTambah = (input("Masukkan harga: "))
                        #validasi integer
                        while cekint(hargaPotionTambah) == False :
                            print("masukkan integer yg benar")
                            hargaPotionTambah = (input("Masukkan harga :"))
                        newPotion = [itemID[int(iditemTambah)],str(stokPotionTambah),str(hargaPotionTambah)]
                        potionShop.append(newPotion)
                        print(f"{itemID[int(iditemTambah)]} telah berhasil ditambahkan ke dalam Shop!")
                        print()

            elif pilihMenu.lower() == "ubah":
                ubah_pilih = input("Mau ubah apa? (monster/item): ")
                while ubah_pilih != "monster" and ubah_pilih != "item":
                    ubah_pilih = (input(">>> Pilih antara monster/item: "))
                if ubah_pilih == "monster":
                    while True :
                        idMonsterUbah = (input(">>> Masukkan id monster: ")) 
                        #validasi apakah id terdapat dishop
                        for i in monstershop :
                            if idMonsterUbah== i[0] :
                                break
                        else :
                            print('ID tersebut tidak tersedia')
                            continue
                        stokMonsterBaru = (input(">>> Masukkan stok baru: "))
                        #validasi integer
                        while cekint(stokMonsterBaru)== False and stokMonsterBaru!="" :
                            print("Masukkan integer yg benar")
                            stokMonsterBaru = input('Masukkan stok baru:')
                        hargaMonsterBaru = (input(">>> Masukkan harga baru: "))
                        #validasi integer
                        while cekint(hargaMonsterBaru)== False and hargaMonsterBaru!="" :
                            print("Masukkan integer yg benar")
                            hargaMonsterBaru = input('Masukkan stok baru:')
                        pesanUbah = f"{monsterdata[int(idMonsterUbah)][1]} telah berhasil diubah "
                        if (stokMonsterBaru != ""):  #jika stok berubah
                            pesanUbah += f"dengan stok baru sejumlah {int(stokMonsterBaru)}"
                            for i in range(len(monstershop)) :
                                if monstershop[i][0]==(idMonsterUbah) :
                                    monstershop[i][1]=str(stokMonsterBaru)
                        if (stokMonsterBaru != "") and (hargaMonsterBaru != ""):
                            pesanUbah += " dan "
                        if (hargaMonsterBaru != ""): #jika harga berubah
                            pesanUbah += f"dengan harga baru {int(hargaMonsterBaru)}"
                            for i in range(len(monstershop)) :
                                if monstershop[i][0]==(idMonsterUbah) :
                                    monstershop[i][2]=str(hargaMonsterBaru)
                        pesanUbah += "!"
                        print(pesanUbah)
                        break
                elif ubah_pilih == "item":
                    while True :
                        iditemUbah = input(">>> Masukkan id item: ")
                        #validasi integer
                        if cekint(iditemUbah)==False :
                            print("Masukkan integer yang benar")
                            continue
                        #validasi apakah id <1 atau >4 
                        if int(iditemUbah) > 4 or int(iditemUbah) < 1 :
                            print("Id tersebut tidak tersedia")
                            continue
                        #validasi apakah id tersebut terdapat dishop atau tidak
                        for i in potionShop:
                            if itemID[int(iditemUbah)]==i[0] :
                                break
                        else :
                            print("Id tersebut tidak tersedia")
                            continue
                        stokitemBaru = ((input(">>> Masukkan stok baru: ")))
                        #validasi integer
                        while cekint(stokitemBaru)== False and stokitemBaru!="":
                            print("Masukkan integer yg benar")
                            stokitemBaru = input('Masukkan stok baru:')
                        hargaitemBaru = ((input(">>> Masukkan harga baru: ")))
                        #validasi integer
                        while cekint(hargaitemBaru)== False and hargaitemBaru!="":
                            print("Masukkan integer yg benar")
                            hargaitemBaru = input('Masukkan harga baru:')
                        pesanUbah = f"{itemID[int(iditemUbah)]} telah berhasil diubah "
                        if (stokitemBaru != ""): #jika stok berubah
                            for i in range(len(potionShop)) :
                                if potionShop[i][0] == itemID[int(iditemUbah)]  :
                                    potionShop[i][1]=str(stokitemBaru)
                            pesanUbah += f"dengan stok baru sejumlah {stokitemBaru}"
                        if (stokitemBaru != "") and (hargaitemBaru != ""):
                            pesanUbah += " dan "
                        if (hargaitemBaru != ""): #jika harga berubah
                            for i in range(len(potionShop)) :
                                if potionShop[i][0] == itemID[int(iditemUbah)]  :
                                    potionShop[i][2]=str(hargaitemBaru)
                            pesanUbah += f"dengan harga baru {hargaitemBaru}"
                        pesanUbah += "!"
                        print(pesanUbah)
                        break

            elif pilihMenu.lower() == "hapus":
                hapusPilih = input(">>> Mau hapus apa? (monster/item): ")
                while hapusPilih != "monster" and hapusPilih != "item":
                    hapusPilih = (input(">>> Pilih antara monster/item: "))
                if hapusPilih.lower() == "monster":
                    while True :
                        idMonsterHapus = (input(">>> Masukkan id monster: "))
                        #validasi apakah id tersebut terdapat dishop atau tidak
                        for i in monstershop :
                            if idMonsterHapus == i[0] :
                                break
                        else :
                            print("Id tersebut tidak tersedia")
                            continue
                        idMonsterHapus=int(idMonsterHapus)
                        while True :
                            yakinHapus = input(f"Apakah anda yakin ingin menghapus {monsterdata[idMonsterHapus][1]} dari Shop (y/n)? ")
                            if yakinHapus.lower() == "y":  #double check apakah benar ingin dihapus
                                newMonsterList = [['monster_id','stock','price']]
                                for i in range(1,len(monstershop)):
                                    if monstershop[i][0] == str(idMonsterHapus):
                                        continue
                                    else:
                                        newMonsterList.append(monstershop[i])
                                monstershop = newMonsterList
                                print(f"{monsterdata[idMonsterHapus][1]} telah berhasil dihapus dari Shop!")
                                break
                            elif yakinHapus.lower() =='n':
                                print("Penghapusan dibatalkan!")
                                print()
                                break
                            else :
                                print("Masukkan Y/N")
                        break
                elif hapusPilih.lower() == "item":
                    while True :
                        iditemHapus = (input(">>> Masukkan id item: "))
                        #validasi integer
                        if cekint(iditemHapus)==False :
                            print("Masukkan integer yang benar")
                            continue
                        #validasi apakah >4 atau <1
                        if int(iditemHapus) > 4 or int(iditemHapus) < 1 :
                            print("Id tersebut tidak tersedia")
                            continue
                        #validasi apakah id item terdapat dishop atau tidak
                        for i in potionShop:
                            if itemID[int(iditemHapus)]==i[0] :
                                break
                        else :
                            print("Id tersebut tidak tersedia")
                            continue
                        while True :
                            yakinHapus = input(f"Apakah anda yakin ingin menghapus {itemID[int(iditemHapus)]} dari Shop (y/n)? ")
                            if yakinHapus.lower() == "y": #double cek apakah ingin dihapus
                                newitemList = []
                                for i in range(len(potionShop)):
                                    if potionShop[i][0] == itemID[int(iditemHapus)]:
                                        continue
                                    else:
                                        newitemList.append(potionShop[i])
                                potionShop = newitemList
                                print(f"{itemID[int(iditemHapus)]} telah berhasil dihapus dari Shop!")
                                print()
                                break
                            elif yakinHapus.lower() =='n':
                                print("Penghapusan dibatalkan!")
                                print()
                                break
                            else :
                                print("masukkan (Y/N)")
                        break

            elif pilihMenu.lower() == 'keluar': # pilihMenu == "keluar"
                print("Sampai bertemu lagi Admin!")
                return monstershop,potionShop
            else : #jika aksi bukan tambah hapus ubah lihat dan keluar
                print("aski tidak diketahui")