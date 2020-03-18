class PlayInfo(object):
    def __init__(self, Title, Position = 0, Duration = 0, Volume = 0):
        self.Title = Title;
        self.Position = Position;
        self.Duration = Duration;
        self.Volume = Volume;

    def getTitle(self):
        return self.Title;
    
    def setPosition(self, Position):
        self.Position = Position;
    
    def setDuration(self, Duration):
        self.Duration = Duration;
    
    def setVolume(self, Volume):
        self.Volume = Volume;

    @classmethod
    def from_json(cls, data):
        return cls(**data);

class PlayInfos(object):
    def __init__(self, playInfos):
        self.playInfos = playInfos;
    @classmethod
    def from_json(cls, data):
        tmpInfos = map(PlayInfo.from_json, data["playInfos"]);
        playInfos = [];
        for info in tmpInfos:
            playInfos.append(info);
        return cls(playInfos);