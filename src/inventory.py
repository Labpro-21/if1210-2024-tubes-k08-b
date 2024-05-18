def inventoryy(userinventory,yourmonsterdata,monsterdata,role,coin) :
    if role=='admin':  #jika role player adalah admin
        print("Maaf! Anda tidak memiliki akses sebagai admin")
    else :
        print(f'jumlah OWCA coin anda saat ini : {coin}')
        while True :
            check = input('Silakan pilih jenis item yang ingin diketahui Anda (Monster/Item/Back): ')
            if check.lower() == 'item' :
                number=1
                types=[]  #list untuk type dari item yang tersedia
                for i in userinventory:
                    if i[1] == 'Strength Potion' :
                        type = 'ATK potion'
                    elif i[1] == 'Resilience Potion' :
                        type = 'DEF potion'
                    elif i[1] == 'Healing Potion' :
                        type = 'HEAL potion'
                    elif i[1] == 'Monster Ball' :
                        type = 'MONSTER BALL'
                    types.append(type)
                    print(f'{number}. Type: {type}')
                    number+=1
                while True :        
                    item_Number = input('Masukkan nomor item untuk menampilkan detail item (1/2/3/Back): ')
                    #cek apakah input sudah benar (yaitu 1/2/3/4)
                    if item_Number.lower() != 'back':
                        for i in range(4) :
                            if item_Number == str(i+1) :
                                break   #jika output benar
                        else :  #jika output salah
                            print('Nomor item tersebut tidak tersedia')
                            continue
                        item_Number = int(item_Number)
                        #menampilkan type dan jumlah item
                        print(f'Type: {types[item_Number-1]}')
                        print(f'Quantity: {userinventory[item_Number-1][2]}')
                    else : #jika input = back
                        break
            elif check.lower() == 'monster' :
                y = 0
                #menampilkan seluruh monster yang kita punya
                for i in yourmonsterdata :
                    print(f"{y+1}. {i[1]}")
                    y+=1
                while True :
                    mons_Number = input('Masukkan nomor monster untuk menampilkan detail monster (1/2/dst/Back): ')
                    if mons_Number.lower() != 'back' :
                        #validasi apakah input sudah benar (1,2,3,..len(monsterkita))
                        for i in range(len(yourmonsterdata)) :
                            if mons_Number == str(i+1) :
                                break  #jika input sudah benar
                        else :  #jika input salah
                            print("Nomor monster tersebut tidak tersedia")
                            continue
                        mons_Number=int(mons_Number)
                        monsterlvl = int(yourmonsterdata[mons_Number-1][2])
                        #menampilkan stats dari monster yg dipilih
                        for i in monsterdata :
                            if i[1]==yourmonsterdata[mons_Number-1][1] :
                                print(f'Nama      : {i[1]}')
                                print(f'ATK Power : {int(i[2])+(monsterlvl-1)*(5/100)*(int(i[2]))}')
                                print(f'DEF Power : {int(i[3])+(monsterlvl-1)*(5/100)*(int(i[3]))}')
                                print(f'HP        : {int(i[4])+(monsterlvl-1)*(5/100)*(int(i[4]))}')
                                print(f'Level     : {monsterlvl}')
                    else : #jika input == break
                        break
            elif check.lower() == 'back' :
                break 
            else :  #jika input salah
                print("Jenis item tersebut tidak ada")