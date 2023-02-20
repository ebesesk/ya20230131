from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status 

from . import schema, crud, schema, crud
from ..login.login_router import get_current_user

from database import get_db, get_async_db
from models import User

router = APIRouter()


@router.get("/list", response_model=schema.QuestionList)
def question_list(db: Session = Depends(get_db),
                  page: int = 0, size: int = 10, keyword: str = ''):
    total, _question_list = crud.get_question_list(
        db, skip=page * size, limit=size, keyword=keyword)
    return {
        'total': total,
        'question_list': _question_list
    }


@router.get("/detail/{question_id}", response_model=schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = crud.get_question(db, question_id=question_id)
    return question


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: schema.QuestionCreate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    crud.create_question(db=db, question_create=_question_create,
                                  user=current_user)


@router.put("/update", status_code=status.HTTP_204_NO_CONTENT)
def question_update(_question_update: schema.QuestionUpdate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_question = crud.get_question(db, question_id=_question_update.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")
    crud.update_question(db=db, db_question=db_question,
                                  question_update=_question_update)


@router.delete("/delete", status_code=status.HTTP_204_NO_CONTENT)
def question_delete(_question_delete: schema.QuestionDelete,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    db_question = crud.get_question(db, question_id=_question_delete.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    if current_user.id != db_question.user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="삭제 권한이 없습니다.")
    crud.delete_question(db=db, db_question=db_question)


@router.post("/vote", status_code=status.HTTP_204_NO_CONTENT)
def question_vote(_question_vote: schema.QuestionVote,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    db_question = crud.get_question(db, question_id=_question_vote.question_id)
    if not db_question:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    crud.vote_question(db, db_question=db_question, db_user=current_user)


# async examples
@router.get("/async_list")
async def async_question_list(db: Session = Depends(get_async_db)):
    result = await crud.get_async_question_list(db)
    return result


@router.post("/async_create", status_code=status.HTTP_204_NO_CONTENT)
async def async_question_create(_question_create: schema.QuestionCreate,
                                db: Session = Depends(get_async_db)):
    await crud.async_create_question(db, question_create=_question_create)