from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# Классный сайт про pydantic
# https://vc.ru/u/1389654-machine-learning/592815-vvedenie-v-pydantic-moshchnaya-proverka-dannyh-dlya-vashih-rest-api-2023

class chatsM(BaseModel):
    mas_users: Optional[str] = None
    mas_messages: Optional[str] = None

class usersM(BaseModel):
    f_name: Optional[str] = None
    s_name: Optional[str] = None
    city: Optional[str] = None
    birth : Optional[str] = None # Optional[datetime] - не робит
                                                                        # data = "01.01.2018"
                                                                        # if datetime.datetime.strptime(date, "%d.%m.%Y):
                                                                        #    print "it's a date"
                                                                        # else:
                                                                        #    print date
    avatar_file: Optional[str] = None # file
    mas_photosFiles: Optional[str] = None
    mas_music: Optional[str] = None

    mas_posts: Optional[str] = None

    password: Optional[str] = None # constr(min_length=8, max_length=32)
    email: Optional[str] = None # EmailStr

    mas_friends: Optional[str] = None
    mas_chats: Optional[str] = None

class musicFiles(BaseModel):
    name: str
    user_id: int
    file: str # file

class usersFiles(BaseModel):
    name: str
    user_id: int
    file: str # file

class usersPosts(BaseModel):
    user_id: int
    content: str
    timestamp : str # date
    file: Optional[str] = None # file

class LoginM(BaseModel):
    password: str # constr(min_length=8, max_length=32)
    email: str # EmailStr