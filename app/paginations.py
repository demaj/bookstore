from pydantic import BaseModel


class BasePagination(BaseModel):
    offset: int = 0
    limit: int = 100


class UserPagination(BasePagination):
    limit: int = 10


class BookPagination(BasePagination):
    ...
