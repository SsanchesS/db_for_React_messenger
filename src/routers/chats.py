from fastapi import APIRouter
from src.models import chatsM
from src.resolvers.chats import get_chat,new_chat,upd_chat,del_chat

chats_router = APIRouter()

@chats_router.get('/{id}')
def f_get_chat(id: int):
    chat = get_chat(id)
    if chat is None:
        return {"code": 404, "message": f"Чат с таким id: {id} не найден","chat":None}
    return {"code": 201, "message": "Успешно",'chat': chat}

@chats_router.post('/')
def f_new_chat(chat: chatsM):
    chat = new_chat(chat)
    if chat is None:
        return {"code": 404, "message": f"Ошибка","chat":None}
    return {"code": 201, "message": "Успешно",'chat': chat}

@chats_router.put('/{id}')
def f_update_chat(id: int, chat: chatsM):
    chat = upd_chat(id, chat)
    if chat is None:
        return {"code": 404, "message": f"Чат с таким id: {id} не найден","chat":None}
    return {"code": 201, "message": "Успешно",'chat': chat}

@chats_router.delete('/{id}')
def f_delete_chat(id: int):
    chat = del_chat(id)
    if chat is None:
        return {"code": 404, "message": f"Чат с таким id: {id} не найден","chat":None}
    return {"code": 201, "message": "Успешно",'chat': chat}