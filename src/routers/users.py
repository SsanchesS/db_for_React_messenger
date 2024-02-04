from fastapi import APIRouter
from sql_base.models import usersM
import resolvers.users

users_router = APIRouter()

@users_router.get('/{id}')
def get_user(id: int):
    user = resolvers.users.get_user(id)
    if user is None:
        return {"code": 404, "message": f"Пользователь с таким id: {id} не найден","user":None}
    return {"code": 201, "message": "Успешно",'user': user}

@users_router.put('/{id}')
def update_user(id: int, user: usersM):
    user = resolvers.users.upd_user(id, user)
    if user is None:
        return {"code": 404, "message": f"Пользователь с таким id: {id} не найден","user":None}
    return {"code": 201, "message": "Успешно",'user': user}

@users_router.delete('/{id}')
def delete_user(id: int):
    user = resolvers.users.del_user(id)
    if user is None:
        return {"code": 404, "message": f"Пользователь с таким id: {id} не найден","user":None}
    return {"code": 201, "message": "Успешно",'user': user}