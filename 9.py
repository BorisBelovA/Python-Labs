dict = {1:['1','Иванов Иван Иванович','23','БО-111111'],
 2:['2','Яшков Илья Петрович','24','БО-222222'],
 3:['3','Сидоров Семен Семенович','25','БО-111111']}

def addMember(dict):
    fio = input('Введите ФИО: ')
    age = input('Введите возраст: ')
    group = input('Введите группу: ')
    n = len(dict)+1
    dict[n] = [fio,age,group]
    return dict

def changeById(id):
    fio = input('Введите ФИО: ')
    age = input('Введите возраст: ')
    group = input('Введите группу: ')
    dict[id] = [fio, age, group]
    return dict

dict = addMember(dict)
print(dict)

id = int(input('Введите номер изменяемого студента: '))

dict = changeById(id)
print(dict)

