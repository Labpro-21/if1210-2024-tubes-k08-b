#FUNGI UNTUK MENGHITUNG JUMLAH MASING MASING POTION
def jumlahpot(userinventory) :
  for i in userinventory :
    if i[1]=='Strength Potion' :
      jumlahstr = i[2]
      break
  else : jumlahstr = 0
  for i in userinventory :
    if i[1]=='Resilience Potion' :
      jumlahres = i[2]
      break
  else : jumlahres = 0
  for i in userinventory :
    if i[1]=='Healing Potion' :
      jumlahheal = i[2]
      break
  else : jumlahheal = 0
  return [int(jumlahstr),int(jumlahres),int(jumlahheal)] #RETURN LIST MASING MASING JUMLAH POTION

#FUNGSI MENCARI INDEKS LOKASI POTION DI INVENTORY
def lokasipot(userinventory) :
  x=0
  for i in userinventory :
    if i[1]=='Strength Potion' :
      break
    x+=1
  else : x=999
  y=0
  for i in userinventory :
    if i[1]=='Resilience Potion' :
      break
    y+=1
  else : y=999
  z=0
  for i in userinventory :
    if i[1]=='Healing Potion' :
      break
    z+=1
  else : x=999
  return [x,y,z] #RETURN INDEKS POTION DI INVENTORY

def potion(jumlahpot,lokasipot,used_Pot_Array, userinventory, attack, defense, HP, max_HP, mons_Name, pilihan):
    if pilihan==1 :   #PILIHAN 1 ADALAH STR POTION
      if int(jumlahpot[0])> 0 :
        if used_Pot_Array[0] == 0 :
          used_Pot_Array[0] += 1   #MENANDAKAN POTION SUDAH DIPAKE DAN TIDAK BISA DIPAKE LAGI
          attack *= 110/100  #ATTACK BERTAMBAH 10 PERSEN
          print(f"Potion telah diminum {mons_Name}, {mons_Name} menjadi lebih kuat!!")
          jumlahpot[0] -= 1  #JUMLAH STR POTION BERKURANG SATU
          userinventory[lokasipot[0]][2]=str(int(userinventory[lokasipot[0]][2])-1)
          return attack
        else :
          print(f"Potion hanya bisa digunakan sekali")  #POTION SUDAH DIGUNAKAN
          return 0
      else :  #POTION TIDAK ADA
        print("Sayangnya Anda tidak memiliki potion tersebut, silakan pilih potion lain: ")  
        return 0
      
    elif pilihan==2 :   #PILIHAN 2 ADALAH RES POTION
      if int(jumlahpot[1]) > 0 :
        if used_Pot_Array[1] == 0 :
          used_Pot_Array[1] += 1
          defense *= 110/100   #DEFENSE BERTAMBAH 10 PERSEN
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
    elif pilihan==3 :  #PILIHAN 3 ADALAH HEAL POTION
      if int(jumlahpot[2]) > 0 :
        if used_Pot_Array[2] == 0 :
          used_Pot_Array[2] += 1
          if HP * 125/100 <= max_HP :  #JIKA HP + 25PERSEN TIDAK MELAMPAU MAKS HP(HP AWAL)
            HP *= 125/100
            print(f"Potion telah diminum {mons_Name}, {mons_Name} beregenerasi dengan cepat sehingga hampir semua luka yang diterimanya menghilang!!")
            jumlahpot[2] -=1
            userinventory[lokasipot[2]][2]=str(int(userinventory[lokasipot[2]][2])-1)
            return HP
          else : #JIKA MELAMPAU MAKS HP MAKA HEAL HANYA AKAN SAMPAI MAKS HP
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