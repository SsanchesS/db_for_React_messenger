import requests
from tkinter import *

def create_user_app(root,font,user_props):
   user_app = Toplevel(root)
   user_app.title("Работа с Пользователями")  
   user_app.geometry('1400x700')


   get_id = StringVar()
   upd_id = StringVar()
   del_id = StringVar()

   new_user_name = StringVar()
   upd_user_name = StringVar()

   new_user_login = StringVar()
   upd_user_login = StringVar()

   new_user_password = StringVar()
   upd_user_password = StringVar()

   new_role_id_id = StringVar()
   upd_role_id_id = StringVar()

#

   lbl_get_user = Label(user_app, text="Показать пользователя по id", font=font)
   entry_get_user = Entry(user_app, font=font, textvariable=get_id)
   btn_get_user = Button(user_app, text='Получить', font=font, command=lambda: fun_get_user(entry_get_user.get()))
   lbl_get_user.grid(row=1, column=1)
   entry_get_user.grid(row=2, column=0)
   btn_get_user.grid(row=2, column=1)

#

   lbl_new_user = Label(user_app, text='Добавить нового пользователя', font=font)

   lbl_new_user_name = Label(user_app, text='Введите имя нового пользователя', font=font)
   entry_new_user_name_data = Entry(user_app, font=font, textvariable=new_user_name)

   lbl_new_user_login = Label(user_app, text='Введите login нового пользователя', font=font)
   entry_new_user_login_data = Entry(user_app, font=font, textvariable=new_user_login)

   lbl_new_user_password = Label(user_app, text='Введите password нового пользователя', font=font)
   entry_new_user_password_data = Entry(user_app, font=font, textvariable=new_user_password)

   lbl_new_role_id_id = Label(user_app, text='Введите id роли нового пользователя: 1 - admin 2 - user', font=font)
   entry_new_role_id_id_data = Entry(user_app, font=font, textvariable=new_role_id_id)

#

   btn_new_user = Button(user_app, text='Создать', font=font, command=lambda: fun_new_user(entry_new_user_name_data.get(),entry_new_user_login_data.get(),entry_new_user_password_data.get(),entry_new_role_id_id_data.get()))
   lbl_new_user.grid(row=3, column=1)

   lbl_new_user_name.grid(row=4, column=0)
   entry_new_user_name_data.grid(row=4, column=2)

   lbl_new_user_login.grid(row=5, column=0)
   entry_new_user_login_data.grid(row=5, column=2)

   lbl_new_user_password.grid(row=6, column=0)
   entry_new_user_password_data.grid(row=6, column=2)

   lbl_new_role_id_id.grid(row=7, column=0)
   entry_new_role_id_id_data.grid(row=7, column=2)

   btn_new_user.grid(row=8, column=1)

#

   lbl_upd_user = Label(user_app, text='Обновить пользователя по id', font=font)

   lbl_upd_user_id = Label(user_app, text='Введите id пользователя', font=font)
   entry_upd_user = Entry(user_app, font=font, textvariable=upd_id)

   lbl_upd_user_name = Label(user_app, text='Введите имя пользователя', font=font)
   entry_upd_user_name_data = Entry(user_app, font=font, textvariable=upd_user_name)

   lbl_upd_user_login = Label(user_app, text='Введите login пользователя', font=font)
   entry_upd_user_login_data = Entry(user_app, font=font, textvariable=upd_user_login)

   lbl_upd_user_password = Label(user_app, text='Введите password пользователя', font=font)
   entry_upd_user_password_data = Entry(user_app, font=font, textvariable=upd_user_password)

   lbl_upd_role_id_id = Label(user_app, text='Введите id роли пользователя: 1 - admin 2 - user', font=font)
   entry_upd_role_id_id_data = Entry(user_app, font=font, textvariable=upd_role_id_id)

#

   btn_upd_user = Button(user_app, text='Обновить', font=font, command=lambda: fun_upd_user(entry_upd_user.get(),entry_upd_user_name_data.get(),entry_upd_user_login_data.get(),entry_upd_user_password_data.get(),entry_upd_role_id_id_data.get()))
   lbl_upd_user.grid(row=9, column=1)

   lbl_upd_user_id.grid(row=10, column=0)
   entry_upd_user.grid(row=10, column=2)

   lbl_upd_user_name.grid(row=11, column=0)
   entry_upd_user_name_data.grid(row=11, column=2)

   lbl_upd_user_login.grid(row=12, column=0)
   entry_upd_user_login_data.grid(row=12, column=2)

   lbl_upd_user_password.grid(row=13, column=0)
   entry_upd_user_password_data.grid(row=13, column=2)

   lbl_upd_role_id_id.grid(row=14, column=0)
   entry_upd_role_id_id_data.grid(row=14, column=2)

   btn_upd_user.grid(row=15, column=1)

#

   lbl_del_user = Label(user_app, text='Удалить пользователя по id', font=font)
   entry_del_user = Entry(user_app, font=font, textvariable=del_id)
   btn_del_user = Button(user_app, text='Удалить', font=font, command=lambda: fun_del_user(entry_del_user.get()))

   lbl_del_user.grid(row=16, column=1)
   entry_del_user.grid(row=17, column=0)
   btn_del_user.grid(row=17, column=1)

   global props
   props = user_props
#
   global lb2_response
   lb1_response = Label(user_app, text='Полученный ответ', font=font)
   lb2_response = Label(user_app, text='', font=font)

   lb1_response.grid(row=18, column=1)
   lb2_response.grid(row=19, column=1)

def get_response(s):
   response = s
   print(response)
   lb2_response.config(text=response)

#

def fun_get_user(user_id):
   r = requests.get(f'http://127.0.0.1:8000/user/{user_id}')
   answer = r.json()
   get_response(answer)

def fun_new_user(name,login,password,role_id):
   data = f'{{ "name": "{name}", "login": "{login}", "password": "{password}", "role_id": "{role_id}"}}'
   if(props['role_id'] == 1):
      r = requests.post(f'http://127.0.0.1:8000/user/',data=data)
      answer = r.json()
      get_response(answer)
   else:
      data = f'{{ "name": "{name}", "login": "{login}", "password": "{password}", "role_id": "{2}"}}'
      r = requests.post(f'http://127.0.0.1:8000/user/',data=data)
      answer = r.json()
      get_response('Добавлен user с role_id user')

def fun_upd_user(user_id,name,login,password,role_id):
   data = f'{{ "name": "{name}", "login": "{login}", "password": "{password}", "role_id": "{role_id}" }}'
   if(props['role_id'] == 1):
      r = requests.put(f'http://127.0.0.1:8000/user/{user_id}',data=data)
      answer = r.json()
      get_response(answer)
   else:
      data = f'{{ "name": "{name}", "login": "{login}", "password": "{password}", "role_id": "{2}"}}'
      r = requests.post(f'http://127.0.0.1:8000/user/',data=data)
      answer = r.json()
      get_response('Обновлен user с role_id user')

def fun_del_user(user_id):
   user_id = int(user_id)
   if (user_id==props['user_id']):
      get_response('Вы не можете удалить себя')
   else:
      if(props['role_id'] == 1):
         r = requests.delete(f'http://127.0.0.1:8000/user/{user_id}')
         answer = r.json()
         get_response(answer)
      else:
         get_response('Не достаточно прав')
   