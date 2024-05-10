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
def write_csv(filename, data):
    with open(filename, 'w') as file:
        for i in range(len(data)):
            file.write(','.join(data[i]))
            if i < len(data) - 1:  # Add newline if it's not the last row
                file.write('\n')

