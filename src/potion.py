from readwritecsv import *

def jumlahpot(userinventory) :
  for i in userinventory :
    if i[1]=='strenghpotion' :
      jumlahstr = i[2]
      break
  else : jumlahstr = 0
  for i in userinventory :
    if i[1]=='respotion' :
      jumlahres = i[2]
      break
  else : jumlahres = 0
  for i in userinventory :
    if i[1]=='healingpotion' :
      jumlahheal = i[2]
      break
  else : jumlahheal = 0
  return [int(jumlahstr),int(jumlahres),int(jumlahheal)]

def lokasipot(userinventory) :
  x=0
  for i in userinventory :
    if i[1]=='strenghpotion' :
      break
    x+=1
  else : x=999
  y=0
  for i in userinventory :
    if i[1]=='respotion' :
      break
    y+=1
  else : y=999
  z=0
  for i in userinventory :
    if i[1]=='healingpotion' :
      break
    z+=1
  else : x=999
  return [x,y,z]

                                    # used_Pot_Array adalah array untuk menunjukkan apakah sebuah potion telah digunakan sekali dalam battle dengan used_Pot_Array [jumlah strength potion digunakan, jumlah resilience potion digunakan, jumlah heal potion digunakan]
def potion(jumlahpot,lokasipot,used_Pot_Array, userinventory, attack, defense, HP, max_HP, mons_Name, pilihan):
    if pilihan==1 :
      if int(jumlahpot[0])> 0 :
        if used_Pot_Array[0] == 0 :
          used_Pot_Array[0] += 1
          attack *= 105/100
          print(f"Potion telah diminum {mons_Name}, {mons_Name} menjadi lebih kuat!!")
          jumlahpot[0] -= 1
          userinventory[lokasipot[0]][2]=str(int(userinventory[lokasipot[0]][2])-1)
          return attack
        else :
          print(f"Potion hanya bisa digunakan sekali")
          return 0
      else :
        print("Sayangnya Anda tidak memiliki potion tersebut, silakan pilih potion lain: ")
        return 0
      
    elif pilihan==2 :
      if int(jumlahpot[1]) > 0 :
        if used_Pot_Array[1] == 0 :
          used_Pot_Array[1] += 1
          defense *= 105/100
          print(f"Potion telah diminum {mons_Name}, {mons_Name} menjadi lebih sulit dilukai!!")
          jumlahpot[1] -=1
          userinventory[lokasipot[1]][2]=str(int(userinventory[lokasipot[1]][2])-1)
          return defense
        else : 
          print(f"Potion hanya bisa digunakan sekali")
          return 0
      else :
        print("Sayangnya Anda tidak memiliki potion tersebut, silakan pilih potion lain: ")
        return 0
    elif pilihan==3 :
      if int(jumlahpot[2]) > 0 :
        if used_Pot_Array[2] == 0 :
          used_Pot_Array[2] += 1
          if HP * 125/100 <= max_HP :
            HP *= 125/100
            print(f"Potion telah diminum {mons_Name}, {mons_Name} beregenerasi dengan cepat sehingga hampir semua luka yang diterimanya menghilang!!")
            jumlahpot[2] -=1
            userinventory[lokasipot[2]][2]=str(int(userinventory[lokasipot[2]][2])-1)
            return HP
          else :
            HP = max_HP
            print(f"Potion telah diminum {mons_Name}, {mons_Name} beregenerasi dengan cepat sehingga hampir semua luka yang diterimanya menghilang!!")
            jumlahpot[2] -=1
            userinventory[lokasipot[2]][2]=str(int(userinventory[lokasipot[2]][2])-1)
            return HP
        else : 
          print(f"Potion hanya bisa digunakan sekali")
          return 0
      else :
        print("Sayangnya Anda tidak memiliki potion tersebut, silakan pilih potion lain: ")
        return 0
      
  

# contoh penggunaan function : potion(pot_Inventory (2, csvRead("E:\Documents\Daspro\Tubes\if1210-2024-tubes-k08-b\item_inventory.csv")), used_Pot_Array, 10, 20, 30, 100, "Zuko")