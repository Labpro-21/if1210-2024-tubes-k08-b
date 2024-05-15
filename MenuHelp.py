from Register import register
from Login import login

# Fungsi untuk menampilkan bantuan sebelum login
def help_before_login():
    print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
    print("Command yang tersedia sebelum login:")
    print("- login: Untuk melakukan login.")
    print("- register: Untuk mendaftar sebagai pengguna baru.")

# Fungsi untuk menampilkan bantuan setelah login
def help_after_login(role, username) :
    print(f"Halo Agent {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
    print("Command yang tersedia setelah login:")
    if role == 'agent':
        print("- lihat_data: Untuk melihat data tertentu.")
        print("- ubah_data: Untuk mengubah data.")
        print("- logout: Untuk logout dari sistem.")
        print("- monster: melihat owca-dex yang dimiliki oleh Agent")
    elif role == 'admin':
        print("- tambah_pengguna: Untuk menambah pengguna baru.")
        print("- hapus_pengguna: Untuk menghapus pengguna.")
        print("- logout: Untuk logout dari sistem.")
    print("- help: Untuk menampilkan bantuan.")
    print("- exit: Untuk keluar dari program.")

# Fungsi untuk menampilkan deskripsi penggunaan command HELP
def help_command():
    print("Command HELP digunakan untuk menampilkan bantuan.")
    print("Penggunaan:")
    print("- Sebelum login: Ketik 'help' saat belum login.")
    print("- Setelah login: Ketik 'help' setelah login untuk menampilkan bantuan khusus per role.")
    print("Catatan:")
    print("Pastikan untuk melakukan validasi input sesuai dengan petunjuk yang diberikan dalam bantuan.")

# Main program
def main():
    logged_in_users = set()

    print (">>> HELP")

    print ("=========== HELP ===========")

    while True:
        command = input("Masukkan command: ")
        
        if command == 'login':
            login()  # Implementasi login
            pass
        elif command == 'register':
            register()  # Implementasi register
        elif command == 'exit':
            break
        elif command == 'help':
            help_before_login()
        elif command in logged_in_users:
            # Implementasi command setelah login
            pass
        else:
            print("Command tidak valid. Ketik 'help' untuk menampilkan bantuan.")

if __name__ == "__main__":
    main()