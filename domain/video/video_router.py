from fastapi import APIRouter, HTTPException, Depends, status, Request
from typing import List, Dict
from sqlalchemy.orm import Session
from pathlib import Path
import json

from database import get_db
from .video_crud import get_all_videos, get_video_list, get_video_id, input_videoinfo, del_dbid, search_video
from .video_schema import Video_info, Video_info_list, Video_update, Video_dbids
# from models import Video
# from db.repository.users import create_new_user
from . import video_util
from config import settings
from .stream_mp4 import range_requests_response

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
@router.get("/scan_files")#, response_model=list[Video_dbids])
def view_scanned_files(db: Session=Depends(get_db)):
    return video_util.scan_files(db)

@router.get("/add_dbids")
def add_files_to_dbids(db: Session=Depends(get_db)):
    return video_util.add_dbids(db)



# Search.svelte
@router.get("/search")#, response_model=Video_info_list)
def get_search(db: Session=Depends(get_db),
               page: int = 0,
               size: int = 10,
               keyword:str=''):
    keyword = json.loads(keyword)
    
    if 'etc' in [i for i in keyword]:
        if len(keyword['etc']) > 0:
            keyword['etc'] = keyword['etc'].strip().split(',')
    keyword['etc'] = [i.strip() for i in keyword['etc']]
    
    total, video_list = search_video(db=db, keyword = keyword, skip=page*size, limit=size)
    # total, video_list = search_video(db=db, keyword = keyword, skip=page*size, limit=size)
    return {
        'total': total,
        'video_list': video_list
    }


# @router.get("/all", response_model=list[Video_info])
# def view_all(db: Session=Depends(get_db)):
    #     videos = get_all_videos(db)
#     return videos





    










@router.get("/stream")
def get_video(request: Request, dbid: str):
    video_path = Path(settings.VIDEO_DIR + dbid)
    return range_requests_response(request, file_path=video_path, content_type="video/mp4")


