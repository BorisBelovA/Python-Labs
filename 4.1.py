import random

n = int(input('Размер матрицы: '))
matrix = []
i = 0
summ = 0

while(i<n):
    arr = []
    j = 0
    while(j<n):
        arr.append(random.randint(0,10))
        j+=1
    matrix.append(arr)
    i+=1
print(matrix)

for arr in matrix:
    for item in arr:
        summ+=item
print('Сумма', summ)

