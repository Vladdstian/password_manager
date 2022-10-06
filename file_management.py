import os
import csv
from cryptography.fernet import Fernet

ACCOUNTS = "Password.csv"


def create_file():
    with open(ACCOUNTS, "a", newline='') as file:
        if os.path.getsize(ACCOUNTS) == 0:
            writer = csv.writer(file)
            column_names = ["website", "username", "password"]
            writer.writerow(column_names)


def generate_local_key():
    if not os.path.isfile('filekey.key'):
        with open('filekey.key', 'wb') as filekey:
            key = Fernet.generate_key()
            filekey.write(key)
            return key
    else:
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
            return key


def encrypt_file(key):
    fernet = Fernet(key)
    with open(ACCOUNTS, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(ACCOUNTS, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt_file(key):
    fernet = Fernet(key)
    with open(ACCOUNTS, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(ACCOUNTS, 'wb') as dec_file:
        dec_file.write(decrypted)
