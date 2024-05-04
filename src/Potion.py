used_Pot_Array = [0, 0, 0]                                                 # used_Pot_Array adalah array untuk menunjukkan apakah sebuah potion telah digunakan sekali dalam battle dengan used_Pot_Array [jumlah strength potion digunakan, jumlah resilience potion digunakan, jumlah heal potion digunakan]

def pot_Inventory (id, pot_Inventory_Data):
  array_Pot = [0, 0, 0]                                                    # array_Pot adalah array dengan isi yaitu [jumlah potion strength, jumlah potion resilience, jumlah potion heal]
  
  for i in range (1, len(pot_Inventory_Data)):
    pot_Inventory_Data[i][0] = int(pot_Inventory_Data[i][0])
    pot_Inventory_Data[i][2] = int(pot_Inventory_Data[i][2]) 

  for i in range (len(pot_Inventory_Data)):
    if pot_Inventory_Data[i][0] == id :
      if pot_Inventory_Data[i][1] == 'strength' :
        array_Pot[0] = pot_Inventory_Data[i][2]

      elif pot_Inventory_Data[i][1] == 'resilience' :
        array_Pot[1] = pot_Inventory_Data[i][2]

      elif pot_Inventory_Data[i][1] == 'heal' :
        array_Pot[2] = pot_Inventory_Data[i][2]
  return array_Pot

def potion(pot_User_Data, used_Pot, attack, defense, HP, max_HP, mons_Name):
  while True :
    pot = input("Pilih potion yang ingin Anda gunakan/batalkan penggunaan option (str/res/heal/cancel): ")
    if pot == 'str' :
      if pot_User_Data[0] > 0 :
        if used_Pot[0] == 0 :
          used_Pot[0] += 1
          attack *= 105/100
          print(f"Potion telah diminum {mons_Name}, {mons_Name} menjadi lebih kuat!!")
        else :
          print(f"Potion hanya bisa digunakan sekali")
      else :
        print("Sayangnya Anda tidak memiliki potion tersebut, silakan pilih potion lain: ")
    elif pot == 'res' :
      if pot_User_Data[1] > 0 :
        if used_Pot[1] == 0 :
          used_Pot[1] += 1
          defense *= 105/100
          print(f"Potion telah diminum {mons_Name}, {mons_Name} menjadi lebih sulit dilukai!!")
        else : 
          print(f"Potion hanya bisa digunakan sekali")
      else :
        print("Sayangnya Anda tidak memiliki potion tersebut, silakan pilih potion lain: ")
    elif pot == 'heal' :
      if pot_User_Data[2] > 0 :
        if used_Pot[2] == 0 :
          used_Pot[2] += 1
          if HP * 125/100 <= max_HP :
            HP *= 125/100
            print(f"Potion telah diminum {mons_Name}, {mons_Name} beregenerasi dengan cepat sehingga hampir semua luka yang diterimanya menghilang!!")
          else :
            HP = max_HP
            print(f"Potion telah diminum {mons_Name}, {mons_Name} beregenerasi dengan cepat sehingga hampir semua luka yang diterimanya menghilang!!")
        else : 
          print(f"Potion hanya bisa digunakan sekali")
      else :
        print("Sayangnya Anda tidak memiliki potion tersebut, silakan pilih potion lain: ")
    elif pot == 'cancel' :
      break

# contoh penggunaan function : potion(pot_Inventory (2, csvRead("E:\Documents\Daspro\Tubes\if1210-2024-tubes-k08-b\item_inventory.csv")), used_Pot_Array, 10, 20, 30, 100, "Zuko")