from readwritecsv import *
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
        user = read_csv("data/data1/user.csv")
        inventory = read_csv("data/data1/item_inventory.csv")
        monster = read_csv("data/data1/monster.csv")
        monsterinventory = read_csv("data/data1/monser_inventory.csv")
        itemshop=read_csv("data/data1/item_shop.csv")
        monstershop=read_csv("data/data1/monster_shop.csv")
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


def buang(data,inventory) :
    print("mau buang item apa ?")
    inp = input("(1(str)/2(res)/3(heal))? ------->")
    if inp == '1' :
        for i in data :
            if i[1]=='strenghpotion' :
                if int(i[2]) >0 :
                    i[2]=str(int(i[2])-1)
                    print("strenght potion dibuang satu")
                    break
                else :
                    print("anda tidak memiliki str potion")
                    break
        else :
            print("anda tidak memiliki strenght potion")
    elif inp == '2' :
        for i in data :
            if i[1]=='respotion' :
                if int(i[2])>0 :
                    i[2]=str(int(i[2])-1)
                    print("resistance potion dibuang satu")
                    break
                else :
                    print("anda tidak memiliki res potion")
                    break
        else :
            print("anda tidak memiliki resistance potion")
    elif inp == '3' :
        for i in data :
            if i[1]=='healingpotion' :
                if int(i[2]) > 0 :
                    i[2]=str(int(i[2])-1)
                    print("heal potion dibuang satu")
                    break
                else :
                    print("anda tidak memiliki heal potion")
                    break
        else :
            print("anda tidak memiliki heal potion")
    x=0
    idx=[]
    for i in inventory :
        print(f"{i[0]} DAN {data[0][0]}")
        if i[0]==data[0][0] :
            idx.append(x)
        x+=1
    for i in range(len(idx)-1,-1,-1) :
        inventory.pop(idx[i])
    for i in data :
        inventory.append(i)

           
def write(path,data) :
    # Writing data to the CSV file
    with open(path, 'w') as file:
        for row in data:
            file.write(','.join(map(str, row)) + '\n')

    print(f"CSV file '{path}' has been created successfully.")

def save(inventory,monster,user) :
    # ALGORITMA
    path = "data/" + input("Masukkan nama folder: ")
    print("Saving...")
    if (os.path.exists(path)) :
        write(path+"/inventory.csv",inventory)
        write(path+"user.csv",user)
        write(path+"/monster.csv",monster)
    