from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
import models
import crud
from datetime import timedelta
from typing import Any
from fastapi import APIRouter, HTTPException
import schemas
from sqlalchemy.orm import Session
from core import security
from core.config import settings
from core import deps


router = APIRouter(tags=["login"])


@router.post("/login", response_model=schemas.Token)
def login(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """ Get access token for future requests """
    user = crud.user.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.get("/run")
def test_token(
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Test access token
    """
    return "Hello World"


@router.get("/me", response_model=schemas.User)
def get_current_user(
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """ Get current user. """
    return current_user