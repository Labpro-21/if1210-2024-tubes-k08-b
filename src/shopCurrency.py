from csvParser import csvRead, csvWrite, csvOverwrite, csvDelete, csvWriteAll
pathItemShop = "C:\if1210-2024-tubes-k08-b\data\item_shop.csv"
potionList = csvRead(pathItemShop)
potionID = ["Type", "Strength Potion", "Resilience Potion", "Healing Potion"]

def shopInterface():
    print(" ▀▄▀▄▀▄  SHOP  ▄▀▄▀▄▀    ▂███████▂   _____  ")
    print(" |__∆|___|_∆_|_|_|∆|      ██ █ ██    |$___|  ")
    print(" |___|__∆|___|_|∆|_|     ███▀▀▀███   __||_   ")
    print(" |∆__|___|∆__|∆|_|_|      ███████   /_____\  ")
    print(" |___|_∆_|___|_|∆|_|  ██████████████ KASIR ██")
    print(" ===================  ███████████████████████")
    return

def sortPotion(potionList):
    if potionList[1][0] == "Resilience Potion":
            potionList[1][0],potionList[2][0] = potionList[2][0],potionList[1][0]
    if potionList[3][0] == "Resilience Potion":
            potionList[3][0],potionList[2][0] = potionList[2][0],potionList[3][0]
    if potionList[1][0] == "Healing Potion":
            potionList[1][0],potionList[3][0] = potionList[3][0],potionList[1][0]
    return potionList

def listTocsv(list):
    new_csv = []
    csvCell = ""
    for i in range(len(list)):
        for j in range(len(list[1])):
            csvCell += f"{list[i][j]}"
            if j != len(list[1])-1:
                csvCell += f";"
            if i != len(list)-1 and j == len(list[1])-1:
                csvCell += "\n"
        new_csv.append(csvCell)
        csvCell = ""
    return new_csv

def shopOpen(role):
    global potionList
    if role == "agent":
        print("    ↤↤↤↤↤ SELAMAT DATANG DI SHOP!!! ↦↦↦↦↦")
        print()
        shopInterface()
        print()
    elif role == "admin":
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
                    print("monster")
                    # monster_list()
                elif lihat_pilih == "potion":
                    print("ID | Type\t\t| Stok\t| Harga")
                    for i in range(1,len(potionList)): # Menampilkan setiap potion yang tersedia di Shop
                        if potionList[i][0] == "Strength Potion":
                            idPotion = 1
                        elif potionList[i][0] == "Resilience Potion":
                            idPotion = 2
                        elif potionList[i][0] == "Healing Potion":
                            idPotion = 3
                        print(f"{idPotion}  | {potionList[i][0]}\t| {potionList[i][1]}\t| {potionList[i][2]}")

            elif pilihMenu == "tambah":
                tambah_pilih = input("Mau tambah apa? (monster/potion): ")
                while tambah_pilih != "monster" and tambah_pilih != "potion":
                    tambah_pilih = (input(">>> Pilih antara monster/potion: "))
                if tambah_pilih == "monster":
                    print("monster") # Nanti di sini list semua monster dari database yang belom ada di Shop
                    print()
                    idMonsterTambah = int(input(">>> Masukkan id monster: ")) # Nanti tambah validasi
                    stokMonsterTambah = int(input(">>> Masukkan stok awal: "))
                    hargaMonsterTambah = int(input(">>> Masukkan harga: "))
                    # monster_list.append()
                    print("[nama monster] telah berhasil ditambahkan ke dalam Shop!")
                elif tambah_pilih == "potion":
                    potionFound = False
                    countFalse = 0
                    print("ID | Type")
                    for i in range(1,4):
                        for j in range(1,len(potionList)):
                            if potionID[i] in potionList[j][0]:
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
                        idPotionTambah = int(input(">>> Masukkan id potion (1-3): "))
                        while (idPotionTambah < 1 or idPotionTambah > 3):
                            print("id tidak valid!")
                            idPotionTambah = int(input(">>> Masukkan id potion (1-3): "))
                        stokPotionTambah = int(input("Masukkan stok awal: "))
                        hargaPotionTambah = int(input("Masukkan harga: "))
                        newPotion = [potionID[idPotionTambah],stokPotionTambah,hargaPotionTambah]
                        potionList.append(newPotion)
                        sortPotion(potionList)
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
                    pesanUbah = f"[nama monster] telah berhasil diubah "
                    # komponenubah = f"{monsterList[int(idMonsterUbah)]};"
                    if (stokMonsterBaru != ""):
                        pesanUbah += f"dengan stok baru sejumlah {stokMonsterBaru}"
                        # komponenUbah += f"{stokMonsterBaru};"
                    # else:
                        # komponenUbah += f"{monsterList[int(idMonsterUbah)][1];}"
                    if (stokMonsterBaru != "") and (hargaMonsterBaru != ""):
                        pesanUbah += " dan "
                    if (hargaMonsterBaru != ""):
                        pesanUbah += f"dengan harga baru {hargaMonsterBaru}"
                        # komponenUbah += f"{hargaMonsterBaru}"
                    # else:
                        # komponenUbah += f"{monsterList[int(idMonsterUbah)][2]}"
                    pesanUbah += "!"
                    csvOverwrite(pathItemShop, int(idMonsterUbah)) # , komponenUbah (Nanti)
                    print(pesanUbah)
                elif ubah_pilih == "potion":
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
                    potionList[idPotionUbah] = [potionID[idPotionUbah],stokPotionBaru,hargaPotionBaru]
                    print(pesanUbah)
                    print()

            elif pilihMenu == "hapus":
                hapusPilih = input(">>> Mau hapus apa? (monster/potion): ")
                while hapusPilih != "monster" and hapusPilih != "potion":
                    hapusPilih = (input(">>> Pilih antara monster/potion: "))
                if hapusPilih == "monster":
                    idMonsterHapus = input(">>> Masukkan id monster: ")
                    # yakinHapus = input(f"Apakah anda yakin ingin menghapus {monsterList[int(idPokemonHapus)]} dari Shop (y/n)? )
                    # if yakinHapus == "y":
                        # csvDelete(pathItemShop, int(idMonsterHapus))
                        # print(f"{monsterList[int(idPokemonHapus)]} telah berhasil dihapus dari Shop!")
                    # else:
                        # continue
                elif hapusPilih == "potion":
                    idPotionHapus = int(input(">>> Masukkan id potion: "))
                    yakinHapus = input(f"Apakah anda yakin ingin menghapus {potionID[idPotionHapus]} dari Shop (y/n)? ")
                    if yakinHapus == "y":
                        newPotionList = []
                        for i in range(len(potionList)):
                            if i == idPotionHapus:
                                continue
                            else:
                                newPotionList.append(potionList[i])
                        potionList = newPotionList
                        print(f"{potionID[int(idPotionHapus)]} telah berhasil dihapus dari Shop!")
                        print()
                    else:
                        print("Penghapusan dibatalkan!")
                        print()
                        continue

            else: # pilihMenu == "keluar"
                print("Sampai bertemu lagi Admin!")
                csvWriteAll(pathItemShop,listTocsv(potionList))
                break
shopOpen("admin")