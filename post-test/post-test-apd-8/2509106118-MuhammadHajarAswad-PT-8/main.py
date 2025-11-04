import os 
from auth import register, login
from admin import admin_menu
from user import menu_user
from termcolor import colored
import pyfiglet



while True:
    judul = pyfiglet.figlet_format("WELCOME", font="slant")
    print(colored(judul, "yellow"))
    print(colored(
"""
=========================
| 1. REGISTER           |
| 2. LOGIN              |
| 3. OUT                |
=========================

""", "cyan"
    ))
    menu_utama = input(colored("Pilih menu 1-3  :", "green"))
    if menu_utama == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("SILAHKAN REGISTER", "green"))
        register()
    elif menu_utama == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        user_type = login()
        if user_type == "admin":
            admin_menu()
        elif user_type == "user":
            menu_user()
    elif menu_utama == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Anda telah keluar dari program", "green"))
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Pilihan tidak valid, silahkan coba lagi.", "red"))