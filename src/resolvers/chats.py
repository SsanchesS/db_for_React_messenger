import json

from sql_base.base import base_worker
from sql_base.models import chatsM

def get_chat(id):
    chat = base_worker.insert_data(f"SELECT * FROM chats WHERE id = {id}",())
    if chat is None:
        return None
    else:
        mas_users = chat[1]
        mas_messages = chat[2]
        if chat[1]:
            mas_users = json.loads(chat[1])
        if chat[2]:
            mas_messages = json.loads(chat[2])
        chat = {"id":chat[0],"mas_users":mas_users,"mas_messages":mas_messages}
        return chat  

def new_chat(chat: chatsM):
    new_id = base_worker.insert_data(f"""
    INSERT INTO chats (mas_users, mas_messages) 
    VALUES (?, ?) RETURNING id;
    """, (chat.mas_users, chat.mas_messages))
    chat = {"id":new_id[0],"mas_users":chat.mas_users,"mas_messages":chat.mas_messages}
    return chat

def upd_chat(id, chat: chatsM):
    update_fields = []
    if chat.mas_users is not None and chat.mas_users != '':
        update_fields.append(f"mas_users = '{chat.mas_users}'")
    if chat.mas_messages is not None and chat.mas_messages != '':
        update_fields.append(f"mas_messages = '{chat.mas_messages}'")

    update_fields_str = ', '.join(update_fields)

    chat_id = base_worker.insert_data(f"""
        UPDATE chats
        SET {update_fields_str}
        WHERE id = {id} 
        RETURNING id;
    """, ())

    if chat_id is None:
        return None
    else:
        chat = {"id":chat_id[0],"mas_users":chat.mas_users,"mas_messages":chat.mas_messages}
        return chat 

def del_chat(id):
    del_id = base_worker.insert_data(f"DELETE FROM chats WHERE id = {id} RETURNING id;", ())
    if del_id is None:
        return None
    else:
        chat = {"id":del_id[0],"mas_users":None,"mas_messages":None}
        return chat