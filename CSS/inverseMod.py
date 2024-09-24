# def mod_inverse(key1):
#     for i in range(26):
#         if (((key1 % 26) * (i % 26)) % 26 == 1):
#             print(i)
#             return i
#     print("Inverse of",i,"does not exists in modulo 26")
#     return None

# mod_inverse(89)

def mod_inverse(key1):
    for i in range(26):
        if (((key1 % 26) * (i % 26)) % 26 == 1):
            return i
    return None  # Return None if no inverse exists

# Calling the function with key1 = 89
result = mod_inverse(89)
print(result)
