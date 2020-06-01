from .TorrentParse import TorrentParse
from ..module.osDefine import osDefine
from requests import post
import time
import threading
import requests
from .TorrentSir5Parse import TorrentSir5Parse



class TorrentveryParse(TorrentParse):
    def __init__(self):
        TorrentParse.__init__(self)
    
    def __del__(self):
        TorrentParse.__del__(self)

    def getMagnet(self, soup):
        retMagnet = ""
        for magnetUrl in soup.find_all("a", class_="btn btn-color btn-xs view_file_download"):
            if True == magnetUrl.get("href").startswith("magnet:?"):
                retMagnet = magnetUrl.get("href")
                break
        return retMagnet 

    def getTitle(self, soup):
        retTitle = ""
        title = soup.find('div', class_="view-wrap view-wrap-title")
        for tag in title.find_all("h1"):
            if ("" != tag.text):
                retTitle = tag.text
                break
        return retTitle

    def isMp4File(self, soup):
        for extValue in soup.find_all("div", class_="text-muted panel-heading3 tpanel-heading3 moreless"):
            for subDiv in extValue.find_all("div"):
                if(-1 < subDiv.text.find("mp4")):
                    return True
        return False 
    
    def getMetaQuery(self, genre):
        selectQuery = "select value from meta where name='Very_%sindex'" % genre
        return selectQuery

    def getBaseUrl(self):
        return "https://torrentvery2.com"
    
    def getUrl(self):
        return 'https://torrentvery2.com/torrent_%s/%s'
    
    def getUpdateQuery(self):
        return "update meta set value='%s' where name='Very_%sindex'"

    @staticmethod
    def CrawlingTorrent():
        TorrentParse.CrawlingTorrent()
        
        tvParse = TorrentveryParse()
        tvParse.getUpdateList("movieko", 1)
        tvParse.getUpdateList("drama", 2)
        tvParse.getUpdateList("ent", 3)
        tvParse.getUpdateList("docu", 4)
        tvParse.getUpdateList("tvend", 5)
        osDefine.YoutubeTokenRefresh()
    
    @staticmethod
    def RunCrawlingThread():
        if(True == osDefine.getIsDev()):
            osDefine.Logger("개발 모드")
        else:
            osDefine.Logger("크롤링 TorrentVery 모드")
            #TorrentveryParse.CrawlingTorrent()
        
#TorrentSir5Parse.RunCrawlingThread()