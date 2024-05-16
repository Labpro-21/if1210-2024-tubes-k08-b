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


'''user_Data = csvRead("data/data1/user.csv")  
pot_Inv_Data = csvRead(r"E:\Documents\Daspro\Tubes\if1210-2024-tubes-k08-b\data\item_inventory.csv")
monster_Data = csvRead(r"E:\Documents\Daspro\Tubes\if1210-2024-tubes-k08-b\data\monster.csv")
mons_Inv_Data = csvRead(r"E:\Documents\Daspro\Tubes\if1210-2024-tubes-k08-b\data\monster_inventory.csv")'''

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
      
'''def pot_Inventory (userinventory):
    for i in userinventory:
        if i[1]=='strenghpotion':
            jumlahstr=i[2]
            break
    else : jumlahstr = 0
    for i in userinventory:
       if i[1]=='respotion' :
            jumlahres=i[2]
            break
    else : jumlahres = 0
    for i in userinventory:
        if i[1]=='healingpotion' :
           jumlahheal=i[2]
           break
    else : jumlahheal = 0
    return [jumlahstr,jumlahres,jumlahheal]

def pot_List (qty): 
    pot_Type = ['ATK', 'DEF', 'HEAL']
    pot_Type_2 = []
    pot_Qty =[]
    for i in range (3): 
        if qty[i] != 0 :
            pot_Type_2.append(pot_Type[i])
            pot_Qty.append(qty[i])
    return (pot_Type_2, pot_Qty)

def monster_Id (yourmonsterdata):
    mons_Id_Array = []
    for i in yourmonsterdata :
       mons_Id_Array.append(i[1])
    return mons_Id_Array

def monster_Lv (yourmonsterdata):
    mons_Lv_Array = []
    for i in yourmonsterdata :
       mons_Lv_Array.append(i[2])
    return mons_Lv_Array'''

def inventoryy(userinventory,yourmonsterdata,monsterdata,role,coin) :
    if role=='admin':
        print("Maaf! Anda tidak memiliki akses sebagai admin")
    else :
        print(f'jumlah OWCA coin anda saat ini : {coin}')
        while True :
            check = input('Silakan pilih jenis item yang ingin diketahui Anda (Monster/Item/Back): ')
            if check.lower() == 'item' :
                x=1
                types=[]
                for i in userinventory:
                    if i[1] == 'strenghpotion' :
                        type = 'ATK potion'
                    elif i[1] == 'respotion' :
                        type = 'DEF potion'
                    elif i[1] == 'healingpotion' :
                        type = 'HEAL potion'
                    elif i[1] == 'monsterball' :
                        type = 'MONSTER BALL'
                    types.append(type)
                    print(f'{x}. Type: {type}')
                    x+=1
                while True :
                    pot_Number = input('Masukkan nomor potion untuk menampilkan detail item (1/2/3/Back): ')
                    if pot_Number.lower() != 'back':
                        pot_Number = int(pot_Number)
                        print(f'Type: {types[pot_Number-1]}')
                        print(f'Quantity: {userinventory[pot_Number-1][2]}')
                    else :
                        break
            elif check.lower() == 'monster' :
                y = 0
                for i in yourmonsterdata :
                    print(f"{y+1}. {i[1]}")
                    y+=1
                while True :
                    mons_Number = input('Masukkan nomor monster untuk menampilkan detail monster (1/2/dst/Back): ')
                    if mons_Number.lower() != 'back' :
                        mons_Number = int(mons_Number)
                        monsterlvl = int(yourmonsterdata[mons_Number-1][2])
                        for i in monsterdata :
                            if i[1]==yourmonsterdata[mons_Number-1][1] :
                                print(f'Nama      : {i[1]}')
                                print(f'ATK Power : {int(i[2])+(monsterlvl-1)*(5/100)*(int(i[2]))}')
                                print(f'DEF Power : {int(i[3])+(monsterlvl-1)*(5/100)*(int(i[3]))}')
                                print(f'HP        : {int(i[4])+(monsterlvl-1)*(5/100)*(int(i[4]))}')
                                print(f'Level     : {monsterlvl}')
                    else :
                        break
            elif check.lower() == 'back' :
                break 

'''def inventory (monsId, monsData, potData, monsLevel, access, oc):
  if access == False :
    print('Maaf! Anda tidak memiliki akses sebagai admin')
  elif access == True :
    print(f'Jumlah O.W.C.A. Coin Anda saat ini : {oc}')
    while True :
      check = input('Silakan pilih jenis item yang ingin diketahui Anda (Monster/Potion/Back): ')
      if check.lower() == 'potion' :
        for i in range(len(potData[0])):
          print(f'{i+1}. Type: {potData[0][i]}')
        
        while True :
          pot_Number = input('Masukkan nomor potion untuk menampilkan detail item (1/2/3/Back): ')
          if pot_Number.lower() != 'back':
            pot_Number = int(pot_Number)
            print('POTION')
            print(f'Type: {potData[0][pot_Number-1]}')
            print(f'Quantity: {potData[1][pot_Number-1]}')
          else :
            break

      elif check.lower() == 'monster' :
        number = 0
        for i in range (1, len(monsData)):
          for j in range (len(monsId)):
            if monsId[j] == int(monsData[i][0]) :
              number += 1
              print(f'{number}. {monsData[i][1]}')
      
        while True :
          mons_Number = input('Masukkan nomor monster untuk menampilkan detail monster (1/2/dst/Back): ')
          if mons_Number.lower() != 'back' :
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
      elif check.lower() == 'back' :
        break      '''

# contoh penggunaan function : 
#inventory(monster_Id(3, mons_Inv_Data), monster_Data, pot_List(pot_Inventory(3, pot_Inv_Data)),monster_Lv(3, mons_Inv_Data), check_Admin(3, user_Data), owca_Coin(3, user_Data))