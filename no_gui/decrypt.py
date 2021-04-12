from cryptography.fernet import Fernet
decrypted = bytes()

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

f = Fernet(key)

with open('enc_file', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()
try:
    decrypted = f.decrypt(encrypted)
    with open('dec_file', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
except:
    with open('ERROR.txt', 'w') as error_file:
        error_file.write('An error has occurred\nThe original key used to encrypt this file does not match the current '
                         'key being used to decrypt this file.\nIn order to decrypt this file, please use the original '
                         'key.\nIf you do not have the original key, then this file can never be decrypted.')
