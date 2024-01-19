from sql_base.models import LoginM 
from sql_base.base import base_worker

def check_login_request(user: LoginM):
    user = base_worker.insert_data(f"SELECT * FROM user WHERE email = ? AND password = ?",(user.email,user.password))
    return user