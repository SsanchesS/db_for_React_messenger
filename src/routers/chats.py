from fastapi import APIRouter
from sql_base.models import chatsM
import resolvers.chats

chats_router = APIRouter()

@chats_router.get('/{id}')
def get_chat(id: int):
    chat = resolvers.chats.get_chat(id)
    if chat is None:
        return {"code": 404, 'message': f"Чат с таким id: {id} не найден"}
    return {"code": 201, "chat": chat}

@chats_router.post('/')
def new_chat(chat: chatsM):
    new_id = resolvers.chats.new_chat(chat)
    return {"code": 201, "id": new_id}

@chats_router.put('/{id}')
def update_chat(id: int, chat: chatsM):
    upd_id = resolvers.chats.upd_chat(id, chat)
    if upd_id is None:
        return {"code": 404, 'message': f"Чат с таким id: {id} не найден"}
    return {"code": 201, "id": upd_id}

@chats_router.delete('/{id}')
def delete_chat(id: int):
    del_id = resolvers.chats.del_chat(id)
    if del_id is None:
        return {"code": 404, 'message': f"Чат с таким id: {id} не найден"}
    return {"code": 201, "id": del_id}