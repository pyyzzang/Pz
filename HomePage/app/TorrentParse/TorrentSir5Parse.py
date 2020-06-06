import os
from selenium import webdriver
from time import sleep
import requests
from ..module.osDefine import osDefine
from ..module.DBExecute import DBExecute
from ..Data.TorrentInfo import torrentInfo
from .TorrentParse import TorrentParse
import threading
import time
from ..module.Task import Task

class TorrentSir5Parse(TorrentParse):
    def __init__(self):
        TorrentParse.__init__(self)
    
    def __del__(self):
        TorrentParse.__del__(self)
    
    def getMagnet(self,soup):
        retMagnet = ""
        for magnetUrl in soup.find_all("a"):
            if None != magnetUrl.get("href") and True == magnetUrl.get("href").startswith("magnet:?"):
                return magnetUrl.get("href")
        return retMagnet
    def getTitle(self,soup):
        for title in soup.find_all("title"):
            return title.text
    
    def isMP4(self, soup):
        for title in soup.find_all("h3", class_="panel-title"):
            return True
        return True
    
    def getMetaQuery(self, param):
        selectQuery = "select value from meta where name='Ts_%sindex'" % param
        return selectQuery

    def getUrl(self):
        return 'https://torrentsir5.com/bbs/board.php?bo_table=%s&wr_id=%s'

    def getUpdateQuery(self):
        return "update meta set value='%s' where name='Ts_%sindex'"
    
    def getBaseUrl(self):
        return "https://torrentsir5.com"

    def Run(self):
        #tsParse.getUpdateList("movie", 1)
        self.getUpdateList("drama", 2)
        self.getUpdateList("entertain", 3)
        self.getUpdateList("tv", 4)

Task.AppendTask(TorrentSir5Parse());