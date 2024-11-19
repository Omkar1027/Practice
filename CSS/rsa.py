from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Generate RSA keys
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Encrypt and Decrypt
cipher = PKCS1_OAEP.new(key.publickey())
encrypted_message = cipher.encrypt(b"Hello, World!")