from fastapi import APIRouter
from sql_base.models import LoginM
from resolvers.auth import check_login_request

auth_router = APIRouter()

@auth_router.post('/')
def auth(user:LoginM):
    user = check_login_request(user)
    if user is None:
        return {"code": 401, "message": "email или password не верны, попробуй снова","user":None}
    else:
        return {"code": 200, "message": "Ты вошёл",'user': user}