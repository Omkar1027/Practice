def encrypt_string(n,key):
    encrypt=''
    for i in range(len(n)):
        char=n[i]
        if char.isupper():
            encrypt += chr(((ord(char)) + key - 65) % 26 + 65)
        else:
            encrypt += chr(((ord(char)) + key - 97) % 26 + 97)
    return encrypt

def decrypt_string(encrypt,key):
    decrypt=''
    for i in range(len(encrypt)):
        char=encrypt[i]
        if char.isupper():
            decrypt += chr(((ord(char)) - key - 65) % 26 + 65)
        else:
            decrypt += chr(((ord(char)) - key - 97) % 26 + 97)
    return decrypt

n=str(input("Enter the string to be encrypted: "))
key=int(input("Enter the key(Roll No): "))
encrypt=str(encrypt_string(n,key))
print("Plaintext: ",n)
print("Key: ",key)
print("Encrypted text: ",encrypt)

decrypt=str(decrypt_string(encrypt,key))
print("\nDecrypted text: ",decrypt)



