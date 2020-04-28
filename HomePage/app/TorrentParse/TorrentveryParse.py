from ..subViews.torrent import torrent;
from bs4 import BeautifulSoup
from .TorrentParse import TorrentParse;
from ..module.osDefine import osDefine;
from requests import post;

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
        while True:
            try:
                magnet = self.getMagnet(soup);
                title = self.getTitle(soup);
                torrentParam = {'torrentTitle': title, 'torrent_upload_url': magnet};
                torrent.torrentInsert(None, title, magnet, genre);

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
    def CrawlingTorrent(param):
        osDefine.Logger(param);
        pa = TorrentveryParse();
        pa.getUpdateList("movieko", 1);
        pa.getUpdateList("drama", 2);
        pa.getUpdateList("ent", 3);
        pa.getUpdateList("docu", 4);
        pa.getUpdateList("tvend", 5);
        return "";
            
