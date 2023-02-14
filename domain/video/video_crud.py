import datetime
import sqlalchemy
from sqlalchemy import or_, and_, not_
from sqlalchemy.orm import Session
from models import Video, User, video_voter
from . import video_schema

def join_Video_voter(db: Session):
    return db.query(Video).join(video_voter).all()

def get_video_id(db:Session, video_id:int):
    return db.query(Video).get(video_id)

def get_all_videos(db: Session):
    # print(db.query(Video).all())
    return db.query(Video).all()


def del_dbid(db: Session, dbid: str):
    video = db.query(Video).filter(Video.dbid == dbid)
    if not video.first():
        return f'{dbid} db 없음'
    video.delete(synchronize_session=False)
    db.commit()

def input_videoinfo(db: Session, q: video_schema.Video_update):
    video = db.query(Video).filter(Video.id == q['id'])
    q['date_modified'] = datetime.datetime.now()
    video.update(q)
    db.commit()
    
def create_new_video(db: Session, _video: video_schema.Video_create):
    _video['date_posted'] = datetime.datetime.now()
    # print(_video)
    video = Video(**_video)
    db.add(video)
    db.commit()
    db.refresh(video)
    
def get_video_list(db: Session, skip:int=0, limit:int=0, keyword:str=""):
    _video_list = db.query(Video).filter(
        or_(Video.dbid.ilike("%"+keyword+"%"), Video.etc.ilike("%"+keyword+"%"))
        ).order_by(Video.date_posted.desc())
    total = _video_list.count()
    video_list = _video_list.offset(skip).limit(limit).all()
    return total, video_list
    
def vote_video(db: Session, db_video: Video, db_user:User):
    db_video.voter.append(db_user)
    db.commit()
    
def delete_vote(db:Session, db_video: Video, db_user:User):
    db_video.voter.remove(db_user)
    db.commit()

def search_video(db: Session, keyword, skip:int=0, limit:int=0):
    # print(keyword)
    q = []
    j = 0
    for _key in keyword:
        j = j + 1
        if type(keyword[_key]) == list:
            if _key == 'resolution':
                if len(keyword[_key]) > 0:
                    _q = []
                    for value in keyword[_key]:
                        if value == 'high':
                            _q.append((Video.width * Video.height) >= 786432)
                        elif value == 'middle':
                            _q.append(and_(((Video.width * Video.height) < 786432), ((Video.width * Video.height) > 307200)))
                        elif value == 'low':
                            _q.append((Video.width * Video.height) <= 307200)
                        else:
                            continue
                    if 'not' not in keyword[_key]:
                        q.append(or_(*_q))
                    else:
                        q.append(not_(or_(*_q)))


            elif _key == 'display_quality':
                if len(keyword[_key]) > 0:
                    _q = []
                    for value in keyword[_key]:
                        _q.append(Video.display_quality == value)
                    if 'not' not in keyword[_key]:
                        q.append(or_(*_q))
                    else:
                        q.append(not_(or_(*_q)))

  
            elif _key == 'country':
                if len(keyword[_key]) > 0:
                    _q = []
                    for value in keyword[_key]:
                        _q.append(Video.country == value)
                    if 'not' not in keyword[_key]:
                        q.append(or_(*_q))
                    else:
                        q.append(not_(or_(*_q)))
                        

            elif _key == 'face':
                if len(keyword[_key]) > 0:
                    # print(j, _key, 'list')
                    _q = []
                    for value in keyword[_key]:
                        _q.append(Video.face == value)
                    if 'not' not in keyword[_key]:
                        q.append(or_(*_q))
                    else:
                        q.append(not_(or_(*_q)))


            elif _key == 'look':
                if len(keyword[_key]) > 0:
                    # print(j, _key, 'list')
                    _q = []
                    for value in keyword[_key]:
                        _q.append(Video.look == value)
                    if 'not' not in keyword[_key]:
                        q.append(or_(*_q))
                    else:
                        q.append(not_(or_(*_q)))


            elif _key == 'age':
                if len(keyword[_key]) > 0:
                    # print(j, _key, 'list')
                    _q = []
                    for value in keyword[_key]:
                        _q.append(Video.age == value)
                    if 'not' not in keyword[_key]:
                        q.append(or_(*_q))
                    else:
                        q.append(not_(or_(*_q)))


            elif _key == 'pussy':
                if len(keyword[_key]) > 0:
                    # print(j, _key, 'list')
                    _q = []
                    for value in keyword[_key]:
                        _q.append(Video.pussy == value)
                    if 'not' not in keyword[_key]:
                        q.append(or_(*_q))
                    else:
                        q.append(not_(or_(*_q)))


            elif _key == 'etc':
                if len(keyword[_key]) > 0:
                    _q = []
                    if '#not' in keyword[_key]:
                        i = keyword[_key].index('#not')
                        # keyword[_key].remove('not')
                        for value in keyword[_key][:i]:
                            print(value)
                            search = '%{}%'.format(value)
                            _q.append(
                                or_(Video.etc.ilike(search), Video.dbid.ilike(search))
                            )
                        for value in keyword[_key][i+1:]:
                            search = '%{}%'.format(value)
                            _q.append(
                                or_(not_(Video.etc.ilike(search)), not_(Video.dbid.ilike(search)))
                            )
                    else:
                        for value in keyword[_key]:
                            # print(value, 'else')
                            search = '%{}%'.format(value)
                            _q.append(
                                or_(Video.etc.ilike(search), Video.dbid.ilike(search))
                            )
                    # _q.append(Video.etc == None)
                    q.append(and_(*_q))


        elif _key == 'ad_start':
            _q = []
            if keyword[_key] == True:
                _q.append(Video.ad_start != None)
            elif keyword[_key] == False:
                _q.append(Video.ad_start == None)
            q.append(or_(*_q))
                
        elif _key == 'star':
            _q = []
            if keyword[_key] == None:
                _q.append(Video.star == None)
            elif keyword[_key] == True:
                _q.append(Video.star != None)
            elif keyword[_key] == '1':
                _q.append(Video.star == 1)
            elif keyword[_key] == '2':
                _q.append(Video.star == 2)
            elif keyword[_key] == '3':
                _q.append(Video.star == 3)
            elif keyword[_key] == '4':
                _q.append(Video.star == 4)
            elif keyword[_key] == '5':
                _q.append(Video.star == 5)
            q.append(or_(*_q))
            
            
        elif type(keyword[_key]) == bool:
            
            
            if _key == 'school_uniform':
                if keyword[_key] == True:
                    q.append(Video.school_uniform == True)
                elif keyword[_key] == False:
                    q.append(Video.school_uniform != True)
            
            
            if _key == 'hip':
                if keyword[_key] == True:
                    q.append(Video.hip == True)
                elif keyword[_key] == False:
                    q.append(Video.hip != True)
            
            
            
            
            if _key == 'group':
                if keyword[_key] == True:
                    q.append(Video.group == True)
                elif keyword[_key] == False:
                    q.append(Video.group != True)
            
            
            if _key == 'pregnant':
                if keyword[_key] == True:
                    q.append(Video.pregnant == True)
                elif keyword[_key] == False:
                    q.append(Video.pregnant != True)
            
            
            if _key == 'oral':
                if keyword[_key] == True:
                    q.append(Video.oral == True)
                elif keyword[_key] == False:
                    q.append(Video.oral != True)
            
            
            if _key == 'ani':
                if keyword[_key] == True:
                    q.append(Video.ani == True)
                elif keyword[_key] == False:
                    q.append(Video.ani != True)
            
            
            if _key == 'lesbian':
                if keyword[_key] == True:
                    q.append(Video.lesbian == True)
                elif keyword[_key] == False:
                    q.append(Video.lesbian != True)
            
            
            if _key == 'conversation':
                if keyword[_key] == True:
                    q.append(Video.conversation == True)
                elif keyword[_key] == False:
                    q.append(Video.conversation != True)
                    
            
            if _key == 'masturbation':
                if keyword[_key] == True:
                    q.append(Video.masturbation == True)
                elif keyword[_key] == False:
                    q.append(Video.masturbation != True)
            
            
            if _key == 'massage':
                if keyword[_key] == True:
                    q.append(Video.massage == True)
                elif keyword[_key] == False:
                    q.append(Video.massage != True)
            
            
            if _key == 'uniform':
                if keyword[_key] == True:
                    q.append(Video.uniform == True)
                elif keyword[_key] == False:
                    q.append(Video.uniform != True)
            
            
            if _key == 'family':
                if keyword[_key] == True:
                    q.append(Video.family == True)
                elif keyword[_key] == False:
                    q.append(Video.family != True)
            
    
    if 'vote' in keyword and keyword['vote']:
        _video_list = db.query(Video).filter(and_(*q)).join(video_voter).order_by(Video.date_posted.desc())
    else:
        _video_list = db.query(Video).filter(and_(*q)).order_by(Video.date_posted.desc())
    total = _video_list.count()
    video_list = _video_list.offset(skip).limit(limit).all()
    print(total)
    return total, video_list
    
    