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

def shopOpen(role):
    if role == "agent":
        print("    ↤↤↤↤↤ SELAMAT DATANG DI SHOP!!! ↦↦↦↦↦")
        print()
        shopInterface()
        print()
        keluar = False
        while keluar != True:
            pilihMenu = input(">>> Pilih aksi (lihat/beli/keluar): ")
            if pilihMenu == "lihat":
                lihat_pilih = input(">>> Mau lihat apa? (monster/potion): ")
                lihatSelesai = False
                while lihat_pilih != "monster" and lihat_pilih != "potion" and lihatSelesai != True:
                    lihat_pilih = input(">>> Pilih antara monster/potion: ")
                if lihat_pilih == "monster":
                    print("monster")
                    lihatSelesai == True
                    # monster_list()
                elif lihat_pilih == "potion":
                    print("ID | Type\t\t| Stok\t| Harga")
                    for i in range(1,len(potionList)): # Menampilkan setiap potion yang tersedia di Shop
                        print(f"{i}  | {potionList[i][0]}\t| {potionList[i][1]}\t| {potionList[i][2]}")
                    lihatSelesai == True
            elif pilihMenu == "beli":
                print("Jumlah O.W.C.A Coin-mu sekarang [jumlah].")
                print()
                beliType = input(">>> Mau beli apa? (monster/potion): ")
                beliSelesai = False
                while beliType != "monster" and beliType != "potion" and beliSelesai != True:
                    beliType = input(">>> Pilih antara monster/potion: ")
                if beliType == "monster":
                    idMonsterBeli = input(">>> Masukkan id monster: ")
                    # if monster in inventory:
                    # print("[nama monster] sudah ada dalam inventory-mu! Pembelian dibatalkan.")
                    # if OWCA >= harga monster:
                    print("Berhasil membeli item: [nama monster]. Item sudah masuk ke inventory-mu!")
                    print()
                    beliSelesai == True
                    # Di sini ntar masukkin monster ke inventory, sama stok di toko ngurang 1 (harus ada database dulu), sama OWCA ngurang
                    # else:
                    # print("OC-mu tidak cukup.")
                elif beliType == "potion":
                    idPotionBeli = input(">>> Masukkan id potion: ")
                    jumlahPotionBeli = input(">>> Masukkan jumlah: ")
                    # if OWCA >= jumlah x potion:
                    print("Berhasil membeli item: [jumlah potion] [nama potion]. Item sudah masuk ke inventory-mu!")
                    print()
                    beliSelesai == True
            else: # pilihMenu == "keluar"
                keluar == True
                print("Terima kasih sudah berkunjung. Sampai bertemu lagi!")
                break
    elif role == "admin":
        print("   ↤↤↤↤ SELAMAT DATANG KEMBALI ADMIN! ↦↦↦↦")
        print()
        shopInterface()
        print()
        keluar = False
        while keluar != True:
            pilihMenu = input(">>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")
            if pilihMenu == "lihat":
                lihat_pilih = input(">>> Mau lihat apa? (monster/potion): ")
                lihatSelesai = False
                while lihat_pilih != "monster" and lihat_pilih != "potion" and lihatSelesai != True:
                    lihat_pilih = input(">>> Pilih antara monster/potion: ")
                if lihat_pilih == "monster":
                    print("monster")
                    lihatSelesai == True
                    # monster_list()
                elif lihat_pilih == "potion":
                    print("ID | Type\t\t| Stok\t| Harga")
                    for i in range(1,len(potionList)): # Menampilkan setiap potion yang tersedia di Shop
                        print(f"{i}  | {potionList[i][0]}\t| {potionList[i][1]}\t| {potionList[i][2]}")
                    lihatSelesai == True
            elif pilihMenu == "tambah":
                tambah_pilih = input("Mau tambah apa? (monster/potion): ")
                tambahSelesai = False
                while tambah_pilih != "monster" and tambah_pilih != "potion" and tambahSelesai != True:
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
                        csvWrite(pathItemShop, f"{potionID[idPotionTambah]};{stokPotionTambah};{hargaPotionTambah}")
                        print(f"{potionID[idPotionTambah]} telah berhasil ditambahkan ke dalam Shop!")
                        print()
            elif pilihMenu == "ubah":
                ubah_pilih = input("Mau ubah apa? (monster/potion): ")
                ubahSelesai = False
                while ubah_pilih != "monster" and ubah_pilih != "potion" and ubahSelesai != True:
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
                    idPotionUbah = (input(">>> Masukkan id potion: "))
                    stokPotionBaru = (input(">>> Masukkan stok baru: "))
                    hargaPotionBaru = (input(">>> Masukkan harga baru: "))
                    pesanUbah = f"{potionID[int(idPotionUbah)]} telah berhasil diubah "
                    komponenUbah = f"{potionID[int(idPotionUbah)]};"
                    if (stokPotionBaru != ""):
                        pesanUbah += f"dengan stok baru sejumlah {stokPotionBaru}"
                        komponenUbah += f"{stokPotionBaru};"
                    else:
                        komponenUbah += f"{potionList[int(idPotionUbah)][1]};"
                    if (stokPotionBaru != "") and (hargaPotionBaru != ""):
                        pesanUbah += " dan "
                    if (hargaPotionBaru != ""):
                        pesanUbah += f"dengan harga baru {hargaPotionBaru}"
                        komponenUbah += f"{hargaPotionBaru}"
                    else:
                        komponenUbah += f"{potionList[int(idPotionUbah)][2]}"
                    pesanUbah += "!"
                    csvDelete(pathItemShop, int(idPotionUbah), komponenUbah)
                    print(pesanUbah)
                    print()
            elif pilihMenu == "hapus":
                hapusPilih = input(">>> Mau hapus apa? (monster/potion): ")
                hapusSelesai = False
                while hapusPilih != "monster" and hapusPilih != "potion" and hapusSelesai != True:
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
                    idPotionHapus = input(">>> Masukkan id potion: ")
                    yakinHapus = input(f"Apakah anda yakin ingin menghapus {potionID[int(idPotionHapus)]} dari Shop (y/n)? ")
                    if yakinHapus == "y":
                        csvDelete(pathItemShop, int(idPotionHapus))
                        print(f"{potionID[int(idPotionHapus)]} telah berhasil dihapus dari Shop!")
                        print()
                    else:
                        print("Penghapusan dibatalkan!")
                        print()
                        continue
            else: # pilihMenu == "keluar"
                keluar == True
                print("Sampai bertemu lagi Admin!")
                break
    return

# shopOpen("agent")
shopOpen("admin")