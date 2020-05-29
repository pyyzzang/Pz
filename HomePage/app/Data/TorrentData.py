from enum import Enum
from ..module.DBExecute import DBExecute

class RowEnum(Enum):
    Title = 0
    MagnetUrl = Title + 1
    ModifyDate = MagnetUrl + 1
    idx = ModifyDate + 1
    ThumbnailImage = idx + 1

class TorrentData:
    def __init__(self, title, magnetUrl, modifyDate, idx):
        self.title = title.strip()
        self.magnetUrl = magnetUrl.strip()
        self.modifyDate = modifyDate
        self.idx = idx

    def getTitle(self):
        return self.title.strip()
        
    def getModifyDate(self):
        return self.modifyDate.strftime("%Y년 %m월 %d일")
    def getMagnetUrl(self):
        return self.magnetUrl
    def getIdx(self):
        return self.idx
    def getStrIdx(self):
        return str(self.getIdx())
    
    @staticmethod
    def createTorrenData(row):
        retData = TorrentData(
        DBExecute.ConvetHangul(row[RowEnum.Title.value]),
        row[RowEnum.MagnetUrl.value],
        row[RowEnum.ModifyDate.value],
        row[RowEnum.idx.value])
        return retData