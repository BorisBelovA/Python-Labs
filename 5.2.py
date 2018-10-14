def makeSurnameArray():
    my_file = open("students.csv", encoding='utf8')
    arr = []
    for line in my_file:
        arr.append(line.split(';'))
    arr = arr[1::1]
    for elem in arr:
        elem[3] = elem[3].replace('\n','')
    return arr


def sortSurname(arr):
    surnamArr = []
    i = 0
    while(i<len(arr)):
        surnamArr.append(arr[i][1])
        i+=1
    return sorted(surnamArr)

print(sortSurname(makeSurnameArray()))