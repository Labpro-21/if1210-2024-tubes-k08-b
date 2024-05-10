from readwritecsv import *

used_Pot_Array = [0, 0, 0]                                                 # used_Pot_Array adalah array untuk menunjukkan apakah sebuah potion telah digunakan sekali dalam battle dengan used_Pot_Array [jumlah strength potion digunakan, jumlah resilience potion digunakan, jumlah heal potion digunakan]

potion_data = read_csv('src\potion.csv')

def potion(pot_User_Data, used_Pot, attack, defense, HP, max_HP, mons_Name, pilihan):
    if pilihan==1 :
      if int(pot_User_Data[1][1])> 0 :
        if used_Pot[0] == 0 :
          used_Pot[0] += 1
          attack *= 105/100
          print(f"Potion telah diminum {mons_Name}, {mons_Name} menjadi lebih kuat!!")
          potion_data[1][1]=str(int(potion_data[1][1])-1)
          write_csv("src\potion.csv",potion_data)
          return attack
        else :
          print(f"Potion hanya bisa digunakan sekali")
          return 0
      else :
        print("Sayangnya Anda tidak memiliki potion tersebut, silakan pilih potion lain: ")
        return 0
      
    elif pilihan==2 :
      if int(pot_User_Data[2][1]) > 0 :
        if used_Pot[1] == 0 :
          used_Pot[1] += 1
          defense *= 105/100
          print(f"Potion telah diminum {mons_Name}, {mons_Name} menjadi lebih sulit dilukai!!")
          potion_data[2][1]=str(int(potion_data[2][1])-1)
          write_csv("src\potion.csv",potion_data)
          return defense
        else : 
          print(f"Potion hanya bisa digunakan sekali")
          return 0
      else :
        print("Sayangnya Anda tidak memiliki potion tersebut, silakan pilih potion lain: ")
        return 0
    elif pilihan==3 :
      if int(pot_User_Data[3][1]) > 0 :
        if used_Pot[2] == 0 :
          used_Pot[2] += 1
          if HP * 125/100 <= max_HP :
            HP *= 125/100
            print(f"Potion telah diminum {mons_Name}, {mons_Name} beregenerasi dengan cepat sehingga hampir semua luka yang diterimanya menghilang!!")
            potion_data[3][1]=str(int(potion_data[3][1])-1)
            write_csv("src\potion.csv",potion_data)
            return HP
          else :
            HP = max_HP
            print(f"Potion telah diminum {mons_Name}, {mons_Name} beregenerasi dengan cepat sehingga hampir semua luka yang diterimanya menghilang!!")
            potion_data[3][1]=str(int(potion_data[3][1])-1)
            write_csv("src\potion.csv",potion_data)
            return HP
        else : 
          print(f"Potion hanya bisa digunakan sekali")
          return 0
      else :
        print("Sayangnya Anda tidak memiliki potion tersebut, silakan pilih potion lain: ")
        return 0
      
  

# contoh penggunaan function : potion(pot_Inventory (2, csvRead("E:\Documents\Daspro\Tubes\if1210-2024-tubes-k08-b\item_inventory.csv")), used_Pot_Array, 10, 20, 30, 100, "Zuko")