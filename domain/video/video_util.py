from datetime import datetime
import os
import integv
import ffmpeg
from PIL import Image
import cv2
# from fastapi import Depends
# from sqlalchemy.orm import Session


# from database import get_db
from config import settings
from . import video_crud

GIF_FRAMES_MAX = int(settings.GIF_FRAMES_MAX)
GIF_FRAMES_MIN = int(settings.GIF_FRAMES_MIN)
GIF_SIZE = settings.GIF_SIZE
TEMP_DIR = settings.TEMP_DIR
class Dbid:
    def __init__(self, dbid):
        VIDEO_DIR = settings.VIDEO_DIR
        GIF_FRAMES_MIN = settings.GIF_FRAMES_MIN
        GIF_FRAMES_MAX  = settings.GIF_FRAMES_MAX
        GIF_SIZE = settings.GIF_SIZE
        self.dbid = dbid
        self.file = VIDEO_DIR + self.dbid
        self.name = dbid[dbid.rfind('/')+1:dbid.rfind('.')]
        self.folder = dbid[:dbid.rfind('/')+1]
        self.type = dbid[dbid.rfind('.')+1:]
        self.folder_gif = VIDEO_DIR + self.folder + 'gif/'
        self.webp = VIDEO_DIR + self.folder + 'webp/' + self.name + '.webp'
        self.folder_webp = VIDEO_DIR + self.folder + 'webp/'
        self.gif = VIDEO_DIR + self.folder + 'gif/' + self.name + '.gif'
        self.showtime = None
        # self.frames = None
        pass
    def gif_frames(self):
        if GIF_FRAMES_MIN > int(self.showtime / 120):
            return GIF_FRAMES_MIN
        if GIF_FRAMES_MAX < int(self.showtime / 120):
            return GIF_FRAMES_MAX
        else:
            return int(self.showtime / 120)
    def get_gif_cuts(self):
        cut_times = []
        frames = self.gif_frames()
        for i in range(frames):
            cut_times.append(int( ((self.showtime) - i*self.showtime/frames) - self.showtime/(2*frames) ))
        cut_times.sort()
        return cut_times
    
def scan_dbids(VIDEO_DIR):
    folders = [i for i in os.listdir(VIDEO_DIR)]
    folders.remove('_waste')
    dbids_scanned_files = []
    dbids_scanned_files_origin = []
    for i in folders:
        _folder = VIDEO_DIR + '/' + i + '/'
        _file = os.listdir(_folder)
        for j in os.listdir(_folder):
            if j not in ['gif', 'webp', '@eaDir', 'Thumbs.db']:
                dbids_scanned_files.append(i + '/' + j)
    return(dbids_scanned_files)

def scan_gif_webp(VIDEO_DIR):
    folders = [i for i in os.listdir(VIDEO_DIR)]
    folders.remove('_waste')
    if 'Thumbs' in folders:
        folders.remove('Thumbs')
    gif_scanned_files = []
    webp_scanned_files = []
    for i in folders:
        _folder = VIDEO_DIR + '/' + i + '/' + 'gif'
        for j in os.listdir(_folder):
            if j not in ['@eaDir', 'Thumbs.db']:
                gif_scanned_files.append(i + '/' + j[:j.rfind('.')])
    for i in folders:
        _folder = VIDEO_DIR + '/' + i + '/' + 'webp'
        for j in os.listdir(_folder):
            if j not in ['@eaDir', 'Thumbs.db']:
                webp_scanned_files.append(i + '/' + j[:j.rfind('.')])
    return {
        'gif': gif_scanned_files,
        'webp': webp_scanned_files
    }            
    
def check_corruptd_video(_file, file_type):
    try:
        return integv.verify(_file, file_type)
    except OverflowError as e:
        return 'OverflowError'
    except NotImplementedError as e:
        return 'NotImplementedError'
    except FileNotFoundError as e:
        return 'FileNotFoundError'


def get_createDate_ffmpeg(src):
    try:
        vmeta = ffmpeg.probe(src)
    except ffmpeg._run.Error:
        dest = ROOT_DIR + WASTE_DIR + src[src.rfind('/')+1:]
        # shutil.move(src, dest)
        return "not video file"
    # pprint(vmeta)
    duration = vmeta['format']['duration']
    try:
        date = vmeta['format']['tags']['creation_time']
        date = date[:date.rfind('.')].replace('T', ' ')
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    except:
        return ({
            'showtime': int(round(float(duration),0)),
            'cdate': None
        })
    
    return ({
        'showtime': int(round(float(duration),0)),
        'cdate': date,
    })

def scan_files(db):
    videos = video_crud.get_all_videos(db=db)
    dbids = [i.dbid for i in videos]
    
    dbids_name = [i[:i.rfind('.')] for i in dbids]
    gif_webp = scan_gif_webp(settings.VIDEO_DIR)
    gif_del = set(gif_webp['gif']) - set(dbids_name)
    webp_del = set(gif_webp['webp']) - set(dbids_name)
    
    dbids_scanned_files = scan_dbids(settings.VIDEO_DIR)
    dbids_del = set(dbids) - set(dbids_scanned_files)
    dbids_detect = set(dbids_scanned_files) - set(dbids)
    print(dbids_detect, '----00-00-0-0')
    
    dbids_detect_name_100 = []
    for d in dbids_detect:
        dbid = Dbid(d)
        print(dbid.name, '---------------------')
        if len(dbid.name) > 100:
            src = dbid.file
            dest = settings.VIDEO_DIR + dbid.folder + dbid.name[0:99]
            os.rename(src, dest)
            dbids_detect_name_100.append()
        else:
            dbids_detect_name_100.append(dbid.dbid)
    for i in dbids_del:
        dbid = video_util.Dbid(dbid=i, VIDEO_DIR=settings.VIDEO_DIR)
        # print(dbid.dbid)
        del_dbid(db=db, dbid=dbid.dbid)
    return {
        'deleted_gif': gif_del,
        'deleted_webp': webp_del,
        'deleted_dbids': dbids_del,
        'detected_files': dbids_detect_name_100,
    }

def cnv_tsTomp4(dbid):
    file = dbid.file
    _ts = file
    _mp4 = file[:file.rfind('.')] + '.mp4'
    command = f'ffmpeg -i {_ts} -acodec copy -vcodec copy {_mp4}'
    # print(_ts,'      ===========')
    # print(_mp4,'     ===========')
    # print(command)
    subprocess.run(['ffmpeg', '-y', '-i',  _ts, '-acodec', 'copy', '-vcodec', 'copy', _mp4])
    os.remove(_ts)
    return dbid.dbid.replace('ts', 'mp4').replace('TS', 'mp4')

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
            'filesize': int(filesize),
            })
    
    return ({
            # '파일명': file_name, 
            'width': int(width),
            'height': int(height),
            'showtime': int(round(float(duration),0)),
            'bitrate': int(bitrate),
            'filesize': int(filesize),
            'cdate': date,
            })

def make_gif(dbid):
    vidcap =cv2.VideoCapture(dbid.file)
    imgs = []
    cut_times = dbid.get_gif_cuts()
    for i, cut_time in enumerate(dbid.get_gif_cuts()):
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        if fps == 1:
            return 'Image file'
        vidcap.set(cv2.CAP_PROP_POS_MSEC, cut_time*1000)
        success, image = vidcap.read()
        if success == False:
            return False
        if success:
            if image.shape[1] > GIF_SIZE:
                image = cv2.resize(image, (GIF_SIZE, int(GIF_SIZE*image.shape[0]/image.shape[1])))
            filename = TEMP_DIR + str(i).zfill(2) + '.png'
            cv2.imwrite(filename, image)
            imgs.append(filename)
    vidcap.release()
    imgs = [Image.open(f) for f in imgs]
    frame_one = imgs[0]
    frame_one.save(dbid.gif, format='GIF', append_images=imgs,
                   save_all=True, duration=500, loop=0)
    return dbid.gif

def make_webp(dbid):
    vidcap = cv2.VideoCapture(dbid.file)
    vidcap.set(cv2.CAP_PROP_POS_MSEC, dbid.showtime*1000/2)
    success, image = vidcap.read()
    if success == False:
        return False
    if success:
        if image.shape[1] > GIF_SIZE:
            image = cv2.resize(image, (GIF_SIZE, int(GIF_SIZE*image.shape[0]/image.shape[1])))
        cv2.imwrite(dbid.webp, image)
        vidcap.release()
        return dbid.webp

def make_rotate_webp(dbid):
    vidcap = cv2.VideoCapture(dbid.file)
    vidcap.set(cv2.CAP_PROP_POS_MSEC, dbid.showtime*1000/2)
    success, image = vidcap.read()
    # print('success', success)
    print(dbid.file)
    if success == False:
        return False
    if success:
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        if image.shape[1] > GIF_SIZE:
            image = cv2.resize(image, (GIF_SIZE, int(GIF_SIZE*image.shape[0]/image.shape[1])))
        cv2.imwrite(dbid.webp, image)
        vidcap.release()
        return dbid.webp

def make_rotate_gif(dbid):
    vidcap =cv2.VideoCapture(dbid.file)
    imgs = []
    for i, cut_time in enumerate(dbid.get_gif_cuts()):
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        if fps == 1:
            return 'Image file'
        vidcap.set(cv2.CAP_PROP_POS_MSEC, dbid.get_gif_cuts()*1000)
        success, image = vidcap.read()
        if success == False:
            return False
        if success:
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            if image.shape[1] > GIF_SIZE:
                image = cv2.resize(image, (GIF_SIZE, int(GIF_SIZE*image.shape[0]/image.shape[1])))
            filename = TEMP_DIR + str(i).zfill(2) + '.png'
            cv2.imwrite(filename, image)
            imgs.append(filename)
    vidcap.release()
    imgs = [Image.open(f) for f in imgs]
    frame_one = imgs[0]
    frame_one.save(dbid.gif, format='GIF', append_images=imgs,
                   save_all=True, duration=500, loop=0)
    return dbid.gif



def add_dbids(db):
    dbids = scan_files(db)
    # print(type(dbids))
    # print(dbids['deleted_dbids'])
    # print(dbids['detected_files'])
    result = {
        'OverflowError':[],
        'NotImplementedError': [],
        'FileNotFoundError': [],
        '알수없는에러': [],
        'db_추가': [],
        'converted': [],
        'make_gif': [],
        'make_webp': []
    }
    for i in dbids['detected_files']:
        # print(i)
        dbid = Dbid(dbid=i)
        # print(dbid.type, '.......................')
        validate = check_corruptd_video(dbid.file, dbid.type)    # 비디오 검사
        # print(validate)
        if validate == 'OverflowError':
            result['OverflowError'].append(i)
        if validate == 'NotImplementedError':
            result['NotImplementedError'].append(i)
        if validate == 'FileNotFoundError':
            result['FileNotFoundError'].append(i)
        
        d = get_createDate_ffmpeg(dbid.file)
        # print(d['showtime'])
        dbid.showtime = d['showtime']
        if d['cdate'] != None:
            dbid.cdate = d['cdate']
        if dbid.type in ['ts', 'TS']:
            r = cnv_tsTomp4(dbid.file)          # ts => mp4 변환
            result['converted'].append(r)
            dbid = Dbid(r)
        video_dbid = get_vmeta_ffmpeg(dbid.file)
        # print(dbid.gif_frames())
        # print(dbid.get_gif_cuts())
        if (video_dbid['width'] > video_dbid['height']):
            result['make_gif'].append(make_gif(dbid))
            result['make_webp'].append(make_webp(dbid))
        else:
            result['make_gif'].append(make_rotate_gif(dbid))
            result['make_webp'].append(make_rotate_webp(dbid))
        # print(video_dbid)
        
        # gif_frames = dbid.gif_frames(GIF_FRAMES_MIN=GIF_FRAMES_MIN, GIF_FRAMES_MAX=GIF_FRAMES_MAX)
        # dbid.gif_frames = gif_frames
        # dbid.gif_size = settings.GIF_SIZE
        # dbid.gif_cut_times(GIF_FRAMES_MIN=GIF_FRAMES_MIN, GIF_FRAMES_MAX=GIF_FRAMES_MAX)
        # print(dbid.gif_cuts)
        video_dbid['dbid'] = dbid.dbid
        video_crud.create_new_video(db=db, _video=video_dbid)
        result['db_추가'].append(dbid.dbid)
        # print(video_dbid)
        
        
    # print(dbids)
    return result