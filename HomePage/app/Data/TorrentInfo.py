from ..module.strUtil import strUtil;
from ..Define import Define;
import os;
from ..module.osDefine import osDefine;
from threading import Lock;
import json;
from difflib import SequenceMatcher

class torrentInfo():
    def __init__(self, fullName = "", title = "", season = "", episode = "", date = "", count = 1):
        self.fullName = fullName;
        self.title = strUtil.getMatchTitle(self.fullName);
        self.season  = strUtil.getSeason(self.fullName);
        self.episode = strUtil.getEpisode(self.fullName);
        self.date = strUtil.getDate(self.fullName);
        self.count = 1;
    
    def getFullName(self):
        return self.fullName;
        
    def getTitle(self):
        return self.title;

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
    
    def getSimilar(self, compareInfo):
        fullTitleValue = SequenceMatcher(None, self.getFullName(), compareInfo.getFullName()).ratio();
        if(0.4 < fullTitleValue):
            return True;
        titleValue = SequenceMatcher(None, self.getTitle(), compareInfo.getTitle()).ratio();
        if(0.8 < titleValue):
            return True;
        return False;

    def equals(self, compareInfo):
        if(self.getTitle() == compareInfo.getTitle()):
            return True;
        elif(self.getSeason() == compareInfo.getSeason() and    \
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

    def findSimilarTorrintInfo(self, title, isCrate = False):
        addInfo = torrentInfo(title);
        for info in self.infos:
            if(True == info.equals(addInfo)):
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
        for info in torrentInfos.infos:
            osDefine.Logger(info.getCount());
        
        torrentInfos.saveFile();
        return info;