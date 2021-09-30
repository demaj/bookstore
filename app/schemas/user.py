from typing import Optional
from pydantic.main import BaseModel
from pydantic.networks import EmailStr


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False


class UserCreate(UserBase):
    email: EmailStr
    password: str


class User(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str
