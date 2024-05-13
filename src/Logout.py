def logout (loginValid):
  if loginValid == False :
    print('Logout GAGAL!')
    print('Anda belum login, silakan login terlebih dahulu')
  else :
    loginValid = False

# contoh penggunaan function : 
logout(True)