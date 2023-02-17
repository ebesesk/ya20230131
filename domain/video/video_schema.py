from datetime import datetime
from pydantic import BaseModel
from typing import Union, Optional
from datetime import date
from typing import List
from ..users.users_schema import User

class Video_dbids(BaseModel):
    dbid: str
    class Config:
        orm_mode = True
    
class Scanreturn(BaseModel):
    OverflowError: list[str] = []
    NotImplementedError: list[str] = []
    FileNotFoundError: list[str] = []
    알수없는에러: list[str] = []
    db_추가: list[str] = []
    converted: list[str] = []
    make_gif: list[str] = []
    make_webp: list[str] = []
    delete_gif: list[str] = []
    delete_webp: list[str] = []
    delete_dbids: list[str] = []
    detect_files: list[str] = []

class Addfiles(BaseModel):
    detect_files: list[str]


class Video_update(BaseModel):
    id: int
    dbid: str
    
    display_quality: str | None = None
    country: str | None = None
    face: str | None = None
    look: str | None = None
    age: str | None = None
    pussy: str | None = None

    etc: str | None = None

    school_uniform: bool | None = None
    hip: bool | None = None
    group: bool | None = None
    pregnant: bool | None = None
    conversation: bool | None = None
    lesbian: bool | None = None
    ani: bool | None = None
    oral: bool | None = None
    masturbation: bool | None = None
    massage: bool | None = None
    uniform: bool | None = None
    family: bool | None = None
    
    ad_start: int | None = None
    ad_finish: int | None = None
    star: int | None = None
    
    date_posted: date | None = None
    date_modified: date | None = None

class Video_create(BaseModel):
    id: int
    dbid: str
    width: int | None = None
    height: int | None = None
    showtime: int | None = None
    bitrate: int | None = None
    filesize: int | None = None
    cdate: date | None = None
    
    display_quality: str | None = None
    country: str | None = None
    face: str | None = None
    look: str | None = None
    age: str | None = None
    pussy: str | None = None

    etc: str | None = None

    school_uniform: bool | None = None
    hip: bool | None = None
    group: bool | None = None
    pregnant: bool | None = None
    conversation: bool | None = None
    lesbian: bool | None = None
    ani: bool | None = None
    oral: bool | None = None
    masturbation: bool | None = None
    massage: bool | None = None
    uniform: bool | None = None
    family: bool | None = None
    
    ad_start: int | None = None
    ad_finish: int | None = None
    star: int | None = None
    
    date_posted: date | None = None
    date_modified: date | None = None



class Video_info(BaseModel):
    id: int
    dbid: str
    width: int | None = None
    height: int | None = None
    showtime: int | None = None
    bitrate: int | None = None
    filesize: int | None = None
    cdate: date | None = None
    
    display_quality: str | None = None
    country: str | None = None
    face: str | None = None
    look: str | None = None
    age: str | None = None
    pussy: str | None = None

    etc: str | None = None

    school_uniform: bool | None = None
    hip: bool | None = None
    group: bool | None = None
    pregnant: bool | None = None
    conversation: bool | None = None
    lesbian: bool | None = None
    ani: bool | None = None
    oral: bool | None = None
    masturbation: bool | None = None
    massage: bool | None = None
    uniform: bool | None = None
    family: bool | None = None
    
    ad_start: int | None = None
    ad_finish: int | None = None
    star: int | None = None
    
    date_posted: date | None = None
    date_modified: date | None = None
    
    voter: list[User] = []
    dislike: list[User] = []
    class Config:
        orm_mode = True

class Video_info_list(BaseModel):
    total: int
    video_list: list[Video_info] = []


class VideoVote(BaseModel):
    video_id: int

class VideoDislike(BaseModel):
    video_id: int

# class VideoItems(BaseModel):
#     Video_list: list[VideoItem] = []