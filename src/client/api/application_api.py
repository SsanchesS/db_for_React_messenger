import requests
from tkinter import *
from datetime import datetime

def create_application_app(root,font):
   application_app = Toplevel(root)
   application_app.title("Работа с Заявкой")  
   application_app.geometry('1400x900')

   global id,dataAt,animal,treatmentType,descriptionDisease,customerData,treatmentStatus
   id=StringVar()
   dataAt=StringVar()
   animal=StringVar()
   treatmentType=StringVar()
   descriptionDisease=StringVar()
   customerData=StringVar()
   treatmentStatus = StringVar()

   dataAt.set(datetime.now().strftime("%Y-%m-%d"))

#

   lbl_get_application = Label(application_app, text="Показать заявку по id", font=font)
   entry_get_application = Entry(application_app, font=font, textvariable=id)
   btn_get_application = Button(application_app, text='Получить', font=font, command=lambda: fun_get_application(entry_get_application.get()))
   lbl_get_application.grid(row=1, column=1)
   entry_get_application.grid(row=2, column=0)
   btn_get_application.grid(row=2, column=1)

#

   lbl_dataAt = Label(application_app, text='Дата в формате Y-m-d', font=font)
   entry_dataAt_data = Entry(application_app, font=font, textvariable=dataAt)

   lbl_animal = Label(application_app, text='животное', font=font)
   entry_animal_data = Entry(application_app, font=font, textvariable=animal)

   lbl_treatmentType = Label(application_app, text='тип лечения', font=font)
   entry_treatmentType_data = Entry(application_app, font=font, textvariable=treatmentType)

   lbl_descriptionDisease = Label(application_app, text='описание заболевания', font=font)
   entry_descriptionDisease_data = Entry(application_app, font=font, textvariable=descriptionDisease)

   lbl_customerData = Label(application_app, text='данные клиента', font=font)
   entry_customerData_data = Entry(application_app, font=font, textvariable=customerData)

   lbl_treatmentStatus = Label(application_app, text='статус лечения', font=font)
   entry_treatmentStatus_data = Entry(application_app, font=font, textvariable=treatmentStatus)
#

   btn_new_application = Button(application_app, text='Создать', font=font, command=lambda: fun_new_application(entry_dataAt_data.get(),entry_animal_data.get(),entry_treatmentType_data.get(),entry_descriptionDisease_data.get(),entry_customerData_data.get(),entry_treatmentStatus_data.get()))

   btn_upd_application = Button(application_app, text='Обновить', font=font, command=lambda: fun_upd_application(entry_get_application.get(),entry_dataAt_data.get(),entry_animal_data.get(),entry_treatmentType_data.get(),entry_descriptionDisease_data.get(),entry_customerData_data.get(),entry_treatmentStatus_data.get()))

   btn_del_application = Button(application_app, text='Удалить по id', font=font, command=lambda: fun_del_application(entry_get_application.get()))

   lbl_dataAt.grid(row=4, column=0)
   entry_dataAt_data.grid(row=4, column=2)

   lbl_animal.grid(row=5, column=0)
   entry_animal_data.grid(row=5, column=2)

   lbl_treatmentType.grid(row=6, column=0)
   entry_treatmentType_data.grid(row=6, column=2)

   lbl_descriptionDisease.grid(row=7, column=0)
   entry_descriptionDisease_data.grid(row=7, column=2)

   lbl_customerData.grid(row=8, column=0)
   entry_customerData_data.grid(row=8, column=2)

   lbl_treatmentStatus.grid(row=9, column=0)
   entry_treatmentStatus_data.grid(row=9, column=2)

   btn_new_application.grid(row=11, column=0)

   btn_upd_application.grid(row=11, column=1)

   btn_del_application.grid(row=11, column=2)

def get_response(s):
   response = s
   try:
      id.set(s[0])
      dataAt.set(s[1])
      animal.set(s[2])
      treatmentType.set(s[3])
      descriptionDisease.set(s[4])
      customerData.set(s[5])
      treatmentStatus.set(s[6])
      print(response)
   except ValueError:
      id.set("ошибка")

#

def fun_get_application(application_id):
   try:
      application_id = int(application_id)
   except ValueError:
     get_response(['id - не число', '', '', '', '', '', ''])
     return

   if isinstance(application_id, int):
      r = requests.get(f'http://127.0.0.1:8000/application/{application_id}')
      answer = r.json()
      print(answer)
      if 'message' in answer:
         get_response(['нет такого id', '', '', '', '', '', ''])
      else:
         get_response(answer['application'])
   else:
      get_response(['Введи число', '', '', '', '', '', ''])

def fun_new_application(dataAt2,animal,treatmentType,descriptionDisease,customerData,treatmentStatus):
   try:
      datetime.strptime(dataAt2, "%Y-%m-%d")
   except ValueError:
      dataAt.set("Не Корректно")
      return
   data = f'{{ "dataAt": "{dataAt2}", "animal": "{animal}", "treatmentType": "{treatmentType}", "descriptionDisease": "{descriptionDisease}", "customerData": "{customerData}", "treatmentStatus": "{treatmentStatus}"}}'
   r = requests.post(f'http://127.0.0.1:8000/application/',data=data)
   answer = r.json()
   print(answer)
   get_response([answer['id'][0], '', '', '', '', '', ''])

def fun_upd_application(application_id,dataAt2,animal,treatmentType,descriptionDisease,customerData,treatmentStatus):
   try:
      datetime.strptime(dataAt2, "%Y-%m-%d")
   except ValueError:
      dataAt.set("Не Корректно")
      return
   try:
      application_id = int(application_id)
   except ValueError:
     get_response(['id - не число', '', '', '', '', '', ''])
     return
   if isinstance(application_id, int):
      data = f'{{ "dataAt": "{dataAt2}", "animal": "{animal}", "treatmentType": "{treatmentType}", "descriptionDisease": "{descriptionDisease}", "customerData": "{customerData}", "treatmentStatus": "{treatmentStatus}"}}'
      r = requests.put(f'http://127.0.0.1:8000/application/{application_id}',data=data)
      answer = r.json()
      print(answer)
      if 'message' in answer:
         get_response(['нет такого id', '', '', '', '', '', ''])
      else:
         get_response([answer['Update application'][0], '', '', '', '', '', ''])
   else:
      get_response(['Введи число', '', '', '', '', '', ''])

def fun_del_application(application_id):
   try:
      application_id = int(application_id)
   except ValueError:
     get_response(['id - не число', '', '', '', '', '', ''])
     return
   if isinstance(application_id, int):
      r = requests.delete(f'http://127.0.0.1:8000/application/{application_id}')
      answer = r.json()
      print(answer)
      if 'message' in answer:
         get_response(['нет такого id', '', '', '', '', '', ''])
      else:
         get_response([answer['Delete application'][0], '', '', '', '', '', ''])
   else:
      get_response(['Введи число', '', '', '', '', '', ''])