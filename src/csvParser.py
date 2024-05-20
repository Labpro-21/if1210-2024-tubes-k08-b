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



def splitSemicolonInt(text):                                                  
    separated = []
    word = ''
    for char in (text):
        if char == '\n' : 
            break
        elif char != ';':
            word += char                                                   
        else:
            if word.isdigit():
                word = int(word)
            separated.append(word)
            word = ''
    if word.isdigit():
        word = int(word)
    separated.append(word)
    return separated

def csvReadInt(path):                                                         
    csvOpen = open(path,'r')                                               
    cleanData = []
    for row in csvOpen:                                                    
        cleanData.append(splitSemicolonInt(row))                              
    csvOpen.close()                                                        
    return cleanData

def csvWriteAll(path,newList):                                             # Fungsi mengupdate csv lama dengan data-data list terbaru
    with open(path,'w') as csvWrite:                              
        for rows in newList:
            csvWrite.write(''.join(rows))
    return