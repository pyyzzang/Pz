from ..module.strUtil import strUtil;
from ..Define import Define;
import os;
from ..module.osDefine import osDefine;
from threading import Lock;
import json;
from difflib import SequenceMatcher

class torrentInfo():
    def __init__(self, fullName = "", title = "", season = "", episode = "", date = "", count = 1, similarTitle = ""):
        self.fullName = fullName;
        self.title = strUtil.getMatchTitle(self.fullName);
        self.similarTitle = strUtil.getSimilarTitle(self.fullName);
        self.season  = strUtil.getSeason(self.fullName);
        self.episode = strUtil.getEpisode(self.fullName);
        self.date = strUtil.getDate(self.fullName);
        self.count = count;
    
    def getFullName(self):
        return self.fullName;
        
    def getTitle(self):
        return self.title;

    def getSimilarTitle(self):
        return self.similarTitle;

    def getSeason(self):
        return self.season;

    def getEpisode(self):
        return self.episode;

    def getDate(self):
        return self.date;
    
    def getCount(self):
        return self.count;

    def incrementCount(self):
        self.count = self.count + 1;
        return self.count;
    
    def getSimilar(self, compareInfo, compareValue = 0.8):
        titleValue = SequenceMatcher(None, self.getSimilarTitle(), compareInfo.getSimilarTitle()).ratio();
        if(compareValue < titleValue):
            return True;
        return False;

    def equals(self, compareInfo):
        if(self.getTitle() == compareInfo.getTitle()):
            return True;
        elif (True == self.getSimilar(compareInfo) and              \
            self.getSeason() == compareInfo.getSeason() and         \
            self.getEpisode() == compareInfo.getEpisode()):
            return True;
        return False;

    def toString(self):
        return "FullName : " + self.getFullName() + \
            "Title : " + self.getTitle() + \
            "Season : " + self.getSeason() + \
            "Episode : " + self.getEpisode() + \
            "Date : " + self.getDate();

    @classmethod
    def from_json(cls, data):
        return cls(**data);

class TorrentInfos(object):
    DataPath = os.path.join(Define.BASE_DIR, 'Data');
    TorrentInfoFile = os.path.join(DataPath, "TorrentInfo");

    def __init__(self, infos):
        if (False == os.path.isdir(TorrentInfos.DataPath)):
            os.mkdir(TorrentInfos.TorrentInfoFile);

        self.infos = infos;

    def saveFile(self):
        criticalSection = Lock();
        with criticalSection:
            
            with open(TorrentInfos.TorrentInfoFile, "w") as fileTorrentInfo:
                json.dump(self, fileTorrentInfo, default=lambda o: o.__dict__);
    
    def deleteInfo(self, title):
        for info in self.infos:
            if(title == info.getTitle()):
                self.infos.remove(info);
                break;
        self.saveFile();
        return title;

    def findSimilarTorrintInfo(self, title, isCrate = False):
        addInfo = torrentInfo(title);
        for info in self.infos:
            if(True == info.getSimilar(addInfo)):
                osDefine.Logger("title : " + title + " info.FullName : " + info.getFullName());
                info.incrementCount();
                return info;
        if(True == isCrate):
            self.infos.append(addInfo);
            return addInfo;
        return None;

    @classmethod
    def from_json(cls, data):
        tmpInfos = map(torrentInfo.from_json, data["infos"]);
        infos = [];
        for info in tmpInfos:
            infos.append(info);
        return cls(infos);

    @staticmethod
    def GetTorrentInfos():
        infos = TorrentInfos([]);
        if (True == os.path.isfile(TorrentInfos.TorrentInfoFile)):
            with open(TorrentInfos.TorrentInfoFile, "r") as filePlayInfo:
                infos = TorrentInfos.from_json(json.load(filePlayInfo));
        return infos;
    
    @staticmethod
    def updateTorrentInfo(title):
        torrentInfos = TorrentInfos.GetTorrentInfos();
        info = torrentInfos.findSimilarTorrintInfo(title, True);
        torrentInfos.saveFile();
        return info;
    
    @staticmethod 
    def Delete(title):
        try:
            infos = TorrentInfos.GetTorrentInfos();
            infos.deleteInfo(title);
        except Exception as e:
            osDefine.Logger(e);
        return title;
