import datetime
from pydantic import BaseModel, validator, EmailStr
from typing import List, Optional
from ..users.users_schema import User


class Manga_db(BaseModel):
    id: int
    title: str
    tag: str | None = None
    created_date: datetime.datetime | None = None
    voter: List[User] = []
    page: int
    class Config:
        orm_mode = True

class Manga(BaseModel):
    id: int
    title: str
    tag: str | None = None
    created_date: datetime.datetime | None = None
    voter: List[User] = []
    images: List[str] | None = None
    
class MangaList(BaseModel):
    total: int = 0
    manga_list: List[Manga] = []
    
class MangaVote(BaseModel):
    manga_id: int