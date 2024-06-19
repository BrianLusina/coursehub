from typing import Dict
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from sanctumlabs_dbkit.sql import BaseModel

from apps.users.domain.entities.user import User
from common.utils import entity_to_orm_dict


class Users(BaseModel):
    
    id: Mapped[str] = mapped_column(String(length=100), unique=True)
    
    email: Mapped[str] = mapped_column(String(length=100), unique=True)

    password: Mapped[str] = mapped_column(String(length=100))

    name: Mapped[str] = mapped_column(String(length=1000))

    def toDict(self) -> Dict[str, str]:
        return dict(
            id=self.id,
            uuid=self.uuid,
            created_at=self.created_at,
            updated_at=self.updated_at,
            updated_by=self.updated_by,
            deleted_at=self.deleted_at,
            name=self.name,
            email=self.email,
            password=self.password,
        )
    
    @staticmethod
    def from_user(user: User) -> 'Users':
        return Users(
            # **entity_to_orm_dict(user),
            id = user.id.value,
            email = user.email,
            password = user.password,
            name = user.name
        )
