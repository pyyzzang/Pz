from django.http import HttpResponse

from ..module.auzerConnect import Auzer;
from enum import Enum;

class RowEnum(Enum):
    Title = 0
    AlisaTitle = 1
    Binary = 2
    ModifyDate = 3
    idx = 4

class TorrentData:
    def __init__(self, title, aliasTitle, modifyDate):
        self.title = title;
        self.aliasTitle = aliasTitle;
        self.modifyDate = modifyDate;
        self.binaryData = b"";

    def getTitle(self):
        if(0 == len(self.aliasTitle.strip())):
            return self.title;
        return self.aliasTitle;
    def getModifyDate(self):
        return self.modifyDate.strftime("%Y년 %m월 %d일");
    def getBinaryData(self):
        return self.binaryData;

    def getHttpRow(self):
        ret = "<td>" + self.getTitle() + "</td>";
        ret += "<td>" + self.getModifyDate() + "</td>";
        return ret;
    
    @staticmethod
    def createTorrenData(row):
        retData = TorrentData(
        Auzer.ConvetHangul(row[RowEnum.Title.value]),
        Auzer.ConvetHangul(row[RowEnum.AlisaTitle.value]),
        row[RowEnum.ModifyDate.value]);
        return retData;
    
class torrent:
    @staticmethod
    def getTorrent(request):
        rows = Auzer.QueryExecute("select title, AliasTitle, '', modifyDate from Torrent");
        
        ret = "<Table><tr>";
        for row in rows:
            data = TorrentData.createTorrenData(row);
            ret += data.getHttpRow();

        ret += "</tr></table>"

        return HttpResponse(ret);