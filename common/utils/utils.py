from typing import Any
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


def entity_to_orm_dict(model: BaseModel) -> Any:
    """Converts an entity to an ORM dictionary that can be used to persist to a database.

    Args:
        model (BaseModel): Pydantic Model

    Returns:
        Any: Json encoded data
    """
    return jsonable_encoder(model)
