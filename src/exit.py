from load import save
def exit(user,monsterinventory,itemshop,monster,monstershop,iteminventory):
    confirmExit = input(("Apakah Anda mau melakukan penyimpanan file yang sudah diubah (y/n)"))
    while confirmExit != "y" and confirmExit != "n":
        confirmExit = input(print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah (y/n)"))
    if confirmExit == "y":
        save(iteminventory,monster,user,monstershop,itemshop,monsterinventory)
        print("Program berhasil disave dan ditutup!")
    else: # confirmExit =="n
        print("Program berhasil ditutup!")