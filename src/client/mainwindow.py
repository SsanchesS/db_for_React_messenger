from tkinter import *
import tkinter.messagebox as mesbox
import requests
from  my_app import create_app

font = ('Arial Bold', 16)

root = Tk()
root.title("My GUI")  
root.geometry('700x400')

login = StringVar()
password = StringVar()

def check_login(login: str, password: str):
    data = {"login": login, "password": password}
    r = requests.post('http://127.0.0.1:8000/login', json=data) # r = requests.post('http://127.0.0.1:8000/login', data=data)
    answer = r.json()
    print(answer)
    code = answer["code"]
    message = answer["message"]
    if code != 200:
        print(f"Server error:{message}")
        return None
    else:
        return {'user_id':answer['user_id'],'role_id':answer["role_id"]}

def open_login():
    user = check_login(login=login.get(),password=password.get())
    if user['user_id']:
        print("Login ok")
        print(f'user: {user}')
        root.withdraw()
        create_app(root,font,user_props=user)
    else:
        mesbox.showerror(title="Wrong login",message="Логин или пароль не верны")

lbl_main = Label(root, text="Вход в систему", font=font)
lbl_login = Label(root, text="login", font=font)
lbl_password = Label(root, text='password', font=font)

entry_login = Entry(root, font=font, textvariable=login)
entry_password = Entry(root, font=font,show="*", textvariable=password)

btn_enter = Button(root, text='Вход', font=font, command=open_login)
btn_close = Button(root, text='Отмена', font=font)

lbl_main.grid(row=0, columnspan=2, column=1)
lbl_login.grid(row=1, column=0, pady=10, ipadx=10)
lbl_password.grid(row=2, column=0, pady=10, ipadx=10)

entry_login.grid(row=1, column=1, columnspan=3, padx=30, pady=10)
entry_password.grid(row=2, column=1, columnspan=3, padx=30, pady=10)

btn_enter.grid(row=3, column=1, pady=10)
btn_close.grid(row=3, column=2, pady=10)

if __name__ == '__main__':
    root.mainloop()