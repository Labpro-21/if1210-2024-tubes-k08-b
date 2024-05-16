def shopInterface():
    print(" ▀▄▀▄▀▄  SHOP  ▄▀▄▀▄▀    ▂███████▂   _____  ")
    print(" |__∆|___|_∆_|_|_|∆|      ██ █ ██    |$___|  ")
    print(" |___|__∆|___|_|∆|_|     ███▀▀▀███   __||_   ")
    print(" |∆__|___|∆__|∆|_|_|      ███████   /_____\  ")
    print(" |___|_∆_|___|_|∆|_|  ██████████████ KASIR ██")
    print(" ===================  ███████████████████████")
    return

def shopOpen(role,potionshop,coin,userinventory,monsterdata,monstershop,yourmonsterdata,monsterinventory):
    yourcoin=coin
    if role == "agent":
        print("Selamat datang di Shop!")
        print()
        shopInterface()
        keluar = False
        while keluar != True:
            pilihMenu = input(">>> Pilih aksi (lihat/beli/keluar): ")
            if pilihMenu == "lihat":
                lihat_pilih = input(">>> Mau lihat apa? (monster/item): ")
                lihatSelesai = False
                while lihat_pilih != "monster" and lihat_pilih != "item" and lihatSelesai != True:
                    lihat_pilih = input(">>> Pilih antara monster/potion: ")
                if lihat_pilih == "monster":
                    print("ID | Type\t| ATK Power\t| DEF Power\t| HP\t| Stok\t| Harga")
                    for i in range(1,len(monstershop)): # Menampilkan setiap potion yang tersedia di Shop
                        x=int(monstershop[i][0])
                        print(f"{x}  | {monsterdata[x][1]}\t| {monsterdata[x][2]}\t\t| {monsterdata[x][3]}\t\t| {monsterdata[x][4]}\t| {monstershop[i][1]}\t| {monstershop[i][2]}")
                    lihatSelesai == True
                elif lihat_pilih == "item":
                    print("ID | Type\t\t| Stok\t| Harga")
                    for i in range(1,len(potionshop)): # Menampilkan setiap potion yang tersedia di Shop
                        print(f"{i}  | {potionshop[i][0]}\t| {potionshop[i][1]}\t| {potionshop[i][2]}")
                    lihatSelesai == True
            elif pilihMenu == "beli":
                print(f"Jumlah O.W.C.A Coin-mu sekarang {yourcoin}.")
                print()
                beliType = input(">>> Mau beli apa? (monster/item): ")
                beliSelesai = False
                while beliType != "monster" and beliType != "item" and beliSelesai != True:
                    beliType = input(">>> Pilih antara monster/potion: ")
                if beliType == "monster":
                    while True :
                        r=0
                        idMonsterBeli = int(input(">>> Masukkan id monster: "))
                        for i in yourmonsterdata :
                            if monsterdata[idMonsterBeli][1]==i[1] :
                                print("Monster sudah dimiliki")
                                break
                        else : 
                            for i in monstershop :
                                if i[0]==str(idMonsterBeli) :
                                    if yourcoin >= int(i[2]) :
                                        print("monster berhasil ditambahkan")
                                        yourcoin-= int(i[2])
                                        yourmonsterdata.append([userinventory[0][0],monsterdata[idMonsterBeli][1],'1'])
                                        monsterinventory.append([userinventory[0][0],monsterdata[idMonsterBeli][1],'1'])
                                        x=0
                                        for i in monstershop :
                                            if i[0]==str(idMonsterBeli) :
                                                monstershop[x][1]=str(int(monstershop[x][1])-1)
                                                break
                                            x+=1
                                        r=1
                                        break
                                    else :
                                        print("maaf coin mu kurang")
                                        break
                        if r==1 : break
        
                    print()
                    beliSelesai == True
                elif beliType == "item":
                    idPotion = int(input(">>> Masukkan id potion: "))
                    while True :
                        jumlahPotionBeli = int(input(">>> Masukkan jumlah: "))
                        if int(potionshop[idPotion][1]) >0 :
                            if jumlahPotionBeli>int(potionshop[idPotion][1]):
                                print("Stock tidak cukup")
                            else : 
                                if yourcoin >= (jumlahPotionBeli * int(potionshop[idPotion][2])):
                                    print(f"Berhasil membeli item: {jumlahPotionBeli} {potionshop[idPotion][0]}. Item sudah masuk ke inventory-mu!")
                                    print()
                                    index=0
                                    for i in userinventory :
                                        if i[1]==potionshop[idPotion][0]:
                                            break
                                        else :
                                            index+=1
                                    userinventory[index][2]=str(int(userinventory[index][2])+jumlahPotionBeli)
                                    print(userinventory)
                                    yourcoin-=(jumlahPotionBeli * int(potionshop[idPotion][2]))
                                    potionshop[idPotion][1]=str(int(potionshop[idPotion][1])-jumlahPotionBeli)
                                    break
                                else :
                                    print("maaf coin mu kurang")
                        else :
                            print("Stock habis!")
                            break

                    beliSelesai == True
            else: # pilihMenu == "keluar"
                keluar == True
                print("Terima kasih sudah berkunjung. Sampai bertemu lagi!")
                break
    return yourcoin
def shopmanagement(potionshop,monstershop,monsterdata)   :
        print("Selamat datang kembali, Admin!")
        print()
        keluar = False
        while keluar != True:
            pilihMenu = input(">>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ")
            if pilihMenu == "lihat":
                lihat_pilih = input(">>> Mau lihat apa? (monster/item): ")
                lihatSelesai = False
                while lihat_pilih != "monster" and lihat_pilih != "item" and lihatSelesai != True:
                    lihat_pilih = input(">>> Pilih antara monster/item: ")
                if lihat_pilih == "monster":
                    print("ID | Type\t| ATK Power\t| DEF Power\t| HP\t| Stok\t| Harga")
                    for i in range(1,len(monstershop)): # Menampilkan setiap potion yang tersedia di Shop
                        x=int(monstershop[i][0])
                        print(f"{x} | {monsterdata[x][1]}\t| {monsterdata[x][2]}\t\t| {monsterdata[x][3]}\t\t| {monsterdata[x][4]}\t| {monstershop[i][1]}\t| {monstershop[i][2]}")
                    lihatSelesai == True
                elif lihat_pilih == "item":
                    print("ID | Type\t\t| Stok\t| Harga")
                    for i in range(1,len(potionshop)): # Menampilkan setiap potion yang tersedia di Shop
                        print(f"{i}   | {potionshop[i][0]}\t| {potionshop[i][1]}\t| {potionshop[i][2]}")
                    lihatSelesai == True
            elif pilihMenu == "tambah":
                tambah_pilih = input("Mau tambah apa? (monster/item): ")
                tambahSelesai = False
                while tambah_pilih != "monster" and tambah_pilih != "item" and tambahSelesai != True:
                    tambah_pilih = (input(">>> Pilih antara monster/item: "))
                if tambah_pilih == "monster":
                    countabsencemonster = 0
                    absencemonsterid=[]
                    for i in monsterdata :
                        for j in monstershop :
                            if i[0]==j[0] :
                                 break
                        else :
                            if i[0] != 'id' :
                                countabsencemonster+=1
                                absencemonsterid.append(i[0])
                    if countabsencemonster==0 :
                        print("semua monster sudah ada dishop")
                    else :
                        print("ID | Type\t| ATK Power\t| DEF Power\t| HP\t")
                        for i in absencemonsterid :
                            x=int(i)
                            print(f"{x} | {monsterdata[x][1]}\t| {monsterdata[x][2]}\t\t| {monsterdata[x][3]}\t\t| {monsterdata[x][4]}\t")
                        print()
                        idMonsterTambah = int(input(">>> Masukkan id monster: ")) # Nanti tambah validasi
                        stokMonsterTambah = int(input(">>> Masukkan stok awal: "))
                        hargaMonsterTambah = int(input(">>> Masukkan harga: "))
                        monstershop.append([str(idMonsterTambah),str(stokMonsterTambah),str(hargaMonsterTambah)])
                        print(f"{monsterdata[idMonsterTambah][1]} telah berhasil ditambahkan ke dalam Shop!")
                elif tambah_pilih == "item":
                    potionFound = False
                    countFalse = 0
                    notinshoplist=[]
                    print("ID | Type")
                    for i in ['Healing Potion','Strength Potion','Resilience Potion','Monster Ball']:
                        for j in potionshop:
                            if i == j[0]:
                                potionFound = True
                                break
                        else:
                            potionFound = False
                            countFalse += 1
                            notinshoplist.append(i)
                        if potionFound == False:
                            print(f"{countFalse}  | {i}")
                    if countFalse == 0:
                        print("Semua Potion sudah tersedia pada Shop!")
                        print()
                    else:
                        idPotionTambah = int(input(">>> Masukkan id potion : "))
                        stokPotionTambah = int(input("Masukkan stok awal: "))
                        hargaPotionTambah = int(input("Masukkan harga: "))
                        potionshop.append([notinshoplist[idPotionTambah-1],str(stokPotionTambah),str(hargaPotionTambah)])
                        print(f"{notinshoplist[idPotionTambah-1]} telah berhasil ditambahkan ke dalam Shop!")
                        print()
            elif pilihMenu=='keluar' :
                keluar=True
            elif pilihMenu == "ubah":
                ubah_pilih = input("Mau ubah apa? (monster/potion): ")
                ubahSelesai = False
                while ubah_pilih != "monster" and ubah_pilih != "item" and ubahSelesai != True:
                    ubah_pilih = (input(">>> Pilih antara monster/item: "))
                if ubah_pilih == "monster":
                    idMonsterUbah = (input(">>> Masukkan id monster: ")) # Nanti nambahin validasi
                    stokMonsterBaru = (input(">>> Masukkan stok baru: "))
                    hargaMonsterBaru = (input(">>> Masukkan harga baru: "))
                    index=0
                    for i in monstershop :
                        if i[0]==(idMonsterUbah) :
                            break
                        index+=1
                    print(index)
                    pesanUbah = f"{monsterdata[int(idMonsterUbah)][1]} telah berhasil diubah "
                    if (stokMonsterBaru != ""):
                        pesanUbah += f"dengan stok baru sejumlah {stokMonsterBaru}"
                        monstershop[index][1]=stokMonsterBaru
                    if (stokMonsterBaru != "") and (hargaMonsterBaru != ""):
                        pesanUbah += " dan "
                    if (hargaMonsterBaru != ""):
                        pesanUbah += f"dengan harga baru {hargaMonsterBaru}"
                        monstershop[index][2]=hargaMonsterBaru
                    pesanUbah += "!"
                    print(pesanUbah)
                elif ubah_pilih == "item":
                    idPotionUbah = (input(">>> Masukkan id item: "))
                    stokPotionBaru = (input(">>> Masukkan stok baru: "))
                    hargaPotionBaru = (input(">>> Masukkan harga baru: "))
                    pesanUbah = f"{potionshop[int(idPotionUbah)][0]} telah berhasil diubah "
                    if (stokPotionBaru != ""):
                        pesanUbah += f"dengan stok baru sejumlah {stokPotionBaru}"
                        potionshop[int(idPotionUbah)][1]=stokPotionBaru
                    if (stokPotionBaru != "") and (hargaPotionBaru != ""):
                        pesanUbah += " dan "
                    if (hargaPotionBaru != ""):
                        pesanUbah += f"dengan harga baru {hargaPotionBaru}"
                        potionshop[int(idPotionUbah)][2]=hargaPotionBaru
                    pesanUbah += "!"
                    print(pesanUbah)
                    print()
         
            elif pilihMenu == "hapus":
                hapusPilih = input(">>> Mau hapus apa? (monster/item): ")
                hapusSelesai = False
                while hapusPilih != "monster" and hapusPilih != "item" and hapusSelesai != True:
                    hapusPilih = (input(">>> Pilih antara monster/potion: "))
                if hapusPilih == "monster":
                    idMonsterHapus = input(">>> Masukkan id monster: ")
                    index=0
                    for i in monstershop :
                        if i[0]==(idMonsterHapus) :
                            break
                        index+=1
                    yakinHapus = input(f"Apakah anda yakin ingin menghapus {monsterdata[int(idMonsterHapus)][1]}dari Shop (y/n)?" )
                    if yakinHapus == "y":
                        monstershop.pop(index)
                        print(f"{monsterdata[int(idMonsterHapus)][1]} telah berhasil dihapus dari Shop!")
                        print()
                    else:
                        print("Penghapusan dibatalkan!")
                        print()
                        continue
                if hapusPilih == "item":
                    idPotionHapus = input(">>> Masukkan id item: ")
                    yakinHapus = input(f"Apakah anda yakin ingin menghapus {potionshop[int(idPotionHapus)][0]} dari Shop (y/n)? ")
                    if yakinHapus == "y":
                        potionshop.pop(int(idPotionHapus))
                        print(f"{potionshop[int(idPotionHapus)][0]} telah berhasil dihapus dari Shop!")
                        print()
                    else:
                        print("Penghapusan dibatalkan!")
                        print()
                        continue
            else: # pilihMenu == "keluar"
                keluar == True
                print("Sampai bertemu lagi Admin!")
                break
    

# shopOpen("agent")
# shopOpen("admin")