import math
dict = {chr(i+65):i for i in range(26) }


def makeKey(text,keyword):
    multiplier = len(text) // len(keyword)
    srez = len(text) - len(keyword) * multiplier
    return keyword*multiplier + keyword[0:srez]


def encrypt_vigenere(plaintext, keyword):
    ciphertext = ''
    keyword = makeKey(plaintext, keyword)
    for i in range(len(plaintext)):
        shift = dict[keyword[i]]
        if(65 <= ord(plaintext[i]) <= 90):
            if(shift+ord(plaintext[i]) > 90):
                ciphertext += chr((shift + ord(plaintext[i])) - 26)
            else:
                ciphertext += chr(shift + ord(plaintext[i]))
        elif (97 <= ord(plaintext[i]) <= 122):
            if (shift + ord(plaintext[i]) > 122):
                ciphertext += chr((shift + ord(plaintext[i])) - 26)
            else:
                ciphertext += chr(shift + ord(plaintext[i]))
        else:
            ciphertext += plaintext[i]
        #print(shift + ord(plaintext[i]))
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    plaintext = ''
    keyword = makeKey(ciphertext, keyword)
    for i in range(len(ciphertext)):
        shift = dict[keyword[i]]
        if (65 <= ord(ciphertext[i]) <= 90):
            if((ord(ciphertext[i]) - shift) < 65):
                plaintext += chr((ord(ciphertext[i]) - shift) + 26)
            else:
                plaintext += chr(ord(ciphertext[i]) - shift)
        elif (97 <= ord(ciphertext[i]) <= 122):
            if ((ord(ciphertext[i]) - shift) < 97):
                plaintext += chr((ord(ciphertext[i]) - shift) + 26)
            else:
                plaintext += chr(ord(ciphertext[i]) - shift)
        else:
            plaintext+=ciphertext[i]
    return plaintext

plaintext = 'ATTACKATDAWN'
#plaintext = 'attackatdawn'
key = 'LEMON'
ciphertext = encrypt_vigenere(plaintext, key)
print('Шифр: ', ciphertext)
plaintext = decrypt_vigenere(ciphertext, key)
print('Изначальное: ', plaintext)

