from fastapi import APIRouter
from sql_base.models import usersM
import resolvers.users

users_router = APIRouter()

@users_router.get('/{id}')
def get_user(id: int):
    user = resolvers.users.get_user(id)
    if user is None:
        return {"code": 404, 'message': f"Пользователь с таким id: {id} не найден"}
    return {"code": 201, 'user': user}

@users_router.post('/')
def new_user(user: usersM):
    new_id = resolvers.users.new_user(user)
    if new_id is None or new_id =="Этот email уже занят":
        return {"code": 404, 'message': f"Этот email уже занят"}
    return {"code": 201, "id": new_id}

@users_router.put('/{id}')
def update_user(id: int, user: usersM):
    upd_id = resolvers.users.upd_user(id, user)
    if upd_id is None:
        return {"code": 404, 'message': f"Пользователь с таким id: {id} не найден"}
    return {"code": 201, "id": upd_id}

@users_router.delete('/{id}')
def delete_user(id: int):
    del_id = resolvers.users.del_user(id)
    if del_id is None:
        return {"code": 404, 'message': f"Пользователь с таким id: {id} не найден"}
    return {"code": 201, "id": del_id}