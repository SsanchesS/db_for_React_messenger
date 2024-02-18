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
            user = {"id":user[0],"f_name":user[1],"s_name":user[2],"city":user[3],"birth":user[4],"password":None,"email":None,"avatar_file":avatar_file,"mas_photosFiles":mas_photosFiles,"mas_music":mas_music,"mas_posts":mas_posts,"mas_friends":mas_friends,"mas_chats":mas_chats}
            return user  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def upd_user(id, user: usersM):

    update_fields = []

    if user.f_name is not None and user.f_name != '':
        update_fields.append(f"f_name = '{user.f_name}'")

    if user.s_name is not None and user.s_name != '':
        update_fields.append(f"s_name = '{user.s_name}'")

    if user.password is not None and user.password != '':
        update_fields.append(f"password = '{user.password}'")

    if user.email is not None and user.email != '':             ###############
        update_fields.append(f"email = '{user.email}'")
    
    if user.avatarFile is not None and user.avatarFile != '':           ###############
        update_fields.append(f"avatarFile = '{user.avatarFile}'")

    if user.mas_friends is not None and user.mas_friends != '':
        update_fields.append(f"mas_friends = '{user.mas_friends}'")

    if user.mas_chats is not None and user.mas_chats != '':
        update_fields.append(f"mas_chats = '{user.mas_chats}'")

    update_fields_str = ', '.join(update_fields)

    user_id = base_worker.insert_data(f"""
        UPDATE users
        SET {update_fields_str}
        WHERE id = {id} 
        RETURNING id;
    """, ())

    if user_id is None:
        return None
    else:
        user = {"id":user_id[0],"f_name":user.f_name,"s_name":user.s_name,"password":None,"email":user.email,"avatarFile":user.avatarFile,"mas_friends":user.mas_friends,"mas_chats":user.mas_chats}
        return user 

def del_user(id):
    del_id = base_worker.insert_data(f"DELETE FROM users WHERE id = {id} RETURNING id;",())
    if del_id is None:
        return None
    else:
        user = {"id":del_id[0],"f_name":None,"s_name":None,"password":None,"email":None,"avatarFile":None,"mas_friends":None,"mas_chats":None}
        return user 