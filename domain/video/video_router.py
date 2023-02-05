from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from sqlalchemy.orm import Session


from database import get_db
from .video_crud import get_all_videos, get_video_list, get_video_id, input_videoinfo
from .video_schema import Video_info, Video_info_list, Video_info_input
# from models import Video
# from db.repository.users import create_new_user

router =APIRouter()


@router.get("/detail/{video_id}", response_model=Video_info)
def get_video(video_id: int, db: Session = Depends(get_db)):
    video = get_video_id(db=db, video_id=video_id)
    return video

@router.get("/all", response_model=list[Video_info])
def view_all(db: Session=Depends(get_db)):
    videos = get_all_videos(db)
    return videos


@router.get("/list", response_model=Video_info_list)
def get_list(db: Session = Depends(get_db),
                   page: int = 0,
                   size: int = 10):
    total, video_list = get_video_list(db=db, skip=page*size, limit=size)
    # manga_list = []
    # for manga in _manga_list:
    #     images = manga_util.get_images(manga.title)
    #     manga_list.append({'id': manga.id,'title': manga.title,'tag': manga.tag,'created_date': manga.created_date, 'images': images})
        
    return {
        'total': total,
        'video_list': video_list
    }

@router.put("/input_videoinfo", status_code=status.HTTP_204_NO_CONTENT)
def input_modified_videoinfo(_video_info: Video_info_input, db:Session=Depends(get_db)):
    # from urllib.parse import unquote
    # _video_info.dbid = unquote(_video_info.dbid)
    
    input_videoinfo(db=db, q=_video_info)