def dictionary():
    dict = {'short' : 'dict', 'long' : 'dictionary', 'rus' : 'словарь'}
    count = 0
    for key in dict:
        count+=1
    return count
print(dictionary())