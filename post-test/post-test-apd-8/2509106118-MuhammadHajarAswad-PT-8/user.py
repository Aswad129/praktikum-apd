import os
from crud import tampilkan_film
from auth import logout
from termcolor import colored

def menu_user():
    while True:
        print(colored("""
=========================================
| 1. LIHAT FILM & TAHUN RILIS           |
| 2. LOGOUT                             |
=========================================
""", "cyan"))
        pilihan = input(colored("Pilih menu 1-2 : ", "green"))
        os.system('cls' if os.name == 'nt' else 'clear')

        if pilihan == "1":
            tampilkan_film()
        elif pilihan == "2":
            logout()
            break
        else:
            print(colored("Pilihan hanya 1-2!", "red"))
