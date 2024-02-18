from src.models import LoginM 
from src.base import base_worker

def check_login_request(user: LoginM):
    try:
        user = base_worker.insert_data(f"SELECT * FROM users WHERE email = ? AND password = ?",(user.email,user.password))
        if user is None:
            return None
        else:
            user = {"id":user[0],"f_name":user[1],"s_name":user[2],"password":None,"email":user[4],"avatarFile":user[5],"mas_friends":None,"mas_chats":None}
            return user 
    except Exception as e:
        print(f"Ошибка {e}")
        return 500