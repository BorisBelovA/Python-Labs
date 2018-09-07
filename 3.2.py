my_string = 'Ф;И;О;Возраст;Категория;' \
            '_Иванов;Иван;Иванович;23 года;Студент 3 курса;' \
            '_Петров;Семен;Игоревич;22 года;Студент 2 курса'


arr = my_string.split('_')[0].split(';')
print(arr[0] + arr[1] + arr[2] + '                     ' + arr[4]+ '       ' + arr[3])
arr = my_string.split('_')[1].split(';')
print(arr[0] + " " + arr[1]+ " " + arr[2] + '     '+ arr[3] + '        ' + arr[4])
arr = my_string.split('_')[2].split(';')
print(arr[0] + " " + arr[1]+ " " + arr[2] + '     '+ arr[3] + '        ' + arr[4])