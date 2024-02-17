from fastapi import APIRouter
from src.models import usersM
from src.resolvers.users import get_user,upd_user,del_user 

users_router = APIRouter()

@users_router.get('/{id}')
def f_get_user(id: int):
    user = get_user(id)
    if user is None:
        return {"code": 404, "message": f"Пользователь с таким id: {id} не найден","user":None}
    return {"code": 201, "message": "Успешно",'user': user}

@users_router.put('/{id}')
def f_update_user(id: int, user: usersM):
    user = upd_user(id, user)
    if user is None:
        return {"code": 404, "message": f"Пользователь с таким id: {id} не найден","user":None}
    return {"code": 201, "message": "Успешно",'user': user}

@users_router.delete('/{id}')
def f_delete_user(id: int):
    user = del_user(id)
    if user is None:
        return {"code": 404, "message": f"Пользователь с таким id: {id} не найден","user":None}
    return {"code": 201, "message": "Успешно",'user': user}