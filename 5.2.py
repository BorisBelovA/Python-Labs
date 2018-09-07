def sortSurname():
    my_file = open("students.csv",encoding='utf8')
    arr = []
    for line in my_file:
        arr.append(line.split(';'))
    #print(arr)
    arr = arr[1::1]
    #print(arr)
    surnamArr = []
    i = 0
    while(i<len(arr)):
        surnamArr.append(arr[i][1])
        i+=1
    return sorted(surnamArr)
print(sortSurname())