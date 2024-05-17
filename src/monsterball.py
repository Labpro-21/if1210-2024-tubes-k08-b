from RandomNumberGenerator import *

# Fungsi untuk fitur bonus Monster Ball
def monsterball(monsterid,monsterlevel,userinventory,monsterdata,monsterinventory,yourmonsterdata):
    jumlahball = int(userinventory[3][2])
    chance = RNG(1,100)
    print(chance)
    success = 0
    if jumlahball >= 1 : # Cek apakah player memiliki monster bal;
        for i in yourmonsterdata : # Looping untuk cek apakah monster yang ingin ditangkap sudah ada di inventory
            if i[1]==monsterdata[monsterid][1] : # bila monster sudah dimiliki player
                print("Anda sudah memiliki monster tersebut!")
                success= 2
                return success
        else : # bila monster tidak dimiliki player
            print('WHOOSSHHH anda melempar monster ball')
            jumlahball -=1 # 1 bola sudah digunakan
            userinventory[3][2]=str(jumlahball)
            if monsterlevel==1 : # bila monster yang dilawan level 1, maka chance player mendapatkan monster tersebut 75%
                if chance>=1 and chance<=75 :
                    print('ANDA DAPAT!!')
                    success = 1
                else : 
                    print('yaah ga dapet')
            elif monsterlevel==2 : # monster level 2, chance 50%
                if chance>=1 and chance<=50 :
                    print('ANDA DAPAT!!')
                    success = 1
                else :
                    print('yaah ga dapet')
            elif monsterlevel==3 : # monster level 3, chance 25%
                if chance>=1 and chance<=25 :
                    print('ANDA DAPAT!!')
                    success = 1
                else :
                    print('yaah ga dapet')
            elif monsterlevel==4 : # monster level 4, chance 10%
                if chance>=1 and chance<=10 :
                    print('ANDA DAPAT!!')
                    success = 1
                else :
                    print('yaah ga dapet')
            elif monsterlevel==5 : # monster level 5, chance 5%
                if chance>=1 and chance<=5 :
                    print('ANDA DAPAT!!')
                    success = 1
                else :
                    print('yaah ga dapet')
    else : # Player tidak memiliki monster ball
        print('Anda tidak memiliki monster ball')
        success = 2
    if success==1 : # success = 1 berarti monster success ditangkap dan monster ditambah ke inventory player
        yourmonsterdata.append([userinventory[0][0],monsterdata[monsterid][1],monsterlevel])
        monsterinventory.append([userinventory[0][0],monsterdata[monsterid][1],monsterlevel])
    return success