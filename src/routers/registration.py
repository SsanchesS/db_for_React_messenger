from fastapi import APIRouter
from sql_base.models import usersM
from resolvers.registration import create_user

registration_router = APIRouter()

@registration_router.post('/')
def registration(user:usersM):
    user = create_user(user)
    if user is None:
        return {"code": 401, "message": "Этот email уже занят","user":None}
    else:
        return {"code": 201, "message": "Ты зареган",'user': user}