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


titles = {"놀라운 토요일 도레미 마켓.E108.200516.720p-NEXT다운로드를 실행합니다.",
"생활의 달인.E743.200525.720p-NEXT다운로드를 실행합니다.",
"기분 좋은 날.E3201.200507.720p-NEXT다운로드를 실행합니다.",
"기분 좋은 날.E3195.200501.720p-NEXT다운로드를 실행합니다.",
"생활의 발견.E670.200428.720p-NEXT다운로드를 실행합니다.",
"놀라운 토요일 도레미 마켓.E101.200321.1080p-NEXT다운로드를 실행합니다.",
"놀라운 토요일 도레미 마켓.E101.200321.1080p-NEXT다운로드를 실행합니다.",
"놀라운 토요일 도레미 마켓.E99.200307.720p-NEXT다운로드를 실행합니다.",
"놀라운 토요일 도레미 마켓.E95.200208.720p-NEXT다운로드를 실행합니다.",
"기분 좋은 날.E3190.200423.720p-NEXT다운로드를 실행합니다.",
"생활의 달인.E734.200421.720p-NEXT다운로드를 실행합니다.",
"기분 좋은 날.E3188.200421.720p-NEXT다운로드를 실행합니다.",
"생활의 발견.E666.200414.720p-NEXT다운로드를 실행합니다.",
"기분 좋은 날.E3185.200414.720p-NEXT다운로드를 실행합니다.",
"기분 좋은 날.E3184.200413.720p-NEXT다운로드를 실행합니다.",
"그것이 알고 싶다.E1210.200411.720p-NEXT다운로드를 실행합니다.",
"생활의 달인.E729.200406.720p-NEXT다운로드를 실행합니다.",
"놀라운 토요일 도레미 마켓.E109.200523.720p-NEXT다운로드를 실행합니다.",
"놀라운 토요일 도레미 마켓.E104.200418.720p-NEXT다운로드를 실행합니다.",
"기분 좋은 날.E3212.200525.720p-NEXT다운로드를 실행합니다.",
"그것이 알고 싶다.E1215.200523.720p-NEXT다운로드를 실행합니다.",
"기분 좋은 날.E3207.200521.720p-NEXT다운로드를 실행합니다.",
"기분 좋은 날.E3209.200520.720p-NEXT다운로드를 실행합니다.",
"생활의 달인.E738.200505.720p-NEXT다운로드를 실행합니다.",
"놀라운 토요일 도레미 마켓.E94.200201.720p-NEXT다운로드를 실행합니다.",
"그것이 알고 싶다.E1211.200418.720p-NEXT다운로드를 실행합니다.",
"생활의 달인.E730.200407.720p-NEXT다운로드를 실행합니다.",
"기분 좋은 날.E3184.200407.720p-NEXT다운로드를 실행합니다.",
"그것이 알고 싶다.E1209.200404.720p-NEXT다운로드를 실행합니다.",
"기분 좋은 날.E3210.200526.720p-NEXT다운로드를 실행합니다.",
"생활의 발견.E677.200520.720p-NEXT다운로드를 실행합니다.",
"놀라운 토요일 도레미 마켓.E101.200321.1080p-NEXT다운로드를 실행합니다.",
"놀라운 토요일 도레미 마켓.E101.200321.1080p-NEXT다운로드를 실행합니다.",
"생활의 달인.E733.200420.720p-NEXT다운로드를 실행합니다.",
"기분 좋은 날.E3187.200417.720p-NEXT다운로드를 실행합니다.",
"기분 좋은 날.E3183.200410.720p-NEXT다운로드를 실행합니다."};



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