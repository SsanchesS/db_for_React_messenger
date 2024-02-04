import sqlite3
from sql_base.models import usersM 
from sql_base.base import base_worker

def create_user(user: usersM):
    insert_fields = ["f_name", "s_name", "password","email"]
    insert_values = [f"'{user.f_name}'",f"'{user.s_name}'",f"'{user.password}'",f"'{user.email}'"]
    if user.avatar is not None:
        avatar_for_response = user.avatar
        insert_fields.append("avatar")
        insert_values.append(f"'{user.avatar}'")
    else:
        default_avatar = "default_avatar"
        avatar_for_response = default_avatar
        insert_fields.append("avatar")
        insert_values.append(f"'{default_avatar}'") 

    fields_str = ', '.join(insert_fields)
    values_str = ', '.join(insert_values)

    try:
        new_id = base_worker.insert_data(f"""
        INSERT INTO users ({fields_str})
        VALUES ({values_str})
        RETURNING id;
        """, ())
        user = {"id":new_id[0],"f_name":user.f_name,"s_name":user.s_name,"password":None,"email":user.email,"avatar":avatar_for_response,"mas_friends":None,"mas_chats":None}
        return user
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
        return None