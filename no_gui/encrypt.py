from cryptography.fernet import Fernet

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

f = Fernet(key)

with open('file', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open ('enc_file', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
