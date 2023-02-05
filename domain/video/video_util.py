import os
from config import settings


class Dbid:
    def __init__(self, dbid, VIDEO_DIR):
        self.VIDEO_DIR = VIDEO_DIR
        self.dbid = dbid
        self.file = VIDEO_DIR + self.dbid
        self.name = dbid[dbid.rfind('/')+1:dbid.rfind('.')]
        self.folder = dbid[:dbid.rfind('/')+1]
        self.type = dbid[dbid.rfind('.')+1:]
        self.gif = self.VIDEO_DIR + self.folder + 'gif/' + self.name + '.gif'
        self.folder_gif = self.VIDEO_DIR + self.folder + 'gif/'
        self.webp = self.VIDEO_DIR + self.folder + 'webp/' + self.name + '.webp'
        self.folder_webp = self.VIDEO_DIR + self.folder + 'webp/'
        pass

def scan_dbids(VIDEO_DIR):
    folders = [i for i in os.listdir(VIDEO_DIR)]
    folders.remove('_waste')
    dbids_scanned_files = []
    for i in folders:
        _folder = VIDEO_DIR + '/' + i + '/'
        _file = os.listdir(_folder)
        for j in os.listdir(_folder):
            if j not in ['gif', 'webp', '@eaDir']:
                dbids_scanned_files.append(i + '/' + j)
    return(dbids_scanned_files)

