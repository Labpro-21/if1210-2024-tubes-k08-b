def godServant() :
    print("""
             .---.
            / ,-- 
    .--.   ( (^_^) )   .--.
  ,'    \  (.-`-'(_)  /    `.
 /       `-/ \ `.  \-'       
: (_,' .  / (.\_ ") \  . `._) :
|   `-'(_,\ \     / /._)`-'   |
|       .  `.\,O,'.'  .   :   |
|   . : !   /\_  /\   ! . !   |
| ! |-'-|  : ""T"" :  |-'-| | |
| |-'   `-'|   H   |`-'   `-| |
`-'        |   H .:|        `-'
           | . H !||
           | : H :!|
           | ! H !||
           | | H |||
           | | H |||  
           /_,'V.L|.
""")

def help(status,role) : #jika pengguna belum login, status akan menjadi false dan mengeluarkan beberapa command umum
    #command umum
    godServant()
    if status == False :
        print("List commands you can call :")
        print("1. Login")
        print("   Login ke akun admin/agent")
        print("2. Register")
        print("   Membuat akun agent baru")
        print("3. Save")
        print("   Menyimpan semua perubahan dalam sebuah folder")
        print("4. Exit")
        print("   Keluar dari program")
        print()
        print("Footnote :")
        print("1. Anda belum login silahkan login terlebih dahulu atau melaukan register")
        print("2. Pastikan input yang anda masukkan sudah tepat atau sesuai perintah program")
        print("3. Jangan lupa untuk save program sebelum exit")
    else : #jika pengguna sudah login, tampilkan daftar perintah berdasarkan role pengguna
        if role == 'agent' : #jika pengguna adalah agent
            #command yang dapat dilakukan oleh agent
            print("List commands you can call :")
            print("1. Battle")
            print("   1v1 dengan monster random")
            print("2. Arena")
            print("   Tempat pelatihan monster anda")
            print("3. Shop")
            print("   Tempat jual beli potion dan monster")
            print("4. Inventory")
            print("   Cek semua item dan monster anda")
            print("5. Laboratory")
            print("   Tempat untuk meng-upgrade monster anda")
            print("6. Jackpot")
            print("   Tempat untuk menguji keberuntungan anda")
            print("7. Logout")
            print("   Keluar dari akun anda")
            print()
            print("Footnote :")
            print("1. Pastikan input yang dimasukkan sesuai dengan perintah program")
            print("2. Jangan lupa untuk save program setelah logout")
        if role == 'admin' : #jika pengguna adalah admin
            #command yang dapat dilakukan oleh admin
            print("List commands you can call :")
            print("1. Shop")
            print("   Manage shop")
            print("2. Monster")
            print("   Manage monster")
            print("3. Logout")
            print("   Keluar dari akun anda")
            print()
            print("Footnote :")
            print("1. Pastikan input yang dimasukkan sesuai dengan perintah program")
            print("2. Jangan lupa untuk save program setelah logout")
            