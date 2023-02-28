import datetime

from pydantic import BaseModel, validator

from ..users.users_schema import User

class Worked(BaseModel):
    id: int
    year: int
    month: int
    day: int
    note: str
    create_date: datetime.datetime
    user: User
    class Config:
        orm_mode = True

class WorkedNote(BaseModel):
    note: str
        
class WorkedCreate(BaseModel):
    # date: datetime.date
    year: int
    month: int
    day: int
    note: str
    @validator('year', 'month', 'day')
    def not_empty(cls, v):
        if not v or not str(v).strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class WorkedList(BaseModel):
    worked_list: list[Worked] = []
    
class WorkedUpdate(WorkedCreate):
    worked_id: int|None = None

class WorkedDelete(BaseModel):
    worked_id: int

class WorkedYmd(BaseModel):
    year: int
    month: int
    day: int
    # worked_id: int
    # worked_year: int
    # worked_month: int
    # worked_day: int
    # worked_user_id: int
    
# class WorkedKeys(BaseModel):
#     keywords = [str]