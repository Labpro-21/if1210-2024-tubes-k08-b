# fungsi jumlahPot untuk mengambil data potion yang ada di userInventory
def jumlahPot(userInventory) :
  for i in userInventory :
    if i[1] == 'Strength Potion' :
      jumlahStr = i[2]
      break
    else : 
      jumlahStr = 0
  for i in userInventory :
    if i[1] == 'Resilience Potion' :
      jumlahRes = i[2]
      break
    else : 
      jumlahRes = 0
  for i in userInventory :
    if i[1] == 'Healing Potion' :
      jumlahHeal = i[2]
      break
    else : 
      jumlahHeal = 0

  return [int(jumlahStr), int(jumlahRes), int(jumlahHeal)]

# fungsi indexPot untuk mengecek index masing-masing tipe potion di userInventory
def indexPot(userInventory) :
  indexStr = 0
  indexRes = 0
  indexHeal = 0

  for i in userInventory :
    if i[1] != 'Strength Potion' :                                        # untuk mencari indexStr dengan menambahkan indexStr secara berulang
      indexStr += 1
    elif i[1] == 'Strength Potion' :                                      # untuk mendapatkan indexStr dengan menghentikan penambahan indexStr
      break

  for i in userInventory :
    if i[1] != 'Resilience Potion' :
      indexRes += 1
    elif i[1] == 'Resilience Potion' : 
      break

  for i in userInventory :
    if i[1] != 'Healing Potion' :
      indexHeal += 1
    elif i[1] == 'Healing Potion' : 
      break

  return [indexStr, indexRes, indexHeal]

# fungsi potion untuk meng-return nilai 1 atau 0 untuk diproses di battle.py
def potion(jumlahpot, indexPot, used_Pot_Array, userInventory, attack, defense, HP, max_HP, mons_Name, pilihan):
    if pilihan == 1 :
      if int(jumlahpot[0]) > 0 :                           # mengecek ada tidaknya potion strength
        if used_Pot_Array[0] == 0 :                        # mengecek pernah tidaknya potion strength digunakan
          used_Pot_Array[0] += 1
          attack *= 105/100
          print(f"Potion telah diminum {mons_Name}, {mons_Name} menjadi lebih kuat!!")
          jumlahpot[0] -= 1
          userInventory[indexPot[0]][2] = str(int(userInventory[indexPot[0]][2])-1)
          return attack                                    # return nilai attack monster setelah menggunakan potion strength
        else :
          print("Potion hanya bisa digunakan sekali")
          return 0                                         # return 0 untuk mengindikasi potion tidak bisa digunakan
      else :
        print("Sayangnya Anda tidak memiliki potion tersebut, silakan pilih potion lain")
        return 0
      
    elif pilihan == 2 :
      if int(jumlahpot[1]) > 0 :                           # mengecek ada tidaknya potion resilience
        if used_Pot_Array[1] == 0 :                        # mengecek pernah tidaknya potion resilience digunakan
          used_Pot_Array[1] += 1
          defense *= 105/100
          print(f"Potion telah diminum {mons_Name}, {mons_Name} menjadi lebih sulit dilukai!!")
          jumlahpot[1] -=1
          userInventory[indexPot[1]][2] = str(int(userInventory[indexPot[1]][2])-1)
          return defense                                   # return nilai defense monster setelah menggunakan potion resilience
        else : 
          print("Potion hanya bisa digunakan sekali")
          return 0
      else :
        print("Sayangnya Anda tidak memiliki potion tersebut, silakan pilih potion lain: ")
        return 0
      
    elif pilihan==3 :
      if int(jumlahpot[2]) > 0 :                           # mengecek ada tidaknya potion healing
        if used_Pot_Array[2] == 0 :                        # mengecek pernah tidaknya potion healing digunakan
          used_Pot_Array[2] += 1
          if HP * 125/100 <= max_HP :                      # mengecek penggunaan potion melebihi HP maksimum atau tidak
            HP *= 125/100
            print(f"Potion telah diminum {mons_Name}, {mons_Name} beregenerasi dengan cepat sehingga hampir semua luka yang diterimanya menghilang!!")
            jumlahpot[2] -= 1
            userInventory[indexPot[2]][2] = str(int(userInventory[indexPot[2]][2])-1)
            return HP                                      # return nilai HP monster setelah menggunakan potion healing
          else :
            HP = max_HP
            print(f"Potion telah diminum {mons_Name}, {mons_Name} beregenerasi dengan cepat sehingga hampir semua luka yang diterimanya menghilang!!")
            jumlahpot[2] -= 1
            userInventory[indexPot[2]][2] = str(int(userInventory[indexPot[2]][2])-1)
            return HP
        else : 
          print("Potion hanya bisa digunakan sekali")
          return 0
      else :
        print("Sayangnya Anda tidak memiliki potion tersebut, silakan pilih potion lain: ")
        return 0