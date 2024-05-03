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

def csvWrite(path, input):                                                 # Fungsi memasukkan data dengan line baru pada csv
    with open(path,'a', newline="") as csvOpen:                            # Membuka csv (dengan with, file tidak perlu diclose)
        csvOpen.write('\n')
        csvOpen.write(''.join(input))                                      # Mengisi baris baru dengan input
    return

def csvOverwrite(path, row, input):                                        # Fungsi memperbaharui data yang sudah ada dengan data baru
    csvOpen = open(path,'r')                                               # Membuka csv
    tempData = []                                                          # Data sementara
    for i in csvOpen:
        tempData.append(i)                                                 # Mengisi list dengan data pada csv tanpa menghilangkan semicolon (";")
    tempData[row] = input                                                  # Mengubah data csv pada baris yang ditentukan dengan input yang baru
    
    with open(path,'w') as csvWrite:                                       # Mengembalikan bentuk list menjadi bentuk csv semula
        for rows in tempData:
            tempData = csvWrite.write(''.join(rows))
    return

def csvDelete(path, row):                                                  # Fungsi menghapus data pada baris yang ditentukan
    csvOpen = open(path,'r')                                               # Membuka csv
    tempData = []                                                          # Data sementara
    count = 0
    for i in csvOpen:
        tempData.append(i)                                                 # Mengisi list dengan data tanpa menghilangkan semicolon (";")
        if count == row:                                                   # Pada baris yang ditentukan, data di-pop (dihapus)
            tempData.pop(row)
        count += 1
    
    with open(path,'w') as csvWrite:                                       # Mengembalikan bentuk list menjadi bentuk csv semula
        for rows in tempData:
            tempData = csvWrite.write(''.join(rows))
    return