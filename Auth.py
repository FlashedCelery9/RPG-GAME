import profile
import tkinter as tk
from tkinter import messagebox
import json
import sys

import main

try:
    with open('DataBase/Logins.json', 'r', encoding='utf-8') as read:
        base = json.load(read)
except FileNotFoundError:
    base = {}


auth = tk.Tk()
auth.protocol("WM_DELETE_WINDOW", sys.exit)

login = ''
password = tk.StringVar()
Login = tk.StringVar()

auth.title('RPG-GAME')
auth.geometry("200x300")
tk.Label(text='Авторизація', font=10, pady=10).pack()

tk.Label(text='Будь ласка введіть свій логін:', justify="left").pack()

logi = tk.Entry(auth, textvariable=Login, width=30, justify="left")
logi.pack(pady=10)
tk.Label(text='Введіть пароль:', justify="left").pack()
passw = tk.Entry(auth, textvariable=password, width=30, justify="left")
passw.pack(pady=10)
def login_():
    global base, login
    pww = passw.get()
    login = logi.get()
    if login not in base:
        messagebox.showerror("Помилка", "Такого користувача не зареєстровано!")
    elif login in base and base[login] != pww:
        messagebox.showerror("Помилка", "Неправильний пароль")
    elif login in base and base[login] == pww:
        auth.destroy()
tk.Button(auth, text='Авторизуватися', command=login_).pack()



label = tk.Label(auth, text='Не маєш облікового запису?', fg='blue', cursor='hand2', font=("Arial", 7, "underline"))
label.pack(pady=20)
label.bind("<Button-1>", lambda e: registration())

reg_password1 = ''
reg_password2 = ''
reg_login = ''
def registration():
    global reg_password1, reg_password2, reg_login
    register = tk.Toplevel()
    register.attributes("-topmost", True)

    #Обявлення полів:
    new_password = tk.StringVar()
    new_Login = tk.StringVar()
    new_password2 = tk.StringVar()

    register.title('Реєстрація')
    tk.Label(register, text='Реєстрація', font=15).pack()
    tk.Label(register, text='Вигадайте свій логін').pack()
    reg_logi = tk.Entry(register, textvariable=new_Login, width=30, justify="left")
    reg_logi.pack(pady=10)
    tk.Label(register, text='Вигадайте свій пароль', justify="left").pack()
    reg_pasw1 = tk.Entry(register, textvariable=new_password, width=30, justify="left")
    reg_pasw1.pack(pady=10)
    tk.Label(register, text='Повторіть ваш пароль', justify="left").pack()
    reg_pasw2 = tk.Entry(register, textvariable=new_password2, width=30, justify="left")
    reg_pasw2.pack(pady=10)

    def validation():
        global base
        pw1 = new_password.get()
        pw2 = new_password2.get()
        login = new_Login.get()
        if pw1 != pw2:
            messagebox.showerror("Помилка", "Неправильно повторений пароль!")
        elif not login or not pw1 or not pw2:
            messagebox.showerror("Помилка", "Усі поля повинні бути заповнені!")
        elif login in base:
            messagebox.showerror("Помилка", "Користувач з таким іменем вже існує")
            return
        else:
            messagebox.showinfo("Успіх", f"Користувач {login} зареєстрований!")
            base[login] = pw1
            with open('DataBase/Logins.json', 'w', encoding='utf-8') as file:
                json.dump(base, file, indent=4, ensure_ascii=False)
            register.destroy()




    tk.Button(register, text="Зареєструватись", command=validation).pack()







auth.mainloop()