import datetime
from sqlalchemy.orm import Session
from models import Video
from . import video_schema

def get_video_id(db:Session, video_id:int):
    return db.query(Video).filter(Video.id == video_id).first()

def get_all_videos(db: Session):
    # print(db.query(Video).all())
    return db.query(Video).all()

def get_video_list(db: Session, skip:int=0, limit:int=0):
    _video_list = db.query(Video).order_by(Video.date_posted.desc())
    total = _video_list.count()
    video_list = _video_list.offset(skip).limit(limit).all()
    return total, video_list

def del_dbid(db: Session, dbid: str):
    video = db.query(Video).filter(Video.dbid == dbid)
    if not video.first():
        return f'{dbid} db 없음'
    video.delete(synchronize_session=False)
    db.commit()

def input_videoinfo(db: Session, q: video_schema.Video_update):
    video = db.query(Video).filter(Video.id == q.id)
    video.update(q.__dict__)
    db.commit()
    
def create_new_video(db: Session, _video: video_schema.Video_create):
    _video['date_posted'] = datetime.datetime.now()
    print(_video)
    video = Video(**_video)
    db.add(video)
    db.commit()
    db.refresh(video)
    