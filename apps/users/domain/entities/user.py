from pydantic import BaseModel, EmailStr
from shared.entities import Entity, UniqueId

class User(BaseModel, Entity):
    id: UniqueId = Entity.next_id()
    name: str
    email: EmailStr
    password: str
