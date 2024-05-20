from src.load import save
def exit(user,monsterinventory,itemshop,monster,monstershop,iteminventory):
    confirmExit = input(("Apakah Anda mau melakukan penyimpanan file yang sudah diubah (y/n) :"))
    while confirmExit.lower() != "y" and confirmExit.lower() != "n":
        confirmExit = input(("Masukkan y/n saja :"))
    if confirmExit.lower() == "y":
        save(iteminventory,monster,user,monstershop,itemshop,monsterinventory)
        print("Program berhasil disave dan ditutup!")
    elif confirmExit.lower() == "n" : 
        print("Program berhasil ditutup!")
