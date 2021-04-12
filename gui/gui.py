from tkinter import *
from cryptography.fernet import Fernet
from tkinter import filedialog
import os
text = "File encrypter and decrypter in python"
key = bytes()


def encrypt():
    global key
    folder_name = os.path.dirname(os.path.realpath(__file__))
    filename = filedialog.askopenfilename(initialdir=folder_name, title="Open A File")
    new_filename = filedialog.asksaveasfilename(initialdir="/", title="Save File")
    f = Fernet(key)

    with open(filename, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)

    with open(new_filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        label_file_explorer.configure(text="File Encrypted")


def decrypt():
    global key
    folder_name = os.path.dirname(os.path.realpath(__file__))
    filename = filedialog.askopenfilename(initialdir=folder_name, title="Open A File")
    new_filename = filedialog.asksaveasfilename(initialdir="/", title="Save File")
    f = Fernet(key)

    with open(filename, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    try:
        decrypted = f.decrypt(encrypted)
        with open(new_filename, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
            label_file_explorer.configure(text="File Decrypted")
    except:
        label_file_explorer.configure(text="An Error has occurred")


def open_key():
    global key
    folder_name = os.path.dirname(os.path.realpath(__file__))
    filename = filedialog.askopenfilename(initialdir=folder_name, title="Open A Key")
    with open(filename, 'rb') as mykey:
        key = mykey.read()
    label_file_explorer.configure(text="Key File Opened")
    button_encrypt.grid(column=1, row=2)
    button_decrypt.grid(column=1, row=3)


def make_key():
    global key
    folder_name = os.path.dirname(os.path.realpath(__file__))
    key = Fernet.generate_key()
    new_filename = filedialog.asksaveasfilename(initialdir=folder_name, title="Save Key")
    with open(new_filename, 'wb') as mykey:
        mykey.write(key)
    button_encrypt.grid(column=1, row=2)
    button_decrypt.grid(column=1, row=3)


# Seting up the tkinter window
window = Tk()
window.title('File encrypter and decrypter')
window.geometry("707x150")
window.config(background="white")
label_file_explorer = Label(window, text=text, width=100, height=4, fg="blue")

button_encrypt = Button(window, text="Encrypt", command=encrypt)
button_decrypt = Button(window, text="Decrypt", command=decrypt)
button_keyopen = Button(window, text="Find Key", command=open_key)
button_makekey = Button(window, text="Make Key", command=make_key)

label_file_explorer.grid(column=1, row=1)
button_keyopen.grid(column=1, row=4)
button_makekey.grid(column=1, row=5)
window.mainloop()
