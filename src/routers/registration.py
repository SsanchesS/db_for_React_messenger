from fastapi import APIRouter
from src.models import usersM
from src.resolvers.registration import create_user

registration_router = APIRouter()

@registration_router.post('/')
def f_registration(user:usersM):
    user = create_user(user)
    if user == 500:
        return {"code": 500, "message": "Ошибка сервера","user":None}
    if user is None:
        return {"code": 401, "message": "Этот email уже занят","user":None}
    return {"code": 201, "message": "Ты зареган",'user': user}