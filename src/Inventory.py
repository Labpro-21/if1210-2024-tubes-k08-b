import sys
sys.path.append("C:\if1210-2024-tubes-k08-b\data")

def splitSemicolon(text):                                                  # Fungsi mirip .split() namun untuk string dengan pemisah semicolon saja
    separated = []
    word = ''
    
    for char in (text):
        if char == '\n' :                                                  # jika "\n" (newline), pengecekan berhenti (agar newline tidak masuk ke array)
            break
        elif char != ';':
            word += char                                                   # jika bukan ";", huruf akan digabung satu persatu menjadi sebuah kata
        else: # char == ";"
            separated.append(word)                                         # jika ";", maka kata yang telah terbentuk akan dimasukkan dalam array
            word = ''                                                      # kemudian kata akan dikosongkan kembali (semicolon dilewat)
    
    separated.append(word)                                                 # Untuk kata setelah semicolon terakhir
    
    return separated

def csvRead(path):                                                         # Fungsi membaca file .csv baris per baris
    csvOpen = open(path,'r')                                               # Membuka file .csv
    cleanData = []
    
    for row in csvOpen:                                                    # Membaca setiap baris
        cleanData.append(splitSemicolon(row))                              # Memisahkan kalimat dari semicolon
    
    csvOpen.close()                                                        # Menutup file
    return cleanData

user_Data = csvRead(r"E:\Documents\Daspro\Tubes\if1210-2024-tubes-k08-b\data\user.csv")  
pot_Inv_Data = csvRead(r"E:\Documents\Daspro\Tubes\if1210-2024-tubes-k08-b\data\item_inventory.csv")
monster_Data = csvRead(r"E:\Documents\Daspro\Tubes\if1210-2024-tubes-k08-b\data\monster.csv")
mons_Inv_Data = csvRead(r"E:\Documents\Daspro\Tubes\if1210-2024-tubes-k08-b\data\monster_inventory.csv")
    
def check_Admin (id, userData):
  for i in range (1, len(userData)):
    if id == int(userData[i][0]) :
      if userData[i][3] == 'admin' :
        return False
      else : 
        return True

def owca_Coin (id, userData):
    for i in range (1, len(userData)):
      if id == int(userData[i][0]) :
         return int(userData[i][4])
      
def pot_Inventory (id, potInvData):
  array_Pot = [0, 0, 0]                                                    # array_Pot adalah array dengan isi yaitu [jumlah potion strength, jumlah potion resilience, jumlah potion heal]
  
  for i in range (1, len(potInvData)):
    potInvData[i][0] = int(potInvData[i][0])
    potInvData[i][2] = int(potInvData[i][2]) 

  for i in range (len(potInvData)):
    if potInvData[i][0] == id :
      if potInvData[i][1] == 'strength' :
        array_Pot[0] = potInvData[i][2]

      elif potInvData[i][1] == 'resilience' :
        array_Pot[1] = potInvData[i][2]

      elif potInvData[i][1] == 'heal' :
        array_Pot[2] = potInvData[i][2]
  return array_Pot

def pot_List (qty): 
  pot_Type = ['ATK', 'DEF', 'HEAL']
  pot_Type_2 = []
  pot_Qty =[]
  for i in range (3): 
    if qty[i] != 0 :
       pot_Type_2.append(pot_Type[i])
       pot_Qty.append(qty[i])
  return (pot_Type_2, pot_Qty)

def monster_Id (id, monsInvData):
  mons_Id_Array = []
  for i in range (1, len(monsInvData)):
    if int(monsInvData[i][0]) == id :
      mons_Id_Array.append(int(monsInvData[i][1]))
  return mons_Id_Array

def monster_Lv (id, monsInvData):
  mons_Lv_Array = []
  for i in range (1, len(monsInvData)):
    if int(monsInvData[i][0]) == id :
      mons_Lv_Array.append(int(monsInvData[i][2]))
  return mons_Lv_Array

def inventory (monsId, monsData, potData, monsLevel, access, oc):
  if access == False :
    print('Maaf! Anda tidak memiliki akses sebagai admin')
  elif access == True :
    print(f'Jumlah O.W.C.A. Coin Anda saat ini : {oc}')
    while True :
      check = input('Silakan pilih jenis item yang ingin diketahui Anda (Monster/Potion): ')
      if check == 'potion' :
        for i in range(len(potData[0])):
          print(f'{i+1}. Type: {potData[0][i]}')
        
        while True :
          pot_Number = input('Masukkan nomor potion untuk menampilkan detail item (1/2/3/Back): ')
          if pot_Number != 'Back' :
            pot_Number = int(pot_Number)
            print('POTION')
            print(f'Type: {potData[0][pot_Number-1]}')
            print(f'Quantity: {potData[1][pot_Number-1]}')
          else :
            break

      elif check == 'monster' :
        number = 0
        for i in range (1, len(monsData)):
          for j in range (len(monsId)):
            if monsId[j] == int(monsData[i][0]) :
              number += 1
              print(f'{number}. {monsData[i][1]}')
      
        while True :
          mons_Number = input('Masukkan nomor monster untuk menampilkan detail monster (1/2/dst/Back): ')
          if mons_Number != 'Back' :
            mons_Number = int(mons_Number)
            print('MONSTER')
            for i in range (1, len(monsData)):
              if int(monsData[i][0]) == monsId[mons_Number-1] :
                print(f'Nama      : {monsData[i][1]}')
                print(f'ATK Power : {int(monsData[i][2]) + (int(monsData[i][2])*(monsLevel[mons_Number-1]-1)*0.1)}')
                print(f'DEF Power : {int(monsData[i][3]) + (int(monsData[i][3])*(monsLevel[mons_Number-1]-1)*0.1)}')
                print(f'HP        : {int(monsData[i][4]) + (int(monsData[i][4])*(monsLevel[mons_Number-1]-1)*0.1)}')
                print(f'Level     : {monsLevel[mons_Number-1]}')
          else :
            break

# contoh penggunaan function : inventory(monster_Id(3, mons_Inv_Data), monster_Data, pot_List(pot_Inventory(3, pot_Inv_Data)),monster_Lv(3, mons_Inv_Data), check_Admin(3, user_Data), owca_Coin(3, user_Data))