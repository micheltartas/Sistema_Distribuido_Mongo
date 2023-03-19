from typing import Any, Type

from pydantic import BaseModel, Extra, root_validator


class OrmModel(BaseModel):
    class Config:
        orm_mode = True


class NonEmptyModel(BaseModel):
    @root_validator(pre=True)
    @classmethod
    def at_least_one_field_is_set(cls: Type[BaseModel], values: dict[str, Any]) -> dict[str, Any]:
        if not values:
            raise ValueError(f"{cls.__name__} cannot be empty (at least one field must be set)")
        return values


class CRUDModel(NonEmptyModel):
    class Config:
        # we generally don't want CRUD input to be empty, mutable, or have unexpected fields
        allow_mutation = False
        extra = Extra.forbid
