from tabulate import tabulate
from cryptography.fernet import Fernet
# import sys

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as kf:
       kf.write(key)

def load_key():
    with open("key.key", "rb") as kf:
        key = kf.read()
    return key

master_pwd = input("What is your master password? ")
key = load_key() + master_pwd.encode()
# print(key)
fer = Fernet(key)

def view():
    with open("passwords.txt", 'r') as f:
        print()
        mat = []
        for line in f.readlines():
            data = line.rstrip()
            user, pswd = data.split('|')
            sub_data = [user, fer.decrypt(pswd.encode())]
            mat.append(sub_data)
            # print(f"User: {user} Password: {pswd}")
        print(tabulate(mat, headers=["User", "Password"]))
        print()
def add():
    name = input("Account: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add): ")

    if mode == 'q':
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!")