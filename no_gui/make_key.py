from cryptography.fernet import Fernet
import shutil
from datetime import datetime
import os

now = datetime.now()
CURR_DIR = os.path.dirname(os.path.realpath(__file__))

old_key = r'mykey.key'
newloc_old_key = fr'{CURR_DIR}\old_keys\key_from-{now.strftime("%Y-%m-%d--%H-%M-%S")}.key'
shutil.move(old_key, newloc_old_key)

key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

with open('mykey.key', 'rb') as mykey:
    key1 = mykey.read()
    if key1 == key:
        print("Success! A new key has been saved")
    else:
        print("Failed to make new key")
