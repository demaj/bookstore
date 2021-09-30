from typing import Optional, Dict, List
from pydantic import BaseModel
from schemas import User, Book


class ListResponse(BaseModel):
    filters: Optional[Dict]
    paging: Optional[Dict]


class UserListResponse(ListResponse):
    results: List[User]


class BookListResponse(ListResponse):
    results: List[Book]
