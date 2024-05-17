def read_csv(path) :
    field = ''
    row = []
    data =[]
    with open(path) as file :
            for char in file.read():
                if char == ';':
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

def write_csv(filename, data):
    with open(filename, 'w') as file:
        for row_index, row in enumerate(data):
            for item_index, item in enumerate(row):
                file.write(item)
                if item_index < len(row) - 1:
                    file.write(';')
            if row_index < len(data) - 1:
                file.write('\n')