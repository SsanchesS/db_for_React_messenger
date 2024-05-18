import sqlite3
import json
from src.base import base_worker
from src.models import usersM

from src.service.service import decode_and_write, get_and_encode

def get_user(id):
    try:
        user = base_worker.insert_data(f"SELECT * FROM users WHERE id = {id}",())
        if user is None:
            return None
        else:
            avatar_file = get_and_encode(user[7])
            if not avatar_file:
                print("Ошибка при создании файла")
                return 500
            mas_photosFiles = user[8]
            mas_music = user[9]
            mas_posts = user[10]
            mas_friends = user[11]
            mas_chats = user[12]
            if mas_photosFiles:
                mas_photosFiles = json.loads(user[8])
            if mas_music:
                mas_music = json.loads(user[9])
            if mas_posts:
                mas_posts = json.loads(user[10])
            if mas_friends:
                mas_friends = json.loads(user[11])
            if mas_chats:
                mas_chats = json.loads(user[12])
            user = {"id":user[0],"f_name":user[1],"s_name":user[2],"city":user[3],"birth":user[4],"password":None,"email":user[6],"avatar_file":avatar_file,"mas_photosFiles":mas_photosFiles,"mas_music":mas_music,"mas_posts":mas_posts,"mas_friends":mas_friends,"mas_chats":mas_chats}
            return user  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def upd_user(id, user: usersM):
    try:
        update_fields = []

        if user.f_name is not None and user.f_name != '':
            update_fields.append(f"f_name = '{user.f_name}'")

        if user.s_name is not None and user.s_name != '':
            update_fields.append(f"s_name = '{user.s_name}'")
        
        if user.city is not None and user.city != '':
            update_fields.append(f"city = '{user.city}'")

        if user.birth is not None and user.birth != '':
            update_fields.append(f"birth = '{user.birth}'") # Проверка? 

        if user.password is not None and user.password != '':
            update_fields.append(f"password = '{user.password}'")

        if user.email is not None and user.email != '':
            update_fields.append(f"email = '{user.email}'")
        
        if user.avatar_file is not None and user.avatar_file != '':           # создаем и добавляем путь
            old_avatar_file_path = base_worker.insert_data(f"SELECT avatar_file FROM users WHERE id = {id}",())

            file_path = decode_and_write(user.avatar_file,old_avatar_file_path[0])
            if not file_path:
                print("Ошибка при создании файла")
                return 500
            update_fields.append(f"avatar_file = '{user.avatar_file}'")
         
        if user.mas_photosFiles is not None and user.mas_photosFiles != '':           #####################################################
            update_fields.append(f"mas_photosFiles = '{user.mas_photosFiles}'")

        if user.mas_music is not None and user.mas_music != '':
            update_fields.append(f"mas_music = '{user.mas_music}'")

        if user.mas_posts is not None and user.mas_posts != '':
            update_fields.append(f"mas_posts = '{user.mas_posts}'")   

        if user.mas_friends is not None and user.mas_friends != '':
            print(user.mas_friends)                                                     #####################################################
            update_fields.append(f"mas_friends = '{user.mas_friends}'")

        if user.mas_chats is not None and user.mas_chats != '':
            update_fields.append(f"mas_chats = '{user.mas_chats}'")

        update_fields_str = ', '.join(update_fields)

        try:
            user_id = base_worker.insert_data(f"""
            UPDATE users
            SET {update_fields_str}
            WHERE id = {id} 
            RETURNING id;
            """, ())
        except sqlite3.IntegrityError as e:
            print(f"Ошибка: {e}")
            return None

        user = {"id":user_id[0],"f_name":None,"s_name":None,"city":None,"birth":None,"password":None,"email":None,"avatar_file":None,"mas_photosFiles":None,"mas_music":None,"mas_posts":None,"mas_friends":None,"mas_chats":None}
        return user  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def del_user(id):
    try:
        user_id = base_worker.insert_data(f"DELETE FROM users WHERE id = {id} RETURNING id;",())
        if user_id is None:
            return None
        else:
            user = {"id":user_id[0],"f_name":None,"s_name":None,"city":None,"birth":None,"password":None,"email":None,"avatar_file":None,"mas_photosFiles":None,"mas_music":None,"mas_posts":None,"mas_friends":None,"mas_chats":None}
            return user  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500