from pydantic import BaseModel, EmailStr
from shared.entities import Entity

class User(BaseModel, Entity):
    id = Entity.next_id()
    name: str
    email: EmailStr
    password: str
