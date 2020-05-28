import os;
import re;
from difflib import SequenceMatcher

import os
import re


class strUtil:
    tvPattern = 0
    movePattern = 0

    @staticmethod
    def init():
        strUtil.titlePattern = '.+.E\d+'

    @staticmethod
    def isMatchTitle(title):
        strUtil.init()
        if(re.search(strUtil.titlePattern, title)):
            return True
        return False

    @staticmethod
    def getRegulaString(str, pattern):
        regulTitle = re.compile(pattern)
        result = regulTitle.findall(str)
        return result

    @staticmethod
    def getMatchTitle(title):
        strUtil.init()
        fileName = os.path.split(title)[1]
        result = strUtil.getRegulaString(fileName, strUtil.titlePattern)
        length = len(result)
        if(0 != length):
            return result[length - 1]
        return fileName
  
    @staticmethod
    def getRegularText(text, pattern, default = ""):
        regulText = re.compile(pattern)
        result = regulText.findall(text)
        if(0 != len(result)):
            return result[0];
        return default;
    
    @staticmethod
    def getSeason(text):
        season = strUtil.getRegularText(text, "S\d\d");
        return strUtil.getRegularText(season, "\d\d");

    @staticmethod
    def getEpisode(text):
        episode = strUtil.getRegularText(text, "E\d{2,6}|\d{2,6}회|E.\d{2,6}");
        return strUtil.getRegularText(text, "\d{2,6}");
    
    @staticmethod
    def getDate(text):
        date = strUtil.getRegularText(text, "['\.',' ']\d{4,6}\.");
        return strUtil.getRegularText(date, "\d{4,6}");

titles = {"요즘책방책읽어드립니다E10.720p.WEB-DL.x264.AAC-Deresisi",
"tvn요즘책방책읽어드립니다.E09.191119.H264.720p",
"tvn요즘책방책읽어드립니다.E11.191203.H264.720p",
"요즘책방책읽어드립니다E12.191210.720p.WEB-DL.x264.AAC-Deresisi",
"요즘책방책읽어드립니다E30.200427.1080p.WEB-DL.x264.AAC-Deresisi",
"요즘책방책읽어드립니다E30.200427.720p.WEB-DL.x264.AAC-Deresisi",
"요즘책방책읽어드립니다E29.200420.1080p.WEB-DL.x264.AAC-Deresisi",
"요즘책방책읽어드립니다E29.200420.720p.WEB-DL.x264.AAC-Deresisi",
"요즘책방-책읽어드립니다E28.200413.1080p.WEB-DL.x264.AAC-Deresisi",
"요즘책방-책읽어드립니다.E28.200413.720p-NEXT",
"요즘책방-책읽어드립니다E28.200413.720p.WEB-DL.x264.AAC-Deresisi",
"요즘책방-책읽어드립니다.E27.200406.720p-NEXT",
"요즘책방-책읽어드립니다E27.200406.1080p.WEB-DL.x264.AAC-Deresisi",
"요즘책방-책읽어드립니다E27.200406.720p.WEB-DL.x264.AAC-Deresisi",
"요즘책방-책읽어드립니다.E26.200330.720p-NEXT",
"요즘책방-책읽어드립니다.E24.200317.720p-NEXT",
"요즘책방-책읽어드립니다.E23.200310.720p-NEXT",
"요즘책방-책읽어드립니다.E22.200303.720p-NEXT.mp4",
"요즘책방-책읽어드립니다.E20.200218.720p-NEXT",
"요즘책방-책읽어드립니다.E19.200211.720p-NEXT",
"요즘책방-책읽어드립니다.E17.200128.720p-NEXT.mp4",
"요즘책방-책읽어드립니다.E14.200107.720p-NEXT.mp4",
"tvN요즘책방:책읽어드립니다EP01-13.1080p.WEB-DL.x264.AAC-Deresisi",
"tvn요즘책방책읽어드립니다.E12.191210.H264.720p",}

addTitles = {
"오지GO 아마존 of 아마존 E02.200427.1080p.WEB-DL.x264.AAC-Deresisi",
"오지GO 아마존 of 아마존 E02.200427.720p.WEB-DL.x264.AAC-Deresisi",
#"77억의 사랑 E12.200427.1080p.WEB-DL.x264.AAC-Deresisi",
#"77억의 사랑 E12.200427.720p.WEB-DL.x264.AAC-Deresisi",
#"요즘책방 책 읽어드립니다 E30.200427.1080p.WEB-DL.x264.AAC-Deresisi",
#"본 어게인.S01E05E06.1080p.HDTV.x265-0utlaw",
#"그 겨울 바람이 분다 That.Winter.the.Wind.Blows.S01.1080p.NF.WEB-DL.DDP2.0.x264…",
#"생활의 발견.E670.200428.720p-NEXT.mp4",
#"판도라.E167.200427.720p-NEXT.mp4",
};

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

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()




infos = list();
for addTitle in addTitles:
    addInfo = torrentInfo(addTitle);
    for tmpTitle in addTitles:
        if(False == ("책방" in tmpTitle)):
            continue;
        tmpInfo = torrentInfo(tmpTitle);
        if(True == addInfo.equals(tmpInfo)):
            print("Add Name : " + addInfo.getEpisode());
            print("Tmp Name : " + tmpInfo.getEpisode());
            break;