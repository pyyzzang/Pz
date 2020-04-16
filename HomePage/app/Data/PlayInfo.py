import os;
import json;
import logging
from ..Define import Define;
from threading import Lock;

infoLogger = logging.getLogger("HomePage");

class PlayInfo(object):
    def __init__(self, Title, Position = 0, Duration = 0, Volume = 0, TotalTime = 0):
        self.Title = Title;
        self.Position = Position;
        self.Duration = Duration;
        self.Volume = Volume;
        
    def getTitle(self):
        return self.Title;
    
    def setPosition(self, Position):
        self.Position = Position;
    
    def getPosition(self):
        return self.Position;
    
    def setDuration(self, Duration):
        self.Duration = Duration;
    
    def getDuration(self):
        return self.Duration;
    
    def setVolume(self, Volume):
        self.Volume = Volume;
    
    def getVolume(self):
        return self.Volume;
    
    def getProgressValue(self):
        return self.getPosition() * 100 / self.getDuration();


    @classmethod
    def from_json(cls, data):
        return cls(**data);

class PlayInfos(object):
    DataPath = os.path.join(Define.BASE_DIR, 'Data');
    UserInfo = os.path.join(DataPath, "UserInfo");

    def __init__(self, playInfos):
        self.playInfos = playInfos;

    def getPlayInfo(self, playFileName, isCreate = False):
        retPlayInfo = "";
        try:
            for playInfo in self.playInfos:
                if(playFileName == playInfo.getTitle()):
                    return playInfo;

            if(False == isCreate):
                return retPlayInfo;
            
            retPlayInfo = PlayInfo(playFileName);
            self.playInfos.append(retPlayInfo);
        except Exception as e:
            infoLogger.info("GetPlayInfo : " + e);
        return retPlayInfo;
    
    def saveFile(self):
        criticalSection = Lock();
        with criticalSection:
            with open(PlayInfos.UserInfo, "w") as filePlayInfo:
                json.dump(self, filePlayInfo, default=lambda o: o.__dict__);

    @staticmethod
    def GetPlayInfos():
        saveInfos = PlayInfos([]);
        if (True == os.path.isfile(PlayInfos.UserInfo)):
            with open(PlayInfos.UserInfo, "r") as filePlayInfo:
                saveInfos = PlayInfos.from_json(json.load(filePlayInfo));
        return saveInfos;

    @classmethod
    def from_json(cls, data):
        tmpInfos = map(PlayInfo.from_json, data["playInfos"]);
        playInfos = [];
        for info in tmpInfos:
            playInfos.append(info);
        return cls(playInfos);