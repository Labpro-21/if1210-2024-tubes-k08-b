def laboratory(yourMonsData, coin, role):
  if role != 'admin' :
    arrayHarga = [100, 200, 400, 700]                                              # list harga untuk meng-upgrade level monster

    while True: 
      print(f"JUMLAH COIN ANDA : {coin}")
      print('============ MONSTER LIST ============')
      number = 1  
      for i in yourMonsData :
        print(f"{number}. {i[1]} LEVEL: {i[2]}")
        number += 1

      print('============ UPGRADE PRICE ============')
      for i in range (1,5):
        print(f'{i}. Level {i} --> Level {i+1}: {arrayHarga[i-1]}')

      pilihMons = input('Pilih monster yang ingin di-upgrade (1/2/dst/Back): ')
      
      inputMonsNum = True                                                           # validasi input selain 1/2/3/dst/back
      for char in str(pilihMons) :
        if ord(char) < ord('0') or ord(char) > ord('9'):
          inputMonsNum = False
      
      if inputMonsNum != False :
        pilihMons = int(pilihMons)
        while True: 
          if yourMonsData[pilihMons-1][2] != '5':  
            monsUpgrade = input('Silakan pilih ke level berapa kah Anda ingin meng-upgrade monster Anda (1/2/dst/Back): ')
            
            inputMonsUp = True                                                      # validasi input selain 1/2/3/dst/back
            for char in str(monsUpgrade) :
              if ord(char) < ord('0') or ord(char) > ord('9'):
                inputMonsUp = False
                  
            if inputMonsUp != False : 
              if monsUpgrade <= yourMonsData[pilihMons-1][2] :                      # validasi input upgrade level <= level saat ini
                print("Masa mau upgrade ke level yg sama/lebih rendah sih.. Itu mah downgrade kak")

              elif int(monsUpgrade) > 5 :
                print('Upgrade cuman sampai level 5 kakak, level di atas 5 itu level kesulitan tubes daspro')

              else :
                monsUpgrade = int(monsUpgrade)
                harga = 0
                for i in range (int(yourMonsData[pilihMons-1][2]), monsUpgrade):    # total harga upgrade
                  harga += arrayHarga[i-1]

                print(f'{yourMonsData[pilihMons-1][1]} akan di-upgrade ke level {monsUpgrade}')
                print(f'Harga untuk meng-upgrade {yourMonsData[pilihMons-1][1]} adalah {harga}')

                while True :  
                  lanjut = input('Lanjutkan upgrade (Y/N): ')                        # konfirmasi upgrade
                  if lanjut.lower() == 'y':
                      if coin >= harga :  
                        yourMonsData[pilihMons-1][2] = str(monsUpgrade)
                        coin -= harga
                        print(f'Selamat! {yourMonsData[pilihMons-1][1]} berhasil di-upgrade ke level {monsUpgrade}!')
                        print(f'Coin Anda tersisa {coin}')
                        break
                      else : 
                        print('Maaf! Anda tidak memiliki Coin yang cukup')
                        break
                  elif lanjut.lower() == 'n' : 
                    break
                  else : 
                    print("Mohon masukkan input yang benar")
                    print()

            elif monsUpgrade.lower() == 'back' :
              break
            else :
              print("Masukkan input level yang benar")
              print()
          else :                                                                     # jika level sudah max
            print('Maaf! Monster yang Anda pilih sudah memiliki level maksimum. Silakan pilih monster lain')
            break
      elif pilihMons.lower() == 'back' :
        print("Sampai bertemu lagi !")
        break
      else :     
        print("Masukkan nomor monster yang benar")
        print()
  else :
    print('Maaf! Anda tidak memiliki akses sebagai admin')

  return coin