from fastapi import APIRouter, HTTPException, Depends, status, Request
from typing import List, Dict
from sqlalchemy.orm import Session
from pathlib import Path
import json

from database import get_db
from .video_crud import (get_all_videos, get_video_list, get_video_id, 
                         input_videoinfo, del_dbid, search_video, 
                         vote_video, delete_vote)
from .video_schema import (Video_info, Video_info_list, Video_update, 
                           Video_dbids, VideoVote, Scanreturn)
# from models import Video
# from db.repository.users import create_new_user
from . import video_util
from config import settings
# from .stream_mp4 import range_requests_response
from ..login.login_router import get_current_user
from models import User

router =APIRouter()
VIDEO_DIR = settings.VIDEO_DIR



# Video.svelte 동영상홈
@router.get("/list", response_model=Video_info_list)
def get_list(db: Session = Depends(get_db),
             page: int = 0,
             size: int = 10,
             keyword: str = ''
             ):
    total, video_list = get_video_list(db=db, skip=page*size, limit=size, keyword=keyword)
    return {
        'total': total,
        'video_list': video_list
    }


# VideoInfo.svelte
@router.get("/detail/{video_id}", response_model=Video_info)
def get_video(video_id: int, db: Session = Depends(get_db)):
    video = get_video_id(db=db, video_id=video_id)
    return video

@router.put("/input_videoinfo", status_code=status.HTTP_204_NO_CONTENT)
def input_modified_videoinfo(_video_info: Video_update, db:Session=Depends(get_db)):
    # from urllib.parse import unquote
    # _video_info.dbid = unquote(_video_info.dbid)
    video_info = {}
    for i, j in enumerate(_video_info):
        video_info[j[0]] = j[1]
        if j[1] == 'del':
            video_info[j[0]] = None
    # print(video_info)
    input_videoinfo(db=db, q=video_info)
    # return _video_info




# Scanfiles.svelte
@router.get("/scan_files", response_model=Scanreturn)
def file_scan(db: Session=Depends(get_db)):
    # video_util.scan_files(db)
    return video_util.scan_files(db)




# @router.post("/add_dbids")
# def add_files_to_dbids(db: Session=Depends(get_db),
#                        detect_files: Addfiles=[]):
#     print(detect_files)
#     # video_util.add_dbids(db, detect_files)
#     # return video_util.add_dbids(db)



# Search.svelte
@router.get("/search", response_model=Video_info_list)
def get_search(db: Session=Depends(get_db),
               page: int = 0,
               size: int = 10,
               keyword:str=''):
    keyword = json.loads(keyword)
    if 'etc' in [i for i in keyword] and len(keyword['etc']) > 0:
        keyword['etc'] = keyword['etc'].strip().split(',')
    keyword['etc'] = [i.strip() for i in keyword['etc']]
    # 빈값 삭제
    keyword_copy = keyword.copy()
    for k in keyword_copy:
        if type(keyword[k]) == list and len(keyword[k]) == 0 :
            del keyword[k]
    # print(keyword)
    total, video_list = search_video(db=db, keyword = keyword, skip=page*size, limit=size)
    # total, video_list = search_video(db=db, keyword = keyword, skip=page*size, limit=size)
    return {
        'total': total,
        'video_list': video_list
    }

@router.post("/vote", status_code=status.HTTP_204_NO_CONTENT)
def video_vote(_video_vote: VideoVote,
               db: Session = Depends(get_db),
               current_user: User = Depends(get_current_user)):
    db_video = get_video_id(db, video_id=_video_vote.video_id)
    if not db_video:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")
    vote_video(db=db, db_video=db_video, db_user=current_user)

@router.delete("/delvote", status_code=status.HTTP_204_NO_CONTENT)
def video_delete_voted(_video_vote: VideoVote,
                       db: Session = Depends(get_db),
                       current_user: User = Depends(get_current_user)):
    db_video = get_video_id(db = db,
                            video_id = _video_vote.video_id)
    if not db_video:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail = "데이터를 찾을수 없습니다.")
    delete_vote(db = db, 
                db_video = db_video, 
                db_user = current_user)
        


# @router.get("/all", response_model=list[Video_info])
# def view_all(db: Session=Depends(get_db)):
    #     videos = get_all_videos(db)
#     return videos





    










@router.get("/stream")
def get_video(request: Request, dbid: str):
    video_path = Path(settings.VIDEO_DIR + dbid)
    return range_requests_response(request, file_path=video_path, content_type="video/mp4")


'''
['/home/video/yadong/20230214/video_2.ts',
 '/home/video/yadong/20230214/Twenty five Japanese women sucking and fucking in one room - IN3X.NET.ts',
 '/home/video/yadong/20230214/MUSUME-122922_01 The year-end party after a long time i_2.ts',
 '/home/video/yadong/20230214/FC2-PPV-1728678 [No appearance] play busty shaved activ.ts',
 '/home/video/yadong/20230214/JAV Hardcore Orgy Sex - 야동코리아.ts',
 '/home/video/yadong/20230214/엉덩이에 눈이 [2분 22초] - 한국야동 - 야동 무료야동 - 야팡.ts',
 '/home/video/yadong/20230214/FC2-PPV-3177333 980pt until 2_7 [Twice creampie] almost.ts',]

'''