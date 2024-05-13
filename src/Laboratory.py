import sys
from csvParser import splitSemicolon, csvRead, csvWrite, csvOverwrite, csvDelete
sys.path.append("C:\if1210-2024-tubes-k08-b\data")

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

def inventory (id, userData, monsInvData, monsId, monsData, monsLevel, access, oc):
  upgraded_Coin = ''
  upgraded_Level = ''

  if access == False :
    print('Maaf! Anda tidak memiliki akses sebagai admin')
  elif access == True :
    print(f'Jumlah O.W.C.A. Coin Anda saat ini : {oc}')
    print('============ MONSTER LIST ============')  
    number = 0
    for i in range (1, len(monsData)):
      for j in range (len(monsId)):
        if monsId[j] == int(monsData[i][0]) :
          number += 1
          print(f'{number}. {monsData[i][1]} (LEVEL: {monsLevel[number-1]})')
    array_Harga = [100, 200, 400, 700]
    print('============ UPGRADE PRICE ============')
    for i in range (1,5):
      print(f'{i}. Level {i} -> Level {i+1}: {array_Harga[i-1]}')

    while True: 
      up_monster = input('Pilih monster yang ingin di-upgrade (1/2/dst/Back): ')
      if up_monster.lower() != 'back':
        up_monster = int(up_monster)
        while True: 
          if monsLevel[int(up_monster)-1] != 5: 
            up_level = input('Silakan pilih ke level berapa kah Anda ingin meng-upgrade monster Anda (1/2/dst/Back): ')
            if up_level.lower() != 'back': 
              up_level = int(up_level)
              harga = 0
              for i in range (monsLevel[int(up_monster)-1]-1, int(up_level)-1):
                harga += array_Harga[i]
              print(f'{monsData[int(up_monster)][1]} akan di-upgrade ke level {up_level}')
              print(f'Harga untuk meng-upgrade {monsData[int(up_monster)][1]} adalah {harga}')
              lanjut = input('Lanjutkan upgrade (Y/N): ')
              if lanjut.lower() != 'n':
                if oc >= harga :
                  
                  for i in range (1, len(monsInvData)):
                    if int(monsInvData[i][1]) == monsId[up_monster-1] :
                      for j in range(len(monsInvData[0])):
                        if j != len(monsInvData[0])-1 :
                          upgraded_Level += (monsInvData[i][j] + ';')
                        elif j == len(monsInvData[0])-1 :
                          upgraded_Level += (str(up_level) + '\n')

                  for i in range (1, len(userData)):
                    if int(userData[i][0]) == id :
                      for j in range(len(userData[0])):
                        if j != len(userData[0])-1 :
                          upgraded_Coin += (userData[i][j] + ';')
                        elif j == len(userData[0])-1 :
                          upgraded_Coin += (str(oc-harga) + '\n')
                  
                  print(f'Selamat! {monsData[int(up_monster)][1]} berhasil di-upgrade ke level {up_level}!')
                  print(f'Coin Anda tersisa {oc-harga}')
                  csvOverwrite(r"E:\Documents\Daspro\Tubes\if1210-2024-tubes-k08-b\data\user.csv", 3, upgraded_Coin)
                  csvOverwrite(r"E:\Documents\Daspro\Tubes\if1210-2024-tubes-k08-b\data\monster_inventory.csv", 3, upgraded_Level)
                  break
                else :
                  print('Maaf! Anda tidak memiliki Coin yang cukup')
                  break
              else :
                break
            else :
              break
          else :
            print('Maaf! Monster yang Anda pilih sudah memiliki level maksimum. Silakan pilih monster lain')
            break
      else:     
         break

# contoh penggunaan function : 
inventory(3, user_Data, mons_Inv_Data, monster_Id(3, mons_Inv_Data), monster_Data, monster_Lv(3, mons_Inv_Data), check_Admin(3, user_Data), owca_Coin(3, user_Data))