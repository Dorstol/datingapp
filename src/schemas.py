from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    desc: str


class ItemCreate(ItemBase):
    pass
