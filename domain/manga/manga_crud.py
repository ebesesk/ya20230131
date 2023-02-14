from datetime import datetime
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import or_, and_, not_

from models import Manga, User, manga_voter

from . import manga_schema


def get_manga(db: Session, manga_id: int):
    return db.query(Manga).get(manga_id)

def get_manga_list(db: Session, skip:int=0, limit:int=0, keyword: str = ''):
    manga_list = db.query(Manga)
    # if keyword:
    #     search = '%{}%'.format(keyword)
    #     sub_
    _manga_list = db.query(Manga).order_by(Manga.created_date.desc())
    total = _manga_list.count()
    manga_list = _manga_list.offset(skip).limit(limit).all()
    return total, manga_list

def bulk_insert_mangas(db: Session, mangas:List[manga_schema.Manga]):
    db.bulk_insert_mappings(Manga, mangas)
    db.commit()

def get_all_mangas(db: Session):
    return db.query(Manga).all()

def bulk_update_mangas(db:Session, mangas:List[manga_schema.Manga_db]):
    db.bulk_update_mappings(Manga, mangas)

def delete_db_list(db:Session, mangas:List[Manga]):
    for manga in mangas:
        db.delete(manga)
    db.commit()

def delete_id(db:Session, _id):
    manga = db.query(Manga).filter(Manga.id == _id)
    manga.delete(synchronize_session=False)
    db.commit()

def vote_manga(db: Session, db_manga: Manga, db_user: User):
    db_manga.voter.append(db_user)
    db.commit()
    
def del_voted_manga(db: Session, db_manga: Manga, db_user: User):
    db_manga.voter.remove(db_user)
    db.commit()
    
def search_manga(db: Session, 
                 skip: int = 0, 
                 limit: int = 0, 
                 keyword: str = '', 
                 vote: bool = False,
                 little: bool = False):

    search = f'%{keyword}%'
    if keyword == '':
        _manga_list = db.query(Manga)
    else:
        _manga_list = db.query(Manga).filter(
                        Manga.title.ilike(search) | Manga.tag.ilike(search)
                      )

    if vote == True:
        _manga_list = _manga_list.join(manga_voter)
    else:
        _manga_list = _manga_list

    if little == True:
        _manga_list = _manga_list.filter(Manga.page < 7)
    else:
        _manga_list = _manga_list.filter(Manga.page > 7)

    total = _manga_list.count()
    manga_list = _manga_list.order_by(Manga.created_date.desc()).offset(skip).limit(limit).all()
    return total, manga_list