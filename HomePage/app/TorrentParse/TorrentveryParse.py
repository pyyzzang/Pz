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
from ..FCM.FCM import FCM;

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

    def isMp4File(self, soup):
        retExt = "";
        for extValue in soup.find_all("div", class_="text-muted panel-heading3 tpanel-heading3 moreless"):
            for subDiv in extValue.find_all("div"):
                if(-1 < subDiv.text.find("mp4")):
                    return True;
        return False; 

    retryValue = 5;
    def getUpdateList(self, param, genre):
        index = int(torrent.getMeta("%s" % param));
        url = 'https://torrentvery.com/torrent_%s/%s' %(param, index);
        response = requests.get(url);
        soup = BeautifulSoup(response.text, 'html.parser')
        insertMagnet = "";
        log = "";
        infos = TorrentInfos.GetTorrentInfos();
        reTryCount = TorrentveryParse.retryValue;
        while True:
            try:
                osDefine.Logger("url : " + url);
                magnet = self.getMagnet(soup);
                title = self.getTitle(soup);              
                if(True == self.isMp4File(soup) 
                    and False == TorrentParse.existsEqualsTorrent(title, genre)):
                    torrent.torrentInsert(None, title, magnet, genre);
                    #유사한 토렌트 파일인 경우 메시지 전달 및 다운로드 받도록 해야 함.
                    if(None != infos.findSimilarTorrintInfo(title)):
                        FCM.SendFireBase(msg = title + "다운로드를 실행합니다.", title ="다운로드 실행");
                        osDefine.Logger("Send FCM and Auto Add");
                        torrent.torrentRemoteAdd(magnet, title);

                TorrentveryParse.retryValue = 20;
                torrent.updateTorrentIndex(index, param);

            except Exception as e:
                osDefine.Logger(e);
                reTryCount = reTryCount - 1;
                if 0 == reTryCount:
                    TorrentveryParse.retryValue = TorrentveryParse.retryValue * 2;
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

        while(True):
            tvParse = TorrentveryParse();
            tvParse.getUpdateList("movieko", 1);
            tvParse.getUpdateList("drama", 2);
            tvParse.getUpdateList("ent", 3);
            tvParse.getUpdateList("docu", 4);
            tvParse.getUpdateList("tvend", 5);
            time.sleep(60 * 3);
            osDefine.YoutubeTokenRefresh();
            FCM.SendFireBaseThread();
            
        return "";
    
    @staticmethod
    def RunCrawlingThread():
        #if(True == osDefine.getIsDev()):
        if(False):
            osDefine.Logger("개발 모드");
        else:
            t = threading.Thread(target=TorrentveryParse.CrawlingTorrent);
            t.start();
        
TorrentveryParse.RunCrawlingThread();

