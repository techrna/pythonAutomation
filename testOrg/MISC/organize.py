import os
import pathlib

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def getDir(val):
    for dType,fType in SUBDIRECTORIES.items():
        if val in fType:
            return dType
    return "MISC"
def organizeFile():
    for x in os.scandir():
        if x.is_dir():
            continue
        fpath=pathlib.Path(x)
        fType=fpath.suffix.lower()
        directory=getDir(fType)
        dPath=pathlib.Path(directory)
        if dPath.is_dir() != True:
            dPath.mkdir()
        fpath.rename(dPath.joinpath(fpath))
organizeFile()


