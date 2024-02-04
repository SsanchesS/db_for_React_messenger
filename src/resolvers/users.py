import sqlite3
import json
from sql_base.base import base_worker
from sql_base.models import usersM

def get_user(id):
    user = base_worker.insert_data(f"SELECT * FROM users WHERE id = {id}",())
    if user is None:
        return None
    else:
        mas_friends = user[6]
        mas_chats = user[7]
        if user[6]:
            mas_friends = json.loads(user[6])
        if user[7]:
            mas_chats = json.loads(user[7])
        user = {"id":user[0],"f_name":user[1],"s_name":user[2],"password":None,"email":user[4],"avatar":user[5],"mas_friends":mas_friends,"mas_chats":mas_chats}
        return user  

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
    
    if user.avatar is not None and user.avatar != '':           ###############
        update_fields.append(f"avatar = '{user.avatar}'")

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
        user = {"id":user_id[0],"f_name":user.f_name,"s_name":user.s_name,"password":None,"email":user.email,"avatar":user.avatar,"mas_friends":user.mas_friends,"mas_chats":user.mas_chats}
        return user 

def del_user(id):
    del_id = base_worker.insert_data(f"DELETE FROM users WHERE id = {id} RETURNING id;",())
    if del_id is None:
        return None
    else:
        user = {"id":del_id[0],"f_name":None,"s_name":None,"password":None,"email":None,"avatar":None,"mas_friends":None,"mas_chats":None}
        return user 