import os
total = 0

def walk(dir):
    total = 0
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            print(path)
            total+=1
        else:
            total+=walk(path)
    return total
dir =  os.getcwd()


print('Количество файлов',walk(dir))

