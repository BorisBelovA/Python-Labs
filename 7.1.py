def makeSurnameDict():
    my_file = open("students.csv", encoding='utf8')
    i = 0
    dict = {}
    while True:
        line = my_file.readline()
        if(len(line) != 0):
            #print(line.split(';'))
            dict[i] = line.split(';')
            i+=1
        else:
            break
    dict.pop(0)
    for i in range(1,len(dict)):
        dict[i][3] = dict[i][3].replace('\n','')
    #print(dict)
    return dict

def SortBySurname(i):
        return i[1]

def sortSurname(dict):
    n = 1
    dict = dict
    surnamArr = []
    for i in range(1,len(dict)+1):
        surnamArr.append(dict[i])
    return sorted(surnamArr,key=lambda i: i[n])


dict = makeSurnameDict()
print(sortSurname(dict))