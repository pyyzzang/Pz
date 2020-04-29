import os;
from selenium import webdriver
from time import sleep
import requests
from ..module.osDefine import osDefine;
from ..module.DBExecute import DBExecute;
from ..Data.TorrentInfo import torrentInfo;

class TorrentParse:
    def __init__(self):
        os.system("sudo killall -9 /usr/lib/chromium-browser/chromium-browser-v7");
        os.system("sudo killall -9 chromedriver");
        os.system("sudo killall -9 chromium-browse")

    def __del__(self):
        os.system("sudo killall -9 /usr/lib/chromium-browser/chromium-browser-v7");
        os.system("sudo killall -9 chromedriver");
        os.system("sudo killall -9 chromium-browse")

    def isEmpty(self):
        pass;
    def getUpdateList(self):
        pass;
    
    @staticmethod
    def existsEqualsTorrent(title):
        try:
            info = torrentInfo(title);
            session = DBExecute.GetDBConnection();
            updateQuery = "select Title from Torrent where title like '\%" + info.getEpisode() + "%' or title like '%" + info.getDate() + "%'"
            osDefine.Logger("UpdateQuery : " + updateQuery);
            rows = session.QueryExecute(updateQuery);
            for row in rows:
                dbTitle = row[0].strip();
                if(True == info.equals(torrentInfo(dbTitle))):
                    osDefine.Logger("Equals Row : " + dbTitle + " Title : " + title);
                    return True
        except Exception as e:
            osDefine.Logger(e);
        return False;
