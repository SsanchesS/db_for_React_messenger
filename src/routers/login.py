from fastapi import APIRouter
from sql_base.models import LoginM
from resolvers.check_login import check_login_request

login_router = APIRouter()

@login_router.post('/')
def check_login_response(user:LoginM):
    user = check_login_request(user)
    if user is None:
        return {"code": 401, "message": "email или password не верны, попробуй снова","user":None}
    else:
        return {"code": 200, "message": "Ты зареган",'user': user}