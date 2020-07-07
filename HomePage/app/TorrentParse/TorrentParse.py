import os
from selenium import webdriver
from time import sleep
import requests
from ..module.osDefine import osDefine
from ..module.DBExecute import DBExecute
from ..Data.TorrentInfo import torrentInfo
from ..FCM.FCM import FCM
from bs4 import BeautifulSoup
from ..Data.TorrentInfo import torrentInfo
from ..Data.TorrentInfo import TorrentInfos
from ..subViews.torrent import torrent
import sys
from ..module.Task import Task
import cfscrape

class TorrentParse(Task):
    def __init__(self):
        Task.__init__(self)
        os.system("sudo killall -9 chromedriver")
        os.system("sudo killall -9 chromium-browse")

    def __del__(self):
        os.system("sudo killall -9 chromedriver")
        os.system("sudo killall -9 chromium-browse")

    def isEmpty(self):
        pass

    def getMetaQuery(self, genre):
        pass

    def reTryCount(self):
        return 2
    
    def isMP4(self, soup):
        pass

    def getMeta(self, param):
        connection = DBExecute.GetDBConnection()
        selectQuery = self.getMetaQuery(param)
        rows = connection.QueryExecute(selectQuery)
        listRow = list(rows)
        return str(listRow[0][0]).strip()
    
    def getUrl(self):
        pass

    def getUpdateQuery(self):
        pass
    
    def getBaseUrl(self):
        pass

    def getTitle(self, soup):
        pass
    def getMagnet(self, soup):
        pass
    def getTorrentFile(self, soup):
        pass

    def isRedirect(self, soup):
        script = soup.find("script")
        osDefine.Logger(script.string)
        if(None == script):
            return ""
        if(None != script.string and "window.location.href =" in script.string):
            tmp1 = script.string.replace(" window.location.href =\"", "")
            tmp2 = tmp1.replace("\"", "")
            return tmp2
        return ""
    
    def getRedirectUrl(self, redirectUrl):
        return self.getBaseUrl() + redirectUrl

    def updateTorrentIndex(self, index, metaName):
        connection = DBExecute.GetDBConnection()
        if(int(index) > 0):
            selectQuery = (self.getUpdateQuery() % (index, metaName))
            osDefine.Logger(selectQuery)
            rows = connection.InsertQueryExecute(selectQuery)
        return self.getMeta(metaName)

    def getUpdateList(self, param, genre, limitCount = sys.maxsize):
        index = int(self.getMeta("%s" % param))
        url = self.getUrl()
        url = url % (param, index)
        scraper = cfscrape.create_scraper()
        response = scraper.get(url)
        if(200 != response.status_code):
            osDefine.Logger("URL : + " + url + " response.status_code : " + str(response.status_code))
            osDefine.Logger("response.text : + " + response.text)
            return

        soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
        redirectUrl = self.isRedirect(soup)        
        osDefine.Logger(response.text)
        osDefine.Logger(redirectUrl)
        if("" != redirectUrl):
            osDefine.Logger("redirectUrl : " + redirectUrl)
            url = self.getRedirectUrl(redirectUrl)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

        insertMagnet = ""
        log = ""
        infos = TorrentInfos.GetTorrentInfos()
        reTryCount = self.reTryCount()
        while True:
            try:

                if( limitCount <= 0):
                    return 
                limitCount = limitCount - 1
                osDefine.Logger("url : " + url)
                magnet = self.getMagnet(soup)
                title = self.getTitle(soup)       

                saveFilePath = "/home/pi/Pz/HomePage/log/Tmp/%s_%s.html" % (param, index)
                f = open(saveFilePath, 'w')
                f.write(response.text)
                f.close()

                if("" == title and "" == magnet):
                    raise Exception("Title and Magnet Empty")

                osDefine.Logger("IsMp4 : " + str(self.isMP4(soup) ))

                if(True == self.isMP4(soup) 
                    and False == TorrentParse.existsEqualsTorrent(title, genre)):

                    osDefine.Logger("title : " + str(title))
                    osDefine.Logger("magnet : " + str(magnet))
                    
                    torrent.torrentInsert(None, title, magnet, genre)
                    #유사한 토렌트 파일인 경우 메시지 전달 및 다운로드 받도록 해야 함.
                    if(None != infos.findSimilarTorrintInfo(title)):
                        FCM.SendFireBase_Msg(msg = title + "다운로드를 실행합니다.", title ="다운로드 실행")
                        osDefine.Logger("Send FCM and Auto Add")
                        torrent.torrentRemoteAdd(magnet, title)

                reTryCount = self.reTryCount()
                self.updateTorrentIndex(index, param)

            except Exception as e:
                osDefine.Logger(e)
                reTryCount = reTryCount - 1
                if(0 >= reTryCount):
                    break
            finally:
                index = index + 1
                url = self.getUrl() % (param, index)
                response =scraper.get(url)
                if(200 != response.status_code):
                    return
                soup = BeautifulSoup(response.text, 'html.parser')

                redirectUrl = self.isRedirect(soup)        
                osDefine.Logger("redirectUrl : " + redirectUrl)
                if("" != redirectUrl):
                    osDefine.Logger(response.text)
                    url = self.getRedirectUrl(redirectUrl)
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
                    osDefine.Logger(response.text)
                
        return log
    
    @staticmethod
    def existsEqualsTorrent(title, genre):
        try:
            info = torrentInfo(title)
            session = DBExecute.GetDBConnection()
            updateQuery = "select Title from Torrent where genre='" + str(genre) + "' and title like '\%" + info.getEpisode() + "%' or title like '%" + info.getDate() + "%'"
            osDefine.Logger("UpdateQuery : " + updateQuery)
            rows = session.QueryExecute(updateQuery)
            for row in rows:
                dbTitle = row[0].strip()
                if(True == info.equals(torrentInfo(dbTitle))):
                    osDefine.Logger("Equals Row : " + dbTitle + " Title : " + title)
                    return True
        except Exception as e:
            osDefine.Logger(e)
        return False
