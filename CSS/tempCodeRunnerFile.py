def encrypt_text(plain_text):
    arr1 = []
    arr2 = []
    arrs1 = ''
    arrs2 = ''

    for i, char in enumerate(plain_text):
        if i % 2 == 0:
            arr1.append(char)
            arrs1 = ''.join(arr1)
        else:
            arr2.append(char)
            arrs2 = ''.join(arr2)
    
    encrypt = arrs1 + arrs2
    return encrypt

def decrypt_text(encrypt):
    length = len(encrypt)
    
    if length % 2 == 0:
        mid = length // 2
        first_half = encrypt[:mid]
        second_half = encrypt[mid:]
    else:
        mid = (length // 2) + 1
        first_half = encrypt[:mid]
        second_half = encrypt[mid:] + " "
    
    decrypted_text = ''
    
    for index in range(mid):
        if index == mid - 1 and length % 2 != 0:
            decrypted_text += first_half[index]
        else:
            decrypted_text += first_half[index] + second_half[index]
    
    return decrypted_text

plain_text = input("Enter string: ")
encrypted = encrypt_text(plain_text)
print("Encrypted text is:", encrypted)

decrypted = decrypt_text(encrypted)
print("Decrypted text is:", decrypted)
