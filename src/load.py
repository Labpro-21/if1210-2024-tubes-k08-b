from readwritecsv import *
from csvParser import *
import os
import argparse
def load() :
    parser = argparse.ArgumentParser(add_help=False,usage='%(prog)s <nama_folder>')
    parser.add_argument("nama_folder",nargs="?",type=str,default="")
    args = parser.parse_args() 
    path = "data/"+args.nama_folder # Perlu ditambah "save/" karena parent foldernya "save"
    if(path == "data/"): # jika args.nama_folder kosong 
        print("Tidak ada nama folder yang diberikan!\n")
        parser.print_usage()
        return []
    elif(os.path.exists(path)): # jika folder ditemukan
        print("Loading...")
        print("Selamat datang")
        user = read_csv(path+"/user.csv")
        inventory = read_csv(path+"/item_inventory.csv")
        monster = read_csv(path+"/monster.csv")
        monsterinventory = read_csv(path+"/monser_inventory.csv")
        itemshop=read_csv(path+"/item_shop.csv")
        monstershop=read_csv(path+"/monster_shop.csv")
        return [user,inventory,monster,monsterinventory,itemshop,monstershop]
    else: # folder tidak ditemukan
        print(f"Folder \"{path}\" tidak ditemukan.")
        return []

def login(user,inventory,monsterinventory) :
    username = input("username :")
    password = input("password :")
    for i in user :
        if i[1] == username :
            if i[2] == password :
                if i[3] =='agent' :
                    player_inventory = []
                    monster_inventory =[]
                    print("login berhasil")
                    for j in inventory :
                        if j[0]==i[0] :
                            player_inventory.append(j)
                    for j in monsterinventory :
                        if j[0]==i[0] :
                            monster_inventory.append(j)
                    return player_inventory,monster_inventory,i[3],int(i[4])
                    break
                elif i[3] =='admin' :
                    return 1,1,i[3],1
            else :
                print("password salah")
                return 0,0,0,0
                break
    else :
        print("username tidak ditemukan")
        return 0,0,0,0

def register(user,inventory,monsterinventory,monster) :
    while True :
        usernamebaru = input("Masukkan Username :")
        for i in user :
            if i[1]== usernamebaru :
                print("Username sudah terpakai")
                break
        else :
            break
    passwordbaru = input("Masukkan password :")
    print('PILIH MONSTER PERTAMA ANDA :')
    for i in range(3) :
        print(f"{i+1}. {monster[i+1][1]}")
    idpilihan = input("--->")
    idbaru = len(user)
    monsterinventory.append([str(idbaru),monster[int(idpilihan)][1],'1'])
    user.append([str(idbaru),usernamebaru,passwordbaru,'agent','0'])
    inventory.append([str(idbaru),'healingpotion','0'])
    inventory.append([str(idbaru),'respotion','0'])
    inventory.append([str(idbaru),'strenghpotion','0'])

    player_inventory = []
    monster_inventory =[]
    print("SELAMAT DATANG AGENT BARU")
    for j in inventory :
        if j[0]==str(idbaru) :
            player_inventory.append(j)
    for j in monsterinventory :
        if j[0]==str(idbaru) :
            monster_inventory.append(j)
    return player_inventory,monster_inventory,'agent',0


           
def write(path,data) :
    # Writing data to the CSV file
    with open(path, 'w') as file:
        for row in data:
            file.write(','.join(map(str, row)) + '\n')

    print(f"CSV file '{path}' has been created successfully.")

def save(inventory,monster,user,monstershop,itemshop,monsterinventory) :
    # ALGORITMA
    path = "data/" + input("Masukkan nama folder: ")
    print("Saving...")
    if (os.path.exists(path)) :
        write_csv(path+"/item_inventory.csv",inventory)
        write_csv(path+"/user.csv",user)
        write_csv(path+"/monster.csv",monster)
        write_csv(path+"/monster_shop.csv",monstershop)
        write_csv(path+"/item_shop.csv",itemshop)
        write_csv(path+"/monster_inventory.csv",monsterinventory)
    else :
        os.mkdir(path)
        write_csv(path+"/item_inventory.csv",inventory)
        write_csv(path+"/user.csv",user)
        write_csv(path+"/monster.csv",monster)
        write_csv(path+"/monster_shop.csv",monstershop)
        write_csv(path+"/item_shop.csv",itemshop)
        write_csv(path+"/monster_inventory.csv",monsterinventory)


