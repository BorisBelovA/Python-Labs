import random
i = 0
list = []
while (i<10):
    list.append(random.randint(0,20))
    i+=1
print(list)
list = list[2::1]
list.append(1)
list.append(2)
print(list)