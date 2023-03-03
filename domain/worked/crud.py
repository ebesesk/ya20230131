import datetime

import sqlalchemy
from sqlalchemy import  and_, or_
from sqlalchemy.orm import Session

from . import schema
from models import User, Worked

def create_worked(db: Session,
                  worked_create:schema.WorkedCreate, 
                  user: User):
    db_worked =  Worked(year = worked_create.year,
                        month = worked_create.month,
                        day = worked_create.day,
                        note = (worked_create.note).strip(),
                        wage = worked_create.wage,
                        create_date = datetime.datetime.now(),
                        user = user)
    db.add(db_worked)
    db.commit()
    
def get_worked_list(db: Session,
                    user: User,
                    year: int = int(datetime.date.today().strftime('%Y')),
                    month: int = int(datetime.date.today().strftime('%m'))):
    worked_list = db.query(Worked).filter(sqlalchemy.and_(
        Worked.user_id == user.id,
        Worked.year == year,
        Worked.month == month
    )).all()
    # print(worked_list)
    return worked_list

def get_worked(db: Session, worked_id: int):
    return db.query(Worked).filter(Worked.id == worked_id).first()

def update_worked(db: Session, db_worked: Worked, worked_update: schema.WorkedUpdate):
    # db_worked.year = worked_update.year
    # db_worked.month = worked_update.month
    # db_worked.day = worked_update.day
    db_worked.note = worked_update.note
    db_worked.wage = worked_update.wage
    # db_worked.user_id = worked_update.user_id
    db.add(db_worked)
    db.commit()

def delete_worked(db: Session, db_worked: Worked):
    db.delete(db_worked)
    db.commit()

def get_worked_ymd(db: Session, year: int, month: int, day: int, user:User):
    worked = db.query(Worked).filter(sqlalchemy.and_(Worked.year == year,
                                                     Worked.month == month,
                                                     Worked.day == day,
                                                     Worked.user_id == user.id
                                                    )).first()
    # print(worked.note, '=================')
    return worked

def get_wage(db: Session, year: int, month: int, day: int, note: str, user:User):
    worked = db.query(Worked).filter(and_(
                                     (Worked.year*10000 + Worked.month*100 + Worked.day) < (year*10000 + month*100 + day) ,
                                     Worked.user_id==user.id, 
                                     Worked.note == note
                                     )).order_by(Worked.create_date.desc()).first()
    if worked == None:
        worked = db.query(Worked).filter(and_(Worked.year <= year,
                                              Worked.month <= month,
                                              Worked.day < day,
                                              Worked.user_id==user.id, 
                                              Worked.wage.is_not(None),
                                              )).order_by(Worked.create_date.desc()).first()
    if worked == None:
        return None
    print(worked.user.username, worked.wage, '+++++++++++++++++')
    return worked.wage