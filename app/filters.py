from typing import Optional
from fastapi import Query
from pydantic import BaseModel


class BaseFilter(BaseModel):
    class Config:
        use_enum_values = True


class BookFilter(BaseFilter):
    title: Optional[str] = Query(None, description="Date")
