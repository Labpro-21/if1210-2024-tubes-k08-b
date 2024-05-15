def exit():
    confirmExit = input(print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah (y/n)"))
    while confirmExit != "y" or confirmExit != "n":
        confirmExit = input(print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah (y/n)"))
    if confirmExit == "y":
        # jalankan fungsi SAVE
        print("Program berhasil ditutup!")
    else: # confirmExit =="n
        print("Program berhasil ditutup!")