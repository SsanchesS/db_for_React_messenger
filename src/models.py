from typing import Optional,Union
from pydantic import BaseModel,constr,EmailStr
from datetime import date

# сайт про pydantic
# https://vc.ru/u/1389654-machine-learning/592815-vvedenie-v-pydantic-moshchnaya-proverka-dannyh-dlya-vashih-rest-api-2023

# Можно использовать функцию uuid4() из модуля uuid но он менее рандомный, как говорят в инете

class chatsM(BaseModel):
    mas_users: Optional[str] = None
    mas_messages: Optional[str] = None

class usersM(BaseModel):
    f_name: Optional[str] = None
    s_name: Optional[str] = None
    city: Optional[str] = None
    birth : Optional[date] = None
                                                                        # data = "01.01.2018"
                                                                        # if datetime.datetime.strptime(date, "%d.%m.%Y):
                                                                        #    print "it's a date"
                                                                        # else:
                                                                        #    print date
    avatar_file: Optional[ Union[str, None] ] = None # file base64 str
    mas_photosFiles: Optional[str] = None
    mas_music: Optional[str] = None

    mas_posts: Optional[str] = None

    password: Optional[constr(min_length=8, max_length=32)] = None
    email: Optional[EmailStr] = None

    mas_friends: Optional[str] = None
    mas_chats: Optional[str] = None

class musicFiles(BaseModel):
    name: str
    user_id: int
    file: object # file

class usersFiles(BaseModel):
    name: str
    user_id: int
    file: object # file

class usersPosts(BaseModel):
    user_id: int
    content: str
    timestamp : date
    file: Optional[ Union[str, None] ] = None # file object   bytes

class LoginM(BaseModel):
    password: constr(min_length=8, max_length=32)
    email: EmailStr