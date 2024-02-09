import sqlite3
from sql_base.models import usersM 
from sql_base.base import base_worker

def create_user(user:usersM):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",user)
    insert_fields = ["f_name", "s_name", "password","email"]
    insert_values = [f"'{user.f_name}'",f"'{user.s_name}'",f"'{user.password}'",f"'{user.email}'"]
    if user.avatar_file is not None:
        avatar_file_for_response = user.avatar_file
        insert_fields.append("avatar_file")
        insert_values.append(f"'{user.avatar_file}'")
    else:
        default_avatar_file = "default_avatar_file"                ##################
        avatar_file_for_response = default_avatar_file
        insert_fields.append("avatar_file")
        insert_values.append(f"'{default_avatar_file}'") 

    fields_str = ', '.join(insert_fields)
    values_str = ', '.join(insert_values)

    try:
        new_id = base_worker.insert_data(f"""
        INSERT INTO users ({fields_str})
        VALUES ({values_str})
        RETURNING id;
        """, ())
        user = {"id":new_id[0],"f_name":user.f_name,"s_name":user.s_name,"password":None,"email":user.email,"avatar_file":avatar_file_for_response,"mas_friends":None,"mas_chats":None}
        return user
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
        return None