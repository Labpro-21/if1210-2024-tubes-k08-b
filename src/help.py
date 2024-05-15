def help(status,role) :
    if status == False :
        print("List command yang dapat anda lakukan :")
        print("1. Login")
        print("   Login ke akun admin/agent")
        print("2. Register")
        print("   Membuat akun agent baru")
        print("3. Save")
        print("   Menyimpan semua perubahan dalam sebuah folder")
        print("4. Exit")
        print("   Keluar dari program")
    else :
        if role == 'agent' :
            print("List command yang dapat anda lakukan :")
            print("1. Battle")
            print("   1v1 dengan monster random")
            print("2. Arena")
            print("   Tempat pelatihan monster anda")
            print("3. Shop")
            print("   Tempat jual beli potion dan monster")
            print("4. Inventory")
            print("   Cek semua item dan monster anda")
            print("5. Logout")
            print("   Keluar dari akun anda")
            