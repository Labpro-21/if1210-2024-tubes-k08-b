def inventory(userInventory, yourMonsData, monsterData, role, coin) :
    if role == 'admin':
        print("Maaf! Anda tidak memiliki akses sebagai admin")
    else :
        print(f'jumlah OWCA coin anda saat ini : {coin}')
        while True :
            check = input('Silakan pilih jenis item yang ingin diketahui Anda (Monster/Item/Back): ')
            if check.lower() == 'item' :
                number = 1
                itemArray = []                  
                for i in userInventory:
                    itemArray.append(i[1])
                    print(f'{number}. {i[1]}')
                    number += 1

                while True :        
                    itemNumber = input('Masukkan nomor item untuk menampilkan detail item (1/2/3/Back): ')
                    inputNum = True                                                  # validasi input selain 1/2/3/dst/back
                    for char in itemNumber:
                        if ord(char) < ord('0') or ord(char) > ord('9'):
                            inputNum = False
                            
                    if inputNum != False :
                        if itemNumber.lower() != 'back' :
                            if int(itemNumber) > len(itemArray) : 
                                print('Nomor item tersebut tidak tersedia')           # validasi input nomor item yang salah
                            else :
                                itemNumber = int(itemNumber)
                                print(f'Type: {itemArray[itemNumber-1]}')
                                print(f'Quantity: {userInventory[itemNumber-1][2]}')
                    elif itemNumber.lower() == 'back' :
                        break
                    else :
                        print('Masukkan input yang benar')                            # validasi input itemNumber yang salah

            elif check.lower() == 'monster' :
                number = 1
                for i in yourMonsData :
                    print(f"{number}. {i[1]}")
                    number += 1

                while True :
                    monsNumber = input('Masukkan nomor monster untuk menampilkan detail monster (1/2/dst/Back): ')
                    inputNum = True
                    for char in monsNumber:
                        if ord(char) < ord('0') or ord(char) > ord('9'):
                            inputNum = False

                    if inputNum != False :
                        if monsNumber.lower() != 'back':
                            if int(monsNumber) > len(yourMonsData) or int(monsNumber) < 1: 
                                print('Nomor monster tersebut tidak tersedia')
                            else :
                                monsNumber = int(monsNumber)
                                monsLevel = int(yourMonsData[monsNumber-1][2])
                                for i in monsterData :
                                    if i[1] == yourMonsData[monsNumber-1][1] :
                                        print(f'Nama      : {i[1]}')
                                        print(f'ATK Power : {int(i[2])+(monsLevel-1)*(5/100)*(int(i[2]))}')
                                        print(f'DEF Power : {int(i[3])+(monsLevel-1)*(5/100)*(int(i[3]))}')
                                        print(f'HP        : {int(i[4])+(monsLevel-1)*(5/100)*(int(i[4]))}')
                                        print(f'Level     : {monsLevel}')
                    elif monsNumber.lower() == 'back' :
                        break                
                    else :
                        print('Masukkan input yang benar')

            elif check.lower() == 'back' :
                break 

            else :
                print("Mohon berikan input yang benar")