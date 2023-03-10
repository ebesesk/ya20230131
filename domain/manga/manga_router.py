import datetime, os
from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Manga, User

from ..login.login_router import get_current_user
from . import manga_schema
from .manga_crud import (bulk_insert_mangas, get_all_mangas, delete_db_list, 
                         get_manga_list, delete_id, vote_manga, get_manga,
                         search_manga,del_voted_manga)
from . import manga_util

from config import settings


router = APIRouter()


@router.get("/refresh")#, response_model=List[manga_schema.Manga])
def manga_refresh(db: Session = Depends(get_db)):
    
    mangas_dir = manga_util.get_manga_list()
    mangas_db = get_all_mangas(db)
    manga_titles = [i.title for i in mangas_db]
    
    # 추가된 만화 DB 등록
    mangas_new = []
    for manga in mangas_dir:
        if manga['title'] not in manga_titles:
            mangas_new.append(manga)
    bulk_insert_mangas(db=db, mangas=mangas_new)
    
    # 삭제한 만화 DB 삭제
    mangas_empty = []
    for manga in mangas_db:
        if manga.title not in [i['title'] for i in mangas_dir]:
            mangas_empty.append(manga)
    delete_db_list(db=db, mangas=mangas_empty)
    
    return {'new':mangas_new}


@router.get("/list", response_model=manga_schema.MangaList)
# @router.get("/list", response_model=manga_schema.MangaList)
def get_list(db: Session = Depends(get_db),
                   page: int = 0,
                   size: int = 10):
    # get_manga_list(db=db, skip=page*size, limit=size)
    total, _manga_list = get_manga_list(db=db, skip=page*size, limit=size)
    manga_list = []
    for manga in _manga_list:
        images = manga_util.get_images(manga.title)
        if images:
            manga_list.append({'id': manga.id,
                               'title': manga.title,
                               'tag': manga.tag,
                               'created_date': manga.created_date,
                               'voter': manga.voter, 
                               'images': images})
        else:
            delete_id(db, manga.id)
    return {
        'total': total,
        'manga_list': manga_list
    }


@router.post("/vote", status_code=status.HTTP_204_NO_CONTENT)
def manga_vote(_manga_vote: manga_schema.MangaVote,
               db: Session = Depends(get_db),
               current_user: User = Depends(get_current_user)):
        
    db_manga = get_manga(db, manga_id=_manga_vote.manga_id)
    # print(db_manga.voter[0].username)
    if not db_manga:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    vote_manga(db=db, 
               db_manga=db_manga, 
               db_user=current_user)
    
@router.delete("/delvote", status_code=status.HTTP_204_NO_CONTENT)
def manga_delete_voted(_manga_vote: manga_schema.MangaVote,
                       db: Session = Depends(get_db),
                       current_user: User = Depends(get_current_user),):
    db_manga = get_manga(db, manga_id=_manga_vote.manga_id)
    if not db_manga:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    del_voted_manga(db=db, 
                    db_manga = db_manga, 
                    db_user = current_user,)
    

    
@router.get("/search", response_model=manga_schema.MangaList)
def manga_search(db: Session = Depends(get_db),
                 page: int = 0,
                 size: int = 10,
                 keyword: str = '',
                 vote: bool = False,
                 little: bool = False):
    # print(keyword, page, vote, little)
    total, _manga_list = search_manga(db=db,
                                      skip=page*size, 
                                      limit=size, 
                                      keyword=keyword.strip(), 
                                      vote=vote,
                                      little=little)
    manga_list = []
    for manga in _manga_list:
        images = manga_util.get_images(manga.title)
        # print('length images: ',len(images))
        if images:
            manga_list.append({'id': manga.id,
                               'title': manga.title,
                               'tag': manga.tag,
                               'created_date': manga.created_date,
                               'voter': manga.voter,
                               'images': images})
        else:
            # manga_util.delete_folder_mangatitle(mangatitle=manga.title)
            delete_id(db, manga.id)
    return {
        'total': total,
        'manga_list': manga_list
    }