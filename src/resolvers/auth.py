import json
from src.models import LoginM 
from src.base import base_worker
from src.service.service import get_and_encode

def check_login_request(user: LoginM):
    try:
        get_user = base_worker.insert_data(f"SELECT * FROM users WHERE email = ? AND password = ?",(user.email,user.password))
        if get_user is None:
            return None
        else:
            avatar_file = get_and_encode(get_user[7])
            if not avatar_file:
                print("Ошибка при создании файла")
                return 500
            mas_photosFiles = get_user[8]
            mas_music = get_user[9]
            mas_posts = get_user[10]
            mas_friends = get_user[11]
            mas_chats = get_user[12]
            if mas_photosFiles:
                mas_photosFiles = json.loads(get_user[8])
            if mas_music:
                mas_music = json.loads(get_user[9])
            if mas_posts:
                mas_posts = json.loads(get_user[10])
            if mas_friends:
                mas_friends = json.loads(get_user[11])
            if mas_chats:
                mas_chats = json.loads(get_user[12])
            user = {"id":get_user[0],"f_name":get_user[1],"s_name":get_user[2],"city":get_user[3],"birth":get_user[4],"password":None,"email":get_user[6],"avatar_file":avatar_file,"mas_photosFiles":mas_photosFiles,"mas_music":mas_music,"mas_posts":mas_posts,"mas_friends":mas_friends,"mas_chats":mas_chats}     
            return user 
    except Exception as e:
        print(f"Ошибка {e}")
        return 500