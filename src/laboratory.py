def laboratory(yourmonsterdata,monsterdata,coin,role):
  if role == 'admin' :  #jika role adalah admin
    print('Maaf! Anda tidak memiliki akses sebagai admin')
  else : #role == 'agent' 
    array_Harga = [100, 200, 400, 700] #list harga untuk mengupgrade level monster

    while True: 
      print(f"JUMLAH COIN ANDA : {coin}")
      #menampilkan seluruh monster yg kita miliki
      print('============ MONSTER LIST ============')
      number=1  
      for i in yourmonsterdata :
        print(f"{number}. {i[1]}, LEVEL :{i[2]}")
        number+=1
      #menampilkan harga untuk mengupgrade ke masing2 level
      print('============ UPGRADE PRICE ============')
      for i in range (1,5):
        print(f'{i}. Level {i} -> Level {i+1}: {array_Harga[i-1]}')
      idpilihan = input('Pilih monster yang ingin di-upgrade (1/2/dst/Back): ')
      #validasi input 
      for i in range(len(yourmonsterdata)) :
         if idpilihan== str(i+1) or idpilihan.lower()=='back' :
            break  #jika input benar
      else :  #jika input salah
         print("Monster tersebut tidak tersedia")
         continue
      
      if idpilihan.lower() != 'back':
        idpilihan = int(idpilihan)
        while True: 
          if yourmonsterdata[idpilihan-1][2] != '5':   #jika monster tidak maks level
            up_level = input('Silakan pilih ke level berapa kah Anda ingin meng-upgrade monster Anda (1/2/dst/Back): ')
            #periksa apakah input berupa int dari 1-5 atau back
            for i in range(5) :
               if up_level == str(i+1) or up_level.lower()=='back' :
                  break
            else :
               print("Masukkan level yg dituju dengan benar")
               continue
            
            if up_level.lower() != 'back': 
              if up_level <= yourmonsterdata[idpilihan-1][2] : #jika level yg dituju sudah tercapai
                print("masa mau upgrade kelevel yg sama/lebihrendah si")
                continue
              else :   #jika input benar dan sesuai
                up_level = int(up_level)
                harga = 0
                #menghitung harga yg dibutuhkan
                for i in range (int(yourmonsterdata[idpilihan-1][2]), up_level):
                    harga += array_Harga[i-1]
                print(f'{yourmonsterdata[idpilihan-1][1]} akan di-upgrade ke level {up_level}')
                print(f'Harga untuk meng-upgrade {yourmonsterdata[idpilihan-1][1]} adalah {harga}')
                while True :  #double cek apakah benar mau di upgarde
                  lanjut = input('Lanjutkan upgrade (Y/N): ')
                  if lanjut.lower() == 'y':
                      if coin >= harga :   #jika coin cukup
                          yourmonsterdata[idpilihan-1][2]=str(up_level)
                          coin -= harga
                          print(f'Selamat! {yourmonsterdata[idpilihan-1][1]} berhasil di-upgrade ke level {up_level}!')
                          print(f'Coin Anda tersisa {coin}')
                          break
                      else :  #jika tidak cukup
                          print('Maaf! Anda tidak memiliki Coin yang cukup')
                          break
                  elif lanjut.lower() == 'n' :   #jika tidak jadi upgrade
                      break
                  else :   #jika input bukan y atau n
                     print("Mohon masukkan input yang benar")
                     continue
                break
                   
            else : #jika input == break
                break
          else :  #jika sudah maks level
            print('Maaf! Monster yang Anda pilih sudah memiliki level maksimum. Silakan pilih monster lain')
            break
      else:     
         break
  return coin

