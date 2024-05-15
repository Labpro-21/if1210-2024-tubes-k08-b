import csvParser

# Fungsi isalnum() menggunakan kode ASCII
def isalnum(s):
    for char in s:
        ascii_val = ord(char)
        if not (48 <= ascii_val <= 57 or    # Digit 0-9
                65 <= ascii_val <= 90 or    # Huruf kapital A-Z
                97 <= ascii_val <= 122):    # Huruf kecil a-z
            return False
    return True

# Fungsi untuk membaca file monster.csv dan mengembalikan daftar monster
def baca_file_monster():
    monster_list = ["Mimik", "Makima", "Godzilla"] #csvParser.csvRead("./monster.csv")
    print(monster_list)
    return monster_list

# Fungsi untuk memeriksa apakah username sudah terdaftar
def cek_username(username, registered_users):
    return username in registered_users

# Fungsi untuk mendaftarkan pengguna baru
def daftar_pengguna(username, password, registered_users):
    if not cek_username(username, registered_users):
        registered_users[username] = {
            'password': password,
            'role': 'agent',
            'OWCA_coin': 0,
            'monster': None
        }
        print("Pengguna berhasil didaftarkan.")
        return True
    else:
        print("Username sudah terdaftar. Silakan gunakan username lain!")
        return False

# Fungsi untuk memilih monster awal jika pengguna baru
def pilih_monster_awal(username, registered_users, monster_list):
    monster = input("Pilih monster awal dari File Monster (monster.csv): ")
    if monster in monster_list:
        registered_users[username]['monster'] = monster
        print("Monster berhasil dipilih.")
        return monster
    else:
        print("Monster tidak ditemukan.")
        return monster

# Register
def register(usernames, passwords):
    # Baca file monster.csv
    monster_list = baca_file_monster()

    print('>>> REGISTER')

    registered_users = {}

    while True:
        username = input("Masukkan username baru: ")
        if not isalnum(username) and '_' not in username and '-' not in username:
            print("Username hanya dapat mengandung alfabet (A-Z), (a-z), underscore '_', strip '-', dan angka 0-9.")
            continue
        
        found = False
        for u in usernames:
            if u == username:
                found = True
                break

        if (found):
            print(f"Username {username} sudah terpakai, silahkan gunakan username lain!")
            continue

        password = input("Masukkan password: ")

        if daftar_pengguna(username, password, registered_users):
            monster = pilih_monster_awal(username, registered_users, monster_list)
            while monster not in monster_list:
                monster = pilih_monster_awal(username, registered_users, monster_list)

        print(f"Selamat datang agent {username}. Mari mengalahkan Dr. Asep Spakbor dengan {registered_users[username]['monster']}!")
        usernames.append(username)
        passwords.append(password)

if __name__ == "__main__":
    usernames = []
    passwords = []

    while True:
        register(usernames, passwords)
        print(usernames)