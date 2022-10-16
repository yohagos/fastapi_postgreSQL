from pydantic import BaseModel
from typing import List

class User(BaseModel):
    lastname: str
    firstname: str
    email: str
    password: str

class UserBase(User):
    id: int

class ShowUser(User):
    lastname: str
    firstname: str
    email: str
    
    class Config():
        orm_mode = True