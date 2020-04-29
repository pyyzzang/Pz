from ..subViews.torrent import torrent;
from bs4 import BeautifulSoup
from .TorrentParse import TorrentParse;
from ..module.osDefine import osDefine;
from requests import post;
from ..Data.TorrentInfo import torrentInfo;
from ..Data.TorrentInfo import TorrentInfos;
import time;
import threading;
import requests;

class TorrentveryParse(TorrentParse):
    def __init__(self):
        TorrentParse.__init__(self);
    
    def __del__(self):
        TorrentParse.__del__(self);

    def getMagnet(self, soup):
        retMagnet = "";
        for magnetUrl in soup.find_all("a", class_="btn btn-color btn-xs view_file_download"):
            if True == magnetUrl.get("href").startswith("magnet:?"):
                retMagnet = magnetUrl.get("href");
                break;
        return retMagnet; 

    def getTitle(self, soup):
        retTitle = "";
        title = soup.find('div', class_="view-wrap view-wrap-title");
        for tag in title.find_all("h1"):
            if ("" != tag.text):
                retTitle = tag.text;
                break;
        return retTitle;

    def getUpdateList(self, param, genre):
        index = int(torrent.getMeta("%s" % param));
        url = 'https://torrentvery.com/torrent_%s/%s' %(param, index);
        response = requests.get(url);
        soup = BeautifulSoup(response.text, 'html.parser')
        insertMagnet = "";
        log = "";
        infos = TorrentInfos.GetTorrentInfos();
        reTryCount = 30;
        while True:
            try:
                osDefine.Logger("url : " + url);
                magnet = self.getMagnet(soup);
                title = self.getTitle(soup);              
                if(False == TorrentParse.existsEqualsTorrent(title)):
                    torrent.torrentInsert(None, title, magnet, genre);
                    #유사한 토렌트 파일인 경우 메시지 전달 및 다운로드 받도록 해야 함.
                    if(None != infos.findSimilarTorrintInfo(title)):
                        osDefine.Logger("Send FCM and Auto Add");

                
                reTryCount = 30;
                torrent.updateTorrentIndex(index, param);

            except Exception as e:
                osDefine.Logger(e);
                reTryCount = reTryCount - 1;
                if 0 == reTryCount:
                    break;
            finally:
                index = index + 1;
                url = 'https://torrentvery.com/torrent_%s/%s' % (param, index);
                response = requests.get(url);
                soup = BeautifulSoup(response.text, 'html.parser');
                
        return log;
    
    @staticmethod
    def CrawlingTorrent(param = ""):
        
        osDefine.Logger("Start Craling");
        '''
        while(True):
            try:
                tvParse = TorrentveryParse();
                tvParse.getUpdateList("ent", 3);
                
            except Exception as e:
                osDefine.Logger(e);
            finally : 
                time.sleep(30 * 1);
        
        
        while(True):
            time.sleep(60 * 5);
            tvParse = TorrentveryParse();
            tvParse.getUpdateList("movieko", 1);
            tvParse.getUpdateList("drama", 2);
            tvParse.getUpdateList("ent", 3);
            tvParse.getUpdateList("docu", 4);
            tvParse.getUpdateList("tvend", 5);
        '''
        return "";
    
    @staticmethod
    def RunCrawlingThread():
        t = threading.Thread(target=TorrentveryParse.CrawlingTorrent);
        t.start();
        
TorrentveryParse.RunCrawlingThread();            

