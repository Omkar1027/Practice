def encrypt_string(n,key1,key2):
    encrypt=''
    for i in range(len(n)):
        char=n[i]
        if char.isupper():
            encrypt += chr(((((ord(char))-65) + key2) * key1 ) % 26 + 65)
        else:
            encrypt += chr(((((ord(char))-97) + key2) * key1 ) % 26 + 97)
    return encrypt

def mod_inverse(key1):
    for i in range(26):
        if (((key1 % 26) * (i % 26)) % 26 == 1):
            print(i)
            return i
    print("Inverse of",i,"does not exists in modulo 26")
    return None

def decrypt_string(encrypt,keyInverse,key2):
    decrypt=''
    for i in range(len(encrypt)):
        char=encrypt[i]
        if char.isupper():
            decrypt += chr(((((ord(char))-65) - key2) * keyInverse ) % 26 + 65)
        else:
            decrypt += chr(((((ord(char))-97) - key2) * keyInverse ) % 26 + 97)
    return decrypt

n=str(input("Enter the string to be encrypted: "))
key1=int(input("Enter the first key(Multiplicative): "))
key2=int(input("Enter the second key(Additive): "))
encrypt=str(encrypt_string(n,key1,key2))
print("Plaintext: ",n)
print("Key 1: ",key1)
print("Key 2: ",key2)
print("Encrypted text: ",encrypt)

keyInverse=mod_inverse(key1)
decrypt=str(decrypt_string(encrypt,keyInverse,key2))
print("\nDecrypted text: ",decrypt)

