from datetime import datetime

from pydantic import BaseModel, EmailStr, conint


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_model = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_model = True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        orm_model = True


class Postout(BaseModel):
    Post: PostResponse
    no_of_votes: int

    class Config:
        orm_model = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str | None = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
