import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import schema, crud
from ..login.login_router import get_current_user

from database import get_db
from models import User 


router = APIRouter()


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
    db_worked = crud.get_worked(db, worked_id=_worked_update.worked_id)
    if not db_worked:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_worked.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    crud.update_worked(db=db, db_worked=db_worked,
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