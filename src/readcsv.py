def read_csv(path) :
    field = ''
    row = []
    data =[]
    with open(path) as file :
            for char in file.read():
                if char == ',':
                    row.append(field)
                    field=''
                elif char=="\n" :
                    row.append(field)
                    data.append(row)
                    field=''
                    row=[]
                else :
                    field += char
            row.append(field)
            data.append(row)
    return data