def encryptString(n,key):
    encrypt=''
    for i in range(len(n)):
        char=n[i]
        if char.isupper():
            encrypt += chr((((ord(char))-65) * key ) % 26 + 65)
        else:
            encrypt += chr((((ord(char))-97) * key ) % 26 + 97)
    return encrypt

def decryptString(encrypt,keyI):
    decrypt=''
    for i in range(len(encrypt)):
        char=encrypt[i]
        if char.isupper():
            decrypt += chr((((ord(char))-65) * keyI ) % 26 + 65)
        else:
            decrypt += chr((((ord(char))-97) * keyI ) % 26 + 97)
    return decrypt

def mod_inverse(key):
    for i in range(26):
        if (((key % 26) * (i % 26)) % 26 == 1):
            return i

n=str(input("Enter the string to be encrypted: "))
key=int(input("Enter the key(Roll No): "))
encrypt=str(encryptString(n,key))
print("Plaintext: ",n)
print("Key: ",key)
print("Encrypted text: ",encrypt)
keyI=(mod_inverse(key))
d=str(decryptString(encrypt,keyI))
print("\nDecryptyed text: ",d)


