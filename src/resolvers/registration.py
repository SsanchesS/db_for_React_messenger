import sqlite3
import base64
import uuid   # Можно с uuid5
import imghdr # для определения типа файла
from src.models import usersM 
from src.base import base_worker

def f_decoded_data(avatar_file):
    try:
        image_type, avatar_file = avatar_file.split(',')  # Можно просто извлечь из image_type

        decoded_data = base64.b64decode(avatar_file)

        file_name = str(uuid.uuid4())[:12]
        image_type = imghdr.what(None, h=decoded_data)
        if not image_type:
            raise ValueError("Невозможно определить расширение файла")
        
        file_path = f"user_files/usersFiles/{file_name}.{image_type}" ################## путь
        with open(file_path, 'wb') as file:        
            file.write(decoded_data)
        return file_path

    except Exception as e:
        print(f"Ошибка {e}")
        return None

def create_user(user:usersM):
    insert_fields = ["f_name", "s_name", "password","email"]
    insert_values = [f"'{user.f_name}'",f"'{user.s_name}'",f"'{user.password}'",f"'{user.email}'"]
    if user.avatar_file is not None:
        file_path = f_decoded_data(user.avatar_file)
        if not file_path:
            print("Ошибка при создании файла")
        insert_fields.append("avatar_file")                   
        insert_values.append(f"'{file_path}'")
    else:
        default_file_path = "user_files/default_avatar_file.png"                ##################
        insert_fields.append("avatar_file")
        insert_values.append(f"'{default_file_path}'") 

    fields_str = ', '.join(insert_fields)
    values_str = ', '.join(insert_values)

    try:
        new_id = base_worker.insert_data(f"""
        INSERT INTO users ({fields_str})
        VALUES ({values_str})
        RETURNING id;
        """, ())
        user = {"id":new_id[0],"f_name":user.f_name,"s_name":user.s_name,"password":None,"email":user.email,"avatar_file":None,"mas_friends":None,"mas_chats":None}
        return user
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
        return None