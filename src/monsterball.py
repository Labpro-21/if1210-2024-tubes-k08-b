from RandomNumberGenerator import *

def monsterball(monsterid,monsterlevel,userinventory,monsterdata,monsterinventory,yourmonsterdata):
    jumlahball = int(userinventory[3][2])
    chance = RNG(1,100)
    print(chance)
    success = 0
    if jumlahball >= 1 :
        for i in yourmonsterdata :
            if i[1]==monsterdata[monsterid][1] :
                print("Anda sudah memiliki monster tersebut!")
                success= 2
                return success
        else :
            print('WHOOSSHHH anda melempar monster ball')
            jumlahball -=1
            userinventory[3][2]=str(jumlahball)
            if monsterlevel==1 :
                if chance>=1 and chance<=75 :
                    print('ANDA DAPAT!!')
                    success = 1
                else :
                    print('yaah ga dapet')
            elif monsterlevel==2 :
                if chance>=1 and chance<=50 :
                    print('ANDA DAPAT!!')
                    success = 1
                else :
                    print('yaah ga dapet')
            elif monsterlevel==3 :
                if chance>=1 and chance<=25 :
                    print('ANDA DAPAT!!')
                    success = 1
                else :
                    print('yaah ga dapet')
            elif monsterlevel==4 :
                if chance>=1 and chance<=10 :
                    print('ANDA DAPAT!!')
                    success = 1
                else :
                    print('yaah ga dapet')
            elif monsterlevel==5 :
                if chance>=1 and chance<=5 :
                    print('ANDA DAPAT!!')
                    success = 1
                else :
                    print('yaah ga dapet')
    else :
        print('Anda tidak memiliki monster ball')
        success = 2
    if success==1 :
        yourmonsterdata.append([userinventory[0][0],monsterdata[monsterid][1],str(monsterlevel)])
        monsterinventory.append([userinventory[0][0],monsterdata[monsterid][1],str(monsterlevel)])
    return success