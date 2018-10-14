arr = [['1','Иванов Иван Иванович','23','БО-111111'],
 ['2','Яшков Илья Петрович','24','БО-222222'],
 ['3','Сидоров Семен Семенович','25','БО-111111']]

def fromArrToDict(arr):
    dict = {}
    for elem in arr:
        dict[elem[0]] = elem
    return dict

def increaseAgeByFIO(string, dict):
    for elem in dict:
        if(dict[elem][1] == string):
            dict[elem][2] = str(int(dict[elem][2])+1)
    return dict

dict = fromArrToDict(arr)
print(increaseAgeByFIO('Яшков Илья Петрович', dict))
