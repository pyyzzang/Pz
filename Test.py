import os;
from threading import Lock;
import json;
from difflib import SequenceMatcher

import os
import re

import pyodbc;

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer;
from sqlalchemy.orm import sessionmaker

class DBExecute():
    PYODBC = 0
    SQLALCHEMY = 1

    dbConnection="";
    dbMode = SQLALCHEMY;

    def InsertQueryExecute(self, query):
        pass
    def QueryExecute(self, query):
        pass

    @staticmethod 
    def ConvetHangul(encodeStr):
        if(DBExecute.SQLALCHEMY == DBExecute.dbMode):
            return encodeStr;

        encodeStr = encodeStr;
        encodeStr = encodeStr.encode('ISO-8859-1')
        return encodeStr.decode('euc-kr');

    @staticmethod
    def GetDBConnection(db = SQLALCHEMY):
        if("" != DBExecute.dbConnection):
            return DBExecute.dbConnection;

        DBExecute.dbMode = db;
        if( DBExecute.PYODBC == db):
            DBExecute.dbConnection = PyODBC();
        elif(DBExecute.SQLALCHEMY == db):
            DBExecute.dbConnection = SQLalchemy();
        return DBExecute.dbConnection;

class SQLalchemy(DBExecute):
    def __init__(self):
        self.engine = create_engine('mssql+pyodbc:///?odbc_connect=' + 'DRIVER%3D%7BFreeTDS%7D%3BSERVER%3Dpyyzzang.database.windows.net%3BPORT%3D1433%3BDATABASE%3DRaspberryPi%3BUID%3Dpyyzzang%3BPWD%3Dcndwn5069%28%29%3BTDS_Version%3D7.4%3B', pool_size=20, pool_recycle=500, max_overflow=5);

    def InsertQueryExecute(self, query):
        Session = sessionmaker(bind=self.engine)
        session = Session();
        session.execute(query);
        session.commit();
        
    def QueryExecute(self, query):
        Session = sessionmaker(bind=self.engine)
        session = Session();
        return session.execute(query);

class PyODBC(DBExecute):
    def InsertQueryExecute(self, query):
        server ="pyyzzang.database.windows.net";
        database = "RaspberryPi";
        username = "pyyzzang";
        password = "cndwn5069()";
        driver = "{FreeTDS}";
        connectString = "DRIVER="+driver+";SERVER="+server+";PORT=1433;DATABASE="+database + ";UID="+username+";PWD="+ password + ";Encrypt=yes;Connection Timeout=30;TDS_Version=7.0";
        cnxn = pyodbc.connect(connectString);
        cursor = cnxn.cursor();
        cursor.execute(query);
        cnxn.commit();
        cnxn.close();

    def QueryExecute(self, query):
        server ="pyyzzang.database.windows.net";
        database = "RaspberryPi";
        username = "pyyzzang";
        password = "cndwn5069()";
        driver = "{FreeTDS}";
        connectString = "DRIVER="+driver+";SERVER="+server+";PORT=1433;DATABASE="+database + ";UID="+username+";PWD="+ password + ";Encrypt=yes;Connection Timeout=30;TDS_Version=7.0";
        cnxn = pyodbc.connect(connectString);
        cursor = cnxn.cursor();
        cursor.execute(query);
        rows = cursor.fetchall();
        return rows; 

import os;
if '/home/pi/Pz/HomePage' != os.getcwd() : 
    DBExecute.GetDBConnection();



class strUtil:
    tvPattern = 0
    movePattern = 0

    @staticmethod
    def init():
        strUtil.titlePattern = '.+.E\d+'
        strUtil.similarTitlePattern = "[ ㄱ-ㅣ가-힣]+";

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
    def getSimilarTitle(title):
        strUtil.init()
        fileName = os.path.split(title)[1]
        result = strUtil.getRegulaString(fileName, strUtil.similarTitlePattern)
        length = len(result)
        if(0 != length):
            return result[0]
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
    def __init__(self, fullName = "", title = "", season = "", episode = "", date = "", count = 1, similarTitle=""):
        self.fullName = fullName;
        self.title = strUtil.getMatchTitle(self.fullName);
        self.similarTitle = strUtil.getSimilarTitle(self.fullName);
        self.season  = strUtil.getSeason(self.fullName);
        self.episode = strUtil.getEpisode(self.fullName);
        self.date = strUtil.getDate(self.fullName);
        self.count = 1;
        self.titleValue = 0;
    
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
    
    def getSimilar(self, compareInfo, v):
        titleValue = SequenceMatcher(None, self.getSimilarTitle(), compareInfo.getSimilarTitle()).ratio();
        self.titleValue = titleValue;
        if(v < titleValue):
            print(self.getSimilarTitle() + " : " + str(titleValue));
            print(self.getTitle());
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
    DataPath = "/home/pi/Pz/HomePage/Data/";
    TorrentInfoFile = "/home/pi/Pz/HomePage/Data/TorrentInfo";

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
            if(True == info.getSimilar(addInfo)):
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

def Compare(s1, s2):
    t1 = strUtil.getMatchTitle(s1);
    t2 = strUtil.getMatchTitle(s2);
    print("t1 : " + t1);
    print("t2 : " + t2);
    titleValue = SequenceMatcher(None, t1, t2).ratio();
    print(titleValue);
'''
result = strUtil.getRegulaString("여자 하숙집 3 2019.HDRip.720p.H264.AAC-STY", );
print(result);

Compare("여자 하숙집 3 2019.HDRip.720p.H264.AAC-STY", "충격! 돌려먹기 2019.HDRip.720p.H264.AAC-STY.mp4");
Compare("여자 하숙집 3 2019.HDRip.720p.H264.AAC-STY", "어린 처형 2.2019.HDRip.1080p.H264.AAC-STY.mp4");
Compare("여자 하숙집 3 2019.HDRip.720p.H264.AAC-STY", "정사 : 결혼 말고 연애 2016.HDRip.720p.H264.AAC-STY.mp4");
Compare("유부녀들-남편바꾸기 2019.1080p.HDRip-mov19.mp4", "엄마와 딸 2019.1080p.HDRip-mov19.mp4");
Compare("유부녀들-남편바꾸기 2019.1080p.HDRip-mov19.mp4", "식모-아내의 친구 2019.1080p.HDRip-mov19.mp4");
Compare("해적 : 바다로 간 산적 Pirates.2014.1080p.BluRay.x264.AAC5.1-[YTS.MX]", "오직 그대만 Always.2011.1080p.BluRay.x264.AAC5.1-[YTS.MX]");
Compare("해적 : 바다로 간 산적 Pirates.2014.1080p.BluRay.x264.AAC5.1-[YTS.MX]", "국가부도의 날 Default.2018.1080p.BluRay.x264.AAC5.1-[YTS.MX]");

info = torrentInfo("삼시");
connection = DBExecute.GetDBConnection();
rows = connection.QueryExecute("select * from Torrent");
for row in rows:
    torrentInfo(row[0].strip()).getSimilar(info, 0.3);
#    if True == torrentInfo(row[0].strip()).getSimilar(info, 0.3):
#        print(info.getTitle() + " : " + row[0].strip() + " : " + str(info.titleValue));

findTitle = "aaaa";
q = "select title, MagnetUrl, modifyDate, idx from Torrent where title like '%" + findTitle + "%');"
print(q);
'''

import smtplib
from email.mime.text import MIMEText
import os, threading
import time;
while(True):
    temp = os.popen("vcgencmd measure_temp").readline()
    result = temp.replace("temp=","").replace("'C", "")
    print(result);
    time.sleep(1);
