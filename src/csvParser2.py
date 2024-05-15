import sys

def splitSemicolon(text):                                                  
    separated = []
    word = ''
    for char in (text):
        if char == '\n' : 
            break
        elif char != ';':
            word += char                                                   
        else:
            separated.append(word)
            word = ''
    separated.append(word)
    return separated

def csvReadInt(path):                                                         
    csvOpen = open(path,'r')                                               
    cleanData = []
    for row in csvOpen:                                                    
        cleanData.append(splitSemicolon(row))                              
    csvOpen.close()                                                        
    return cleanData

def csvOverwrite(path, row, input):                                        
    csvOpen = open(path,'r')                                               
    tempData = []                                                          
    for i in csvOpen:
        tempData.append(i)                                                 
    tempData[row] = input                                                  

    with open(path,'w') as csvWrite:                                       
        for row in tempData:
            tempData = csvWrite.write(''.join(input))
            csvWrite.write("\n")

def csvWrite(path, input):
    with open(path,'a', newline="") as csvOpen:
        csvOpen.write("\n")
        csvOpen.write(''.join(input))

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