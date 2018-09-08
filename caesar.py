def encrypt_caesar(plaintext):
    ciphertext = ''
    for char in plaintext:
        if 65 <= ord(char) <= 90:
            if 88 <= ord(char) <= 90:
                ciphertext+=chr(ord(char) - 23)
            else:
                ciphertext += chr(ord(char) +3)
        elif 97 <= ord(char) <= 122:
            if 120 <= ord(char) <= 122:
                ciphertext+=chr(ord(char) - 23)
            else:
                ciphertext += chr(ord(char) +3)
        else:
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext):
    plaintext = ''
    for char in ciphertext:
        if 65 <= ord(char) <= 90:
            if 65 <= ord(char) <= 67:
                plaintext+=chr(ord(char) + 23)
            else:
                plaintext += chr(ord(char) - 3)
        elif 97 <= ord(char) <= 122:
            if 97 <= ord(char) <= 99:
                plaintext += chr(ord(char) + 23)
            else:
                plaintext += chr(ord(char) - 3)
        else:
            plaintext += char
    return plaintext


plaintext = 'python'

print(encrypt_caesar('Python3.2'))
print(decrypt_caesar('Sbwkrq3.2'))
