from starlette.responses import Response
from schemas import Book, BookCreate
from paginations import BookPagination
from typing import Dict
from fastapi.params import Depends
from fastapi.routing import APIRouter
from filters import BookFilter
from sqlalchemy.orm.session import Session
from responses import BookListResponse
from core import deps


router = APIRouter(prefix="/books", tags=["books"])


@router.get(
    "/",
    response_model=BookListResponse,
    response_model_exclude_none=True
)
def books_list(
    db: Session = Depends(deps.get_db),
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
    *,
    db: Session = Depends(deps.get_db),
    id: int
):
    """ Read book details """
    return
