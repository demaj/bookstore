import crud
from core import deps
from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
import schemas
import models
from responses import UserListResponse
from paginations import UserPagination
from filters import UserFilter


router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=List[schemas.User])
def users_list(
    db: Session = Depends(deps.get_db),
    offset: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Dict:
    """ Retrieve users. """
    users = crud.user.get_multi(db, offset=offset, limit=limit)
    return users


@router.post("", response_model=schemas.User)
def users_create(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """ Create new user. """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """ Get current user. """
    return current_user
