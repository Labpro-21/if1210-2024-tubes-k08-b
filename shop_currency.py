def shopOpen(role):
    if role == "agent":
        print("Selamat datang di Shop!")
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
                    print("potion")
                    lihatSelesai == True
                    # potion_list()
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
                    idpotionBeli = input(">>> Masukkan id potion: ")
                    jumlahPotionBeli = input(">>> Masukkan jumlah: ")
                    # if OWCA >= jumlah x potion:
                    print("Berhasil membeli item: [jumlah potion] [nama potion]. Item sudah masuk ke inventory-mu!")
                    print()
                    beliSelesai == True
            else: # pilihMenu == "keluar"
                keluar == True
                print("Terima kasih sudah berkunjung. Sampai bertemu lagi!")
                break    

shopOpen("agent")