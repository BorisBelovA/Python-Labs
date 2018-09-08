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
        if(shift+ord(plaintext[i]) > 90):
            ciphertext += chr((shift + ord(plaintext[i])) - 90 + 65 - 1)
        else:
            ciphertext += chr(shift+ord(plaintext[i]))
        print(shift + ord(plaintext[i]))
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    decrypt_vigenere("python", "a")
    'python'
    decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    plaintext = ''
    return plaintext


print(encrypt_vigenere('ATTACKATDAWN', "A"))


