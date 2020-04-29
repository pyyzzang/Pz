from ..subViews.torrent import torrent;
from bs4 import BeautifulSoup
from .TorrentParse import TorrentParse;
from ..module.osDefine import osDefine;
from requests import post;
from ..Data.TorrentInfo import torrentInfo;
from ..Data.TorrentInfo import TorrentInfos;
import time;
import threading;

class TorrentveryParse(TorrentParse):
    def __init__(self):
        TorrentParse.__init__(self);

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
        self.browser.get(url);
        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        insertMagnet = "";
        log = "";
        infos = TorrentInfos.GetTorrentInfos();
        while True:
            try:
                magnet = self.getMagnet(soup);
                title = self.getTitle(soup);
                
                if(None == FindEqualsTorrentInfo(title)):
                    osDefine.Logger("url : " + url);
                    torrent.torrentInsert(None, title, magnet, genre);

                    if(None != infos.findSimilarTorrintInfo(title)):
                        osDefine.Logger("Send FCM and Auto Add");
                
                index = index + 1;
                url = 'https://torrentvery.com/torrent_%s/%s' % (param, index);
                self.browser.get(url);
                soup = BeautifulSoup(self.browser.page_source, 'html.parser');
                torrent.updateTorrentIndex(index, param);

            except Exception as e:
                #osDefine.Logger(e);
                break;

        return log;
    
    @staticmethod
    def CrawlingTorrent(param = ""):
        
        osDefine.Logger("Start Craling");
        '''
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
        
#TorrentveryParse.RunCrawlingThread();            

