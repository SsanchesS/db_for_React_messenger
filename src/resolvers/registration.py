import sqlite3
from src.models import usersM 
from src.base import base_worker
from src.service.service import decode_and_write

def create_user(user:usersM):
    try:
        insert_fields = ["f_name", "s_name", "password","email"]
        insert_values = [f"'{user.f_name}'",f"'{user.s_name}'",f"'{user.password}'",f"'{user.email}'"]
        if user.avatar_file is not None:
            file_path = decode_and_write(user.avatar_file)
            if not file_path:
                print("Ошибка при создании файла")
                return 500
            insert_fields.append("avatar_file")                   
            insert_values.append(f"'{file_path}'")
        else:
            file_path = "user_files/default_avatar_file.png"   # default_file_path              ##################
            insert_fields.append("avatar_file")
            insert_values.append(f"'{file_path}'") 

        fields_str = ', '.join(insert_fields)
        values_str = ', '.join(insert_values)
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

    try:
        new_id = base_worker.insert_data(f"""
        INSERT INTO users ({fields_str})
        VALUES ({values_str})
        RETURNING id;
        """, ())
        user = {"id":new_id[0],"f_name":user.f_name,"s_name":user.s_name,"password":None,"email":user.email,"avatar_file":file_path,"mas_friends":None,"mas_chats":None}
        return user
    except sqlite3.IntegrityError as e:
        print(f"Ошибка: {e}")
        return None