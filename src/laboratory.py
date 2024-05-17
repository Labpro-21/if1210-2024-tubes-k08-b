
'''from csvParser import splitSemicolon, csvRead, csvWrite, csvOverwrite, csvDelete'''


    
'''def check_Admin (id, userData):
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
  return mons_Lv_Array'''

def laboratory(yourmonsterdata,monsterdata,coin,role):
  if role == 'admin' :
    print('Maaf! Anda tidak memiliki akses sebagai admin')
  elif role == 'agent' :
    print(f'Jumlah O.W.C.A. Coin Anda saat ini : {coin}')
    print('============ MONSTER LIST ============')  
    for i in yourmonsterdata :
      index=0
      for j in monsterdata :
         if j[1]==i[1] :
            break
         else :
            index+=1
      print(f"{index}. {i[1]}, LEVEL :{i[2]}")
    array_Harga = [100, 200, 400, 700]
    print('============ UPGRADE PRICE ============')
    for i in range (1,5):
      print(f'{i}. Level {i} -> Level {i+1}: {array_Harga[i-1]}')

    while True: 
      idpilihan = input('Pilih monster yang ingin di-upgrade (1/2/dst/Back): ')
      if idpilihan.lower() != 'back':
        idpilihan = int(idpilihan)
        while True: 
          if yourmonsterdata[idpilihan-1][2] != 5: 
            up_level = input('Silakan pilih ke level berapa kah Anda ingin meng-upgrade monster Anda (1/2/dst/Back): ')
            if up_level.lower() != 'back': 
              if up_level == yourmonsterdata[idpilihan-1][2] :
                print("masa mau upgrade kelevel yg sama si")
                break
              else :
                up_level = int(up_level)
                harga = 0
                for i in range (int(yourmonsterdata[idpilihan-1][2]), up_level):
                    harga += array_Harga[i-1]
                print(f'{yourmonsterdata[idpilihan-1][1]} akan di-upgrade ke level {up_level}')
                print(f'Harga untuk meng-upgrade {yourmonsterdata[idpilihan-1][1]} adalah {harga}')
                lanjut = input('Lanjutkan upgrade (Y/N): ')
                if lanjut.lower() != 'n':
                    if coin >= harga :
                        yourmonsterdata[idpilihan-1][2]=str(up_level)
                        coin -= harga
                        print(f'Selamat! {yourmonsterdata[idpilihan-1][1]} berhasil di-upgrade ke level {up_level}!')
                        print(f'Coin Anda tersisa {coin}')
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
  return coin

# contoh penggunaan function : 
#inventory(3, user_Data, mons_Inv_Data, monster_Id(3, mons_Inv_Data), monster_Data, monster_Lv(3, mons_Inv_Data), check_Admin(3, user_Data), owca_Coin(3, user_Data))