from sql_base.base import base_worker
from sql_base.models import chatsM

def get_chat(id) -> int:
    chat = base_worker.insert_data(f"SELECT * FROM chats WHERE id = {id}",())
    return chat

def new_chat(chat: chatsM) -> int:
    new_id = base_worker.insert_data(f"""
        INSERT INTO chats (mas_users, mas_messages) 
        VALUES (?, ?) RETURNING id;
    """, (chat.mas_users, chat.mas_messages))
    return new_id

def upd_chat(id, chat: chatsM) -> int:

    update_fields = []

    if chat.mas_users is not None: # and chat.mas_users != ''
        update_fields.append(f"mas_users = '{chat.mas_users}'")

    if chat.mas_messages is not None: # and chat.mas_messages != ''
        update_fields.append(f"mas_messages = '{chat.mas_messages}'")

    update_fields_str = ', '.join(update_fields)

    upd_id = base_worker.insert_data(f"""
        UPDATE chats
        SET {update_fields_str}
        WHERE id = {id} 
        RETURNING id;
    """, ())

    return upd_id

def del_chat(id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM chats WHERE id = {id} RETURNING id;", ())
    return del_id