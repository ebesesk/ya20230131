import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import schema, crud
from ..login.login_router import get_current_user

from database import get_db
from models import User 


router = APIRouter()

@router.get("/keywords")#, response_model=schema.WorkedKeys)
def worked_keyword(db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    today = datetime.datetime.today()
    year = today.year
    month = today.month
    if month == 12:
        last_month = 1
        last_year = year - 1
    else:
        last_month = month - 1
        last_year = year
    worked_list_this = crud.get_worked_list(db=db, user=current_user, year=year, month=month)
    worked_list_last = crud.get_worked_list(db=db, user=current_user, year=last_year, month=last_month)
    # print(worked_list_this)
    # print(worked_list_last)
    keywords = []
    for worked in worked_list_this:
        keywords.append(worked.note)
    for worked in worked_list_last:
        keywords.append(worked.note)
    keywords = list(set(keywords))
    # print(keywords)
    # return keywords
    return {'keywords': keywords}

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_worked_create: schema.WorkedCreate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    crud.create_worked(db=db, worked_create=_worked_create, user=current_user)


    
@router.get("/list", response_model=schema.WorkedList)
def question_list(db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user),
                  year: int = int(datetime.date.today().strftime('%Y')),
                  month: int = int(datetime.date.today().strftime('%m'))):
    worked_list = crud.get_worked_list(db=db, user=current_user, year=year, month=month)
    return {
        'worked_list': worked_list
    }

@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def worked_update(_worked_update: schema.WorkedUpdate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_worked = crud.get_worked_ymd(db=db, 
                                    year=_worked_update.year, 
                                    month=_worked_update.month, 
                                    day=_worked_update.day,
                                    user=current_user)
    if not db_worked:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_worked.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    crud.update_worked(db=db, 
                       db_worked=db_worked,
                       worked_update=_worked_update)
    
@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def worked_delete(_worked_delete: schema.WorkedDelete,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    db_worked = crud.get_worked(db, worked_id=_worked_delete.worked_id)
    if not db_worked:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_worked.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    crud.delete_worked(db=db, db_worked=db_worked)

@router.delete("/delete_ymd", status_code=status.HTTP_204_NO_CONTENT)
def worked_delete_ymd(_worked_delete: schema.WorkedYmd,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    db_worked = crud.get_worked_ymd(db=db, 
                                    year=_worked_delete.year, 
                                    month=_worked_delete.month, 
                                    day=_worked_delete.day, 
                                    user=current_user)
    # print(db_worked)
    if not db_worked:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_worked.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    crud.delete_worked(db=db, db_worked=db_worked)


@router.get("/detail", response_model=schema.Worked)
def worked_detail(year: int, 
                  month: int,
                  day: int,
                  db: Session = Depends(get_db), 
                  current_user:User=Depends(get_current_user)):
    worked = crud.get_worked_ymd(db=db, 
                                 year=year, 
                                 month=month, 
                                 day=day, 
                                 user=current_user)
    if not worked:
        # return {'worked': worked}
        return worked
    if not worked.wage:
        print(worked.note, worked.wage, '-----------------------일한곳 급여')
        worked.wage = crud.get_wage(db=db, year=year, month=month, day=day, note=worked.note, user=current_user)
    print(worked.wage, '====================급여')
    return worked
    # return {'worked': worked}