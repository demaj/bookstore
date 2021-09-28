from typing import Optional, Dict, List
from pydantic import BaseModel
from schemas import Book


class ListResponse(BaseModel):
    filters: Optional[Dict]
    paging: Optional[Dict]


class BookListResponse(ListResponse):
    results: List[Book]
