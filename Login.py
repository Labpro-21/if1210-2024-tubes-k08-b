from Register import registered_users
# Fungsi untuk melakukan login
def login(username, password, logged_in_users):
    if username in logged_in_users:
        print("Anda sudah login. Silakan logout terlebih dahulu.")
        return False

    if username in registered_users:
        if registered_users[username]['password'] == password:
            print("Login berhasil.")
            logged_in_users.add(username)
            return True
        else:
            print("Password salah.")
            return False
    else:
        print("Username tidak terdaftar.")
        return False

# Fungsi untuk logou

# Main program
def main():
    logged_in_users = set()

    while True:
        command = input("Masukkan command (login/logout/exit): ")
        
        if command == 'login':
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            login(username, password, logged_in_users)
        elif command == 'exit':
            break
        else:
            print("Command tidak valid. Silakan masukkan command yang sesuai.")

if __name__ == "__main__":
    main()