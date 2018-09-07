import math as m
def calc():
    a = int(input('Введите а: '))
    b = int(input('Введите b: '))
    c = int(input('Введите c: '))
    k = int(input('Введите k: '))

    exp = m.fabs((a**2/b**2 + c**2*a**2)/(a+b+c*(k-a/(b**3))) + c + (k/b - k/a))
    return exp


command = int(input('Введите команду:'
                    '1 : def calc() '))
if(command == 1):
    print('Результат',calc())