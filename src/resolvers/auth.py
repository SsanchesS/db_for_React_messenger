import json
from src.models import LoginM 
from src.base import base_worker

def check_login_request(user: LoginM):
    user = base_worker.insert_data(f"SELECT * FROM users WHERE email = ? AND password = ?",(user.email,user.password))
    if user is None:
        return None
    else:
        mas_friends = None
        mas_chats = None
        if user[6]:
            mas_friends = json.loads(user[6])
        if user[7]:
            mas_chats = json.loads(user[7])
        user = {"id":user[0],"f_name":user[1],"s_name":user[2],"password":None,"email":user[4],"avatarFile":user[5],"mas_friends":mas_friends,"mas_chats":mas_chats}
        return user 