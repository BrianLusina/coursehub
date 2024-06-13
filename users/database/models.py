from typing import Dict
from sanctumlabs_dbkit.sql import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class User(BaseModel):
    email: Mapped[str] = mapped_column(String(length=100), unique=True)

    password: Mapped[str] = mapped_column(String(length=100))

    name: Mapped[str] = mapped_column(String(length=1000))

    def toDict(self) -> Dict[str, str]:
        return dict(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            updated_by=self.updated_by,
            deleted_at=self.deleted_at,
            email=self.email,
            password=self.password,
            name=self.name,
        )
