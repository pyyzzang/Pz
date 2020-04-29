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
        return strUtil.getRegularText(text, "S\d\d");

    @staticmethod
    def getEpisode(text):
        return strUtil.getRegularText(text, "E\d{2,6}");
    
    @staticmethod
    def getDate(text):
        return strUtil.getRegularText(text, "['\.',' ']\d{4,6}\.");