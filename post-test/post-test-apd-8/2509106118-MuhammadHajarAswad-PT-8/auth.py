import os
from data import data_login
from termcolor import colored

def register():
    regis_username = input("Masukkan username  :")
    regis_password = input("Masukkan password  :")
    new_user = len(data_login) + 1
    data_login[new_user] = {"username": regis_username, "password": regis_password, "tipe": "user"}
    print("Anda berhasil register")

def login():
    from data import status_login
    os.system('cls' if os.name == 'nt' else 'clear')
    print("LOGIN")
    input_username = input("Masukkan username  :")
    input_password = input("Masukkan password  :")

    for value in data_login.values():
        if input_username == value["username"] and input_password == value["password"]:
            print(colored(f" Login berhasil sebagai {value['tipe']}", "green"))
            status_login = True
            return value["tipe"]
        

def logout():
    from data import status_login
    status_login = False
    print(colored("Anda berhasil logout", "green"))
