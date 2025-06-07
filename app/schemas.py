from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime
# from pydantic.types import conint
from typing import Literal
# from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    model_config = ConfigDict(from_attributes=True)


class PostOut(BaseModel):
    Post: Post
    votes: int
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int | None = None


# ZeroOrOne = conint(ge=0, le=1) this would allow 0.5 etc
class Vote(BaseModel):
    post_id: int
    dir: Literal[0, 1]
