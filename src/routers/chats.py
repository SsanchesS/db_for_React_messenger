from fastapi import APIRouter
from sql_base.models import chatsM
import resolvers.chats

chats_router = APIRouter()

@chats_router.get('/{id}')
def get_chat(id: int):
    chat = resolvers.chats.get_chat(id)
    if chat is None:
        return {"code": 404, "message": f"Чат с таким id: {id} не найден","chat":None}
    return {"code": 201, "message": "Успешно",'chat': chat}

@chats_router.post('/')
def new_chat(chat: chatsM):
    chat = resolvers.chats.new_chat(chat)
    if chat is None:
        return {"code": 404, "message": f"Ошибка","chat":None}
    return {"code": 201, "message": "Успешно",'chat': chat}

@chats_router.put('/{id}')
def update_chat(id: int, chat: chatsM):
    chat = resolvers.chats.upd_chat(id, chat)
    if chat is None:
        return {"code": 404, "message": f"Чат с таким id: {id} не найден","chat":None}
    return {"code": 201, "message": "Успешно",'chat': chat}

@chats_router.delete('/{id}')
def delete_chat(id: int):
    chat = resolvers.chats.del_chat(id)
    if chat is None:
        return {"code": 404, "message": f"Чат с таким id: {id} не найден","chat":None}
    return {"code": 201, "message": "Успешно",'chat': chat}