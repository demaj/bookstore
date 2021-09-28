from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None


class BookCreate(BookBase):
    title: str
    author: str


class Book(BookBase):
    id: int
    title: str
    author: str
