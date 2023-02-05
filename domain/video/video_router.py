from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from sqlalchemy.orm import Session


from database import get_db
from .video_crud import get_all_videos, get_video_list, get_video_id, input_videoinfo, del_dbid
from .video_schema import Video_info, Video_info_list, Video_info_input, Video_dbids
# from models import Video
# from db.repository.users import create_new_user
from . import video_util
from config import settings

router =APIRouter()
VIDEO_DIR = settings.VIDEO_DIR

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
    
@router.get("/scan_files")#, response_model=list[Video_dbids])
def view_scanned_files(db: Session=Depends(get_db)):
    videos = get_all_videos(db)
    dbids = [i.dbid for i in videos]
    dbids_scanned_files = video_util.scan_dbids(settings.VIDEO_DIR)
    dbids_del = set(dbids) - set(dbids_scanned_files)
    dbids_detect = set(dbids_scanned_files) - set(dbids)
    for i in dbids_del:
        dbid = video_util.Dbid(dbid=i, VIDEO_DIR=settings.VIDEO_DIR)
        print(dbid.dbid)
        del_dbid(db=db, dbid=dbid.dbid)
    return {
        'deleted dbids': dbids_del,
        'detected files': dbids_detect,
    }
    # return videos   


def get_vmeta_ffmpeg(src):
    print(src)
    try:
        vmeta = ffmpeg.probe(src)
    except ffmpeg._run.Error:
        dest = ROOT_DIR + WASTE_DIR + src[src.rfind('/')+1:]
        # shutil.move(src, dest)
        return "not video file"
    # pprint(vmeta)
    bitrate = vmeta['format']['bit_rate']
    duration = vmeta['format']['duration']
    filesize = vmeta['format']['size']
    try:
        width = vmeta['streams'][0]['coded_width']
        height = vmeta['streams'][0]['coded_height']
    except:
        width = vmeta['streams'][1]['coded_width']
        height = vmeta['streams'][1]['coded_height']
    try:
        date = vmeta['format']['tags']['creation_time']
        date = date[:date.rfind('.')].replace('T', ' ')
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    except:
        return ({
            # '파일명': src, 
            'width': int(width),
            'height': int(height),
            'showtime': int(round(float(duration),0)),
            'bitrate': int(bitrate),
            'size': int(filesize),
            })
    
    return ({
            # '파일명': file_name, 
            'width': int(width),
            'height': int(height),
            'showtime': int(round(float(duration),0)),
            'bitrate': int(bitrate),
            'size': int(filesize),
            'cdate': date,
            })

