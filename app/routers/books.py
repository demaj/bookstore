from schemas import BookCreate
from starlette.responses import Response
from schemas import Book
from paginations import BookPagination
from typing import Dict
from fastapi.params import Depends
from fastapi.routing import APIRouter
from filters import BookFilter
from sqlalchemy.orm.session import Session
from responses import BookListResponse
from core import dependencies


router = APIRouter(prefix="/books")


@router.get(
    "/",
    response_model=BookListResponse,
    response_model_exclude_none=True
)
def books_list(
    # db: Session = Depends(dependencies.get_db),
    filters: BookFilter = Depends(),
    pagination: BookPagination = Depends()
) -> Dict:
    """ Retrieve a list of books """
    return


@router.post("/", response_model=Book)
def books_create(book_in: BookCreate, response: Response):
    """ Create a new book """
    return


@router.get("/{id}", response_model=Book)
def books_read(
    # db: Session = Depends(dependencies.get_db),
    id: int
):
    """ Read book details """
    return
