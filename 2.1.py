my_number = 30

user_num = int(input('Введите число: '))

while(True):
    if(my_number < user_num):
        user_num = int(input('Большое число, давай поменьше: '))
    if(my_number>user_num):
        break
print(user_num)