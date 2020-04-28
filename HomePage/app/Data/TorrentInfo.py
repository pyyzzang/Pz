from ..module.strUtil import strUtil;

class torrentInfo():
    def __init__(self, fullName):
        self.fullName = fullName;
        self.title = strUtil.getMatchTitle(self.fullName);
        self.season  = strUtil.getSeason(self.fullName);
        self.episode = strUtil.getEpisode(self.fullName);
        self.date = strUtil.getDate(self.fullName);
    
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
    
    def toString(self):
        return "FullName : " + self.getFullName() + \
            "Title : " + self.getTitle() + \
            "Season : " + self.getSeason() + \
            "Episode : " + self.getEpisode() + \
            "Date : " + self.getDate();