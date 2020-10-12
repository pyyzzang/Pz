# -*- coding: utf-8 -*- 

import os
from selenium import webdriver
from time import sleep
import requests
from bs4 import BeautifulSoup
import sys
import cfscrape
from requests import post
import time
import threading
import requests
import subprocess
from urllib import request



class TorrentParse():
    def __init__(self):
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
        return 3133
    
    def getUrl(self):
        pass

    def getUpdateQuery(self):
        pass
    
    def getBaseUrl(self):
        pass

    def getTitle(self,soup):
        pass
    def getMagnet(self,soup):
        pass
    def getTorrentFile(self,soup):
        pass

    def isRedirect(self, soup):
        script = soup.find("script")
        if(None == script):
            return ""
        if(None != script.string and "window.location.href =" in script.string):
            tmp1 = script.string.replace(" window.location.href =\"", "")
            tmp2 = tmp1.replace("\"", "")
            return tmp2
        return ""
    
    def getRedirectUrl(self, redirectUrl):
        return self.getBaseUrl() + redirectUrl

    def getUpdateList(self, param, genre, limitCount = sys.maxsize):
        index = 7065;
        url = self.getUrl()
        url = url % (param, index)
        print(url)
        scraper = cfscrape.create_scraper(delay=1000)
        response = scraper.get(url).content
        print(url)
        saveFilePath = "/home/pi/Pz/Test.html"
        f = open(saveFilePath, 'w')
        f.write(response.decode('utf-8'))
        f.close()

        soup = BeautifulSoup(response.decode('utf-8'), 'html.parser')
        redirectUrl = self.isRedirect(soup)        
        if("" != redirectUrl):
            url = self.getRedirectUrl(redirectUrl)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

        log = ""
        
        try:

            if( limitCount <= 0):
                return 
            limitCount = limitCount - 1
            magnet = self.getMagnet(soup)
            magnetFile = self.getTorrentFile(soup)  
            title = self.getTitle(soup)     

            

            saveFilePath = "/home/pi/Pz/HomePage/log/Tmp/%s_%s.html" % (param, index)
            f = open(saveFilePath, 'w')
            f.write(response.text)
            f.close()

            if("" == title and ("" == magnet or "" == magnetFile)):
                raise Exception("Title and Magnet Empty")

            
        except Exception as e:
            print(e)
        return log
    
    
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
            print(tag.text);
            if ("" != tag.text):
                retTitle = tag.text
                break
        return retTitle
    
    def getTorrentFile(self, soup):
        tag = soup.find("a", class_="btn btn-color btn-xs view_file_download")
        magnetUrl = tag.get("href")

        print(magnetUrl);

        saveFilePath = "/home/pi/Pz/Test.torrent"

        mem = request.urlopen(magnetUrl).read() 
        with open(saveFilePath, mode="wb") as f:
            f.write(mem) 
            print("저장되었습니다.")
        
        torrentUrl = "magnet-link " + "http://192.168.219.102:8080" + saveFilePath;
        magnetUrl = subprocess.check_output(torrentUrl, shell = True).decode("utf-8");
        Binary = magnetUrl.replace("\n", "");
        print("Binary : " + Binary);


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
        return "https://torrentdia.com"
    
    def getUrl(self):
        return self.getBaseUrl() + '/torrent_%s/%s'
    
    def getUpdateQuery(self):
        return "update meta set value='%s' where name='Very_%sindex'"

    @staticmethod
    def CrawlingTorrent():
        tvParse = TorrentveryParse()
        tvParse.getUpdateList("drama", 1)
        

import requests

mem = requests.get("https://torrentdia.com/bbs/download.php?bo_table=torrent_drama&wr_id=7065&no=0")
with open("saveFilePath", mode="wb") as f:
    f.write(mem.text.encode("utf-8")) 
    print("저장되었습니다.")

    
#TorrentveryParse.CrawlingTorrent();