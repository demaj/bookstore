from typing import Optional
from pydantic import BaseModel


class BookBase(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None


class BookCreate(BookBase):
    title: str
    author: str


class Book(BookCreate):
    id: int

    class Config:
        orm_mode = True
