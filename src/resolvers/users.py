from sql_base.base import base_worker
from sql_base.models import usersM

def get_user(id) -> int:
    get_user = base_worker.insert_data(f"SELECT * FROM users WHERE id = {id}",())
    return get_user

def new_user(user: usersM) -> int:

    insert_fields = ["f_name", "s_name", "password","email"]
    insert_values = [user.f_name, user.s_name, user.password,user.email]

    if user.avatar is not None:
        insert_fields.append("avatar")
        insert_values.append(f"'{user.avatar}'")
    else:
        default_avatar = ""
        insert_fields.append("avatar")
        insert_values.append(f"'{default_avatar}'")

    fields_str = ', '.join(insert_fields)
    values_str = ', '.join(insert_values)

    new_id = base_worker.insert_data(f"""
        INSERT INTO users ({fields_str})
        VALUES ({values_str})
        RETURNING id;
    """, ())
    
    return new_id

def upd_user(id, user: usersM) -> int:

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

    if user.mas_friends is not None: # and user.mas_friends != ''
        update_fields.append(f"mas_friends = '{user.mas_friends}'")

    if user.mas_chats is not None: # and user.mas_chats != ''
        update_fields.append(f"mas_chats = '{user.mas_chats}'")

    update_fields_str = ', '.join(update_fields)

    upd_id = base_worker.insert_data(f"""
        UPDATE users
        SET {update_fields_str}
        WHERE id = {id} 
        RETURNING id;
    """, ())

    return upd_id

def del_user(id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM users WHERE id = {id} RETURNING id;",())
    return del_id