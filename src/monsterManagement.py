# FUNGSI UNTUK PENAMBAHAN MONSTER
# Fungsi - fungsi proses untuk mengecek validasi input data monster
def cekint(input):
    # Check if the input is empty, it's not an integer
    if input == '':
        return False
    # Convert input to string if it is not already
    input = str(input)
    # Check for a negative sign at the beginning
    if input[0] == '-':
        if len(input) == 1:
            return False  # Only a '-' is not an integer
        input = input[1:]  # Remove the negative sign for further check
    # Check if all characters are digits
    for char in input:
        if ord(char) < ord('0') or ord(char) > ord('9'):
            return False
    return True

def checkType(type,listMonster):
    while True:
        monsterExist = False # asumsi awal, nama yang diinput tidak sama dengan nama pada database.
        for i in range(1, len(listMonster)): # 1 sebagai parameter karena listMonster[0] merupakan judul, len(listMonster) sebagai parameter akhir karena database monster bisa berubah seiring game berjalan.
            if listMonster[i][1] == type: # apabila nama monster yang diinput ada yang sama dengan nama monster yang ada di database
                print("Nama sudah terdaftar. Coba lagi!")
                type = str(input("Masukkan Type Monster : "))
                monsterExist = True # bila nama monster yang diinput ada yang sama dengan nama monster yang ada di database, maka menjadi True.
        if monsterExist == False : # Terjadi apabila nama monster yang diinput berhasil pengecekan
            break
    return type

def checkAttack(attack):
    while True:
        if cekint(attack): # bila keseluruhan attack berupa angka
            attack = int(attack) # ubah menjadi integer agar dapat dioperasikan
            break 
        else : # terdapat character yang bukan angka
            print("Masukkan bukan bertipe integer, coba lagi!")
            attack = str(input("Masukkan attack power : ")) # input berupa string karena untuk pengecekan isdigit()
    return attack

def checkDefense(defense):
    while True:
        if cekint(defense): # defense berupa angka secara keseluruhan
            defense = int(defense) # diubah menjadi integer agar dapat dioperasikan
            if 0 <= defense <= 50 : # nilai sudah sesuai ketentuan
                break
            else : # defense > 0 dan defense > 50, belum sesuai
                print("Masukkan harus bernilai 0-50")
                defense = str(input("Masukkan DEF power (0-50) : "))
        else : # defense tidak merupakan angka secara keseluruhan
            print("Masukkan bukan bertipe integer, coba lagi!")
            defense = str(input("Masukkan DEF power (0-50) : "))
    return defense

def checkHp(hp):
    while True:
        if cekint(hp): # keseluruhan hp berupa angka
            hp = int(hp) # ubah menjadi integer agar dapat dioperasikan
            break
        else : # terdapat character yang bukan angka pada hp
            print("Masukkan bukan bertipe integer, coba lagi!")
            hp = str(input("Masukkan hp : ")) # input berupa string karena untuk pengecekan isdigit() perlu tipe data string
    return hp

# FUNGSI SIMPLIFIKASI
# Fungsi-fungsi dibawah berisi input awal data monster baru dari user
def newType(listMonster):
    type = str(input("Masukkan Type Monster : "))
    return checkType(type,listMonster)

def newAttack():
    attack = str(input("Masukkan attack power : "))
    return checkAttack(attack)

def newDefense():
    defense = str(input("Masukkan DEF power (0-50) : "))
    return checkDefense(defense)

def newHp():
    hp = str(input("Masukkan hp : "))
    return checkHp(hp)

# FUNGSI CHECK Y/N
def checkUserInput(listMonster,userInput, nType, nAttack , nDefense, nHp):
    while True:
        if userInput.lower() == "y" :
            # disini masukkan file ke csv dulu karena bila append terlebih dahulu len(listMonster) id akan tidak sesuai pada file monster.csv
            listMonster.append([str(len(listMonster)), nType, str(nAttack), str(nDefense), str(nHp)])
            print("Monster berhasil ditambahkan")
            break
        elif userInput.lower() == "n" :
            print("Monster gagal ditambahkan")
            break
        else : # Input bukan Y/N
            print("input tidak valid, hanya menerima input Y/N")
            userInput = str(input("(Y/N): "))

def validUserInput(listMonster,userInput, nType, nAttack, nDefense, nHp):
    userInput = str(input("Apakah mau tambahkan monster? (Y/N): "))
    checkUserInput(listMonster,userInput, nType, nAttack, nDefense, nHp)

# FUNGSI PENAMBAHAN MONSTER BARU SECARA KESELURUHAN
def newMonster(listMonster):
    nType = newType(listMonster)
    nAttack = newAttack()
    nDefense = newDefense()
    nHp = newHp()
    userInput = ""
    validUserInput(listMonster,userInput, nType, nAttack, nDefense, nHp)

# FUNGSI PENCETAKAN TABEL RAPIH
# Fungsi mengubah elemen integer pada list dari data csv menjadi string karena nanti akan digunakan fungsi len()
def changeInt(listMonster):
    for i in range(1,len(listMonster)):
        for j in range(5):
            if j != 1 : # karena j == 1 berupa type monster yang berupa string
                listMonster[i][j] = str(listMonster[i][j])
    return listMonster

# Fungsi mencari elemen terbesar dalam 1 kolom
# elemen terbesar tiap kolom akan disimpan pada array largestElement, posisi bersamaan dengan kolom
def findLargestElement(largestElement,listMonster):
    for i in range(len(largestElement)):
        for j in range(len(listMonster)):
            if largestElement[i] < len(listMonster[j][i]):
                largestElement[i] = len(listMonster[j][i])
    return largestElement

# Fungsi mengganti header dari file csv yang kurang rapih
def changeHeader(newHeader, listMonster):
    for i in range(5):
        listMonster[0][i] = newHeader[i]
    return

# Fungsi print tabel database monster
def printTabel (listMonster, largestElement):
    for i in range(len(listMonster)):
        # Print judul terlebih dahulu
        print(listMonster[i][0], end="") 
        for j in range(abs(largestElement[0]-(len(listMonster[i][0])))):
            print(" ", end="")
        print("  |", end="")

        # Print type monster
        print(" ", listMonster[i][1], end="")
        for j in range(abs(largestElement[1]-(len(listMonster[i][1])))):
            print(" ", end="")
        print("  |", end="")

        # Print ATK Power
        print(" ", listMonster[i][2], end="")
        for j in range(abs(largestElement[2]-(len(listMonster[i][2])))):
            print(" ", end="")
        print("  |", end="")

        # Print DEF Power
        print(" ", listMonster[i][3], end="")
        for j in range(abs(largestElement[3]-(len(listMonster[i][3])))):
            print(" ", end="")
        print("  |", end="")

        # Print HP
        print(" ", listMonster[i][4], end="")
        for j in range(abs(largestElement[4]-(len(listMonster[i][4])))):
            print(" ", end="")
        print("  |", end="")
    
        # Enter agar program lanjut print baris ke-2 dan seterusnya
        print("")
    return

# Fungsi akhir pencetakan tabel
def tabelMonster(listMonster):
    largestElement = [-1, -1, -1, -1, -1]
    newHeader = ["ID", "Type", "ATK Power", "DEF Power", "HP"]
    changeInt(listMonster)
    findLargestElement(largestElement,listMonster)
    changeHeader(newHeader, listMonster)
    printTabel(listMonster, largestElement)
    return

# FUNGSI AKHIR MONSTER MANAGEMENT
def monsterManagement(listMonster):
    while True :
        print("""
SELAMAT DATANG DI DATABASE PARA MONSTER !!!
1. Tampilkan Semua Monster
2. Tambah Monster Baru
( Ketik nomor untuk aksi yang diinginkan, ketik 0 untuk keluar )
        """)
        aksiUser = str(input("Pilih Aksi: "))
        if aksiUser == "1" :
            tabelMonster(listMonster)
            str(input("Ketik apapun untuk balik ke menu: "))
        elif aksiUser == "2" :
            newMonster(listMonster)
        elif aksiUser == "0" :
            print("Teirma kasih telah mengunjungi database monster")
            break
        else :
            print("Input tidak valid, input yang diterima hanya 0/1/2")