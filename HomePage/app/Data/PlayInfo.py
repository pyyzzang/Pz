import os;
import json;
import logging
from ..Define import Define;
from threading import Lock;

infoLogger = logging.getLogger("HomePage");

class PlayInfo(object):
    def __init__(self, Title, Position = 0, Duration = 0, Volume = 0, TotalTime = 0, Progress = 0):
        self.Title = Title;
        self.Position = Position;
        self.Duration = Duration;
        self.Volume = Volume;
        self.Progress = Progress;
        
    def getTitle(self):
        return self.Title;
    
    def setPosition(self, Position):
        self.Position = Position;
        try:
            self.Progress = self.getPosition() * 100 / self.getDuration();
        except:
            self.Progress = 0;
    
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
        return self.Progress;

    def getVideoPos(self, value):
        return value * self.getDuration() / 100;


    @classmethod
    def from_json(cls, data):
        return cls(**data);

class PlayInfos(object):
    DataPath = os.path.join(Define.BASE_DIR, 'Data');
    UserInfo = os.path.join(DataPath, "UserInfo");

    def __init__(self, playInfos):
        if (False == os.path.isdir(PlayInfos.DataPath)):
            os.mkdir(PlayInfos.DataPath);

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
            infoLogger.info(e);
        return retPlayInfo;

    def removeInfo(self, removeInfo):
        self.playInfos.remove(removeInfo);
    
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