def splitSemicolon(text): # Fungsi mirip .split() namun untuk string dengan pemisah semicolon saja
    separated = []
    word = ''
    
    for char in (text):
        if char == '\n' : # jika "\n" (newline), pengecekan berhenti (agar newline tidak masuk ke array)
            break
        elif char != ';':
            word += char # jika bukan ";", huruf akan digabung satu persatu menjadi sebuah kata
        else: # char == ";"
            separated.append(word) # jika ";", maka kata yang telah terbentuk akan dimasukkan dalam array
            word = '' # kemudian kata akan dikosongkan kembali (semicolon dilewat)
    
    separated.append(word) # Untuk kata setelah semicolon terakhir
    
    return separated

def csvRead(path): # Fungsi membaca file .csv baris per baris
    csvOpen = open(path,'r') # Membuka file .csv
    
    for row in csvOpen: # Membaca setiap baris
        cleanData = splitSemicolon(row) # Memisahkan kalimat dari semicolon
    
    csvOpen.close() # Menutup file
    return cleanData