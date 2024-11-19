from prettytable import PrettyTable
import hashlib
# Function to compute hash lengths
def get_hash_lengths(text):
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    return len(md5_hash), len(sha256_hash)
# Strings to be used in the table
strings = ["Hi", "Paragraph", "Page"]
# Compute hash lengths for each string
len_1, len_4 = get_hash_lengths(strings[0])
len_2, len_5 = get_hash_lengths(strings[1])
len_3, len_6 = get_hash_lengths(strings[2])
# Specify the column names while initializing the table
myTable = PrettyTable(["Strings", "MD5 Length", "SHA-256 Length"])
# Add rows
myTable.add_row([strings[0], len_1, len_4])
myTable.add_row([strings[1], len_2, len_5])
myTable.add_row([strings[2], len_3, len_6])
# Display the table
print(myTable)



sha1Length=hashlib.md5(str1.encode()).hexdigest()