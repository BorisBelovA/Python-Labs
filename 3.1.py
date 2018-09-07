str = "Hello my name is Boris i'm student"

newStr = ''

str = str.split(' ')

for item in str:
    if(len(item) > 5):
        newStr+=item
print(newStr)