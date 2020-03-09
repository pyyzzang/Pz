from django.http import HttpResponse

from ..module.auzerConnect import Auzer;
from enum import Enum;
import datetime
import base64

class RowEnum(Enum):
    Title = 0
    AlisaTitle = Title + 1;
    MagnetUrl = AlisaTitle + 1;
    ModifyDate = MagnetUrl + 1;
    idx = ModifyDate + 1;

class TorrentData:
    def __init__(self, title, aliasTitle, modifyDate):
        self.title = title;
        self.aliasTitle = aliasTitle;
        self.modifyDate = modifyDate;
        self.magnetUrl = "";

    def getTitle(self):
        if(0 == len(self.aliasTitle.strip())):
            return self.title;
        return self.aliasTitle;
    def getModifyDate(self):
        return self.modifyDate.strftime("%Y년 %m월 %d일");
    def getMagnetUrl(self):
        return self.magnetUrl;

    def getHttpRow(self):
        ret = "<td>" + self.getTitle() + "</td>";
        ret += "<td>" + self.getModifyDate() + "</td>";
        return ret;
    
    @staticmethod
    def createTorrenData(row):
        retData = TorrentData(
        Auzer.ConvetHangul(row[RowEnum.Title.value]),
        Auzer.ConvetHangul(row[RowEnum.AlisaTitle.value]),
        row[RowEnum.ModifyDate.value]);
        return retData;

class torrent:
    @staticmethod
    def torrentUpload(request):
        Title = request.POST.get("torrentTitle");

        try:
            fileBinary = request.FILES["torrent_files"];
            
            Binary= ""
        except :
            Binary = "";
        
        if "" == Binary:
            Binary = request.POST.get("torrent_upload_url", "");
        
        query = "insert into Torrent values('%s', ' ', '%s', GETDATE(), 6)" % (Title, Binary);
        #query= "insert into Torrent values('1111', ' ', '11', GETDATE(), 7)";
        Auzer.InsertQueryExecute(query);
        return HttpResponse(query);

    @staticmethod
    def getTorrent(request):
        ret = "<script type=\"text/javascript\" src=\"/static/app/scripts/Torrent.js\"></script>";
        ret += "<div style=\"position: relative;\">";
        ret += "<Table><tr>";

#        rows = Auzer.QueryExecute("select title, AliasTitle, '', modifyDate from Torrent");
#        for row in rows:
#            data = TorrentData.createTorrenData(row);
#            ret += data.getHttpRow();

        ret += "</tr></table>"
        ret += "</div>"

        ret += "<div style=\"position: relative; left:0px; top: 0px;border:1px solid rgb(119,119,119); background-color: #FFFFF0\">";
        ret += "<div class=\"dialog_window\" id=\"dialog_Window\">";
        ret += "<div class=\"dialog_logo\" id=\"upload_dialog_logo\"></div>";
        ret += "<h2 class=\"dialog_heading\">Upload Torrent Files</h2>";
        ret += "<form action=\"/Torrent/Upload\" method=\"post\" id=\"torrent_upload_form\"";
        ret += "enctype=\"multipart/form-data\" target=\"torrent_upload_frame\">";
        ret += "<div class=\"dialog_message\">";
        ret += "<label\">제목을 입력하세요(*) : </label>";
        ret += "<input type=\"TextBox\" name=\"torrentTitle\" id=\"torrentTitle\"/>";
        ret += "<P><label for=\"torrent_upload_file\">Please select a torrent file to upload:</label>";
        ret += "<input type=\"file\" name=\"torrent_files\" id=\"torrent_upload_file\" multiple=\"multiple\" />";
        ret += "<p><label for=\"torrent_upload_url\">Or enter a URL:</label>";
        ret += "<input type=\"url\" name=\"torrent_upload_url\" id=\"torrent_upload_url\"/>";
        ret +=  "</div>"
        ret += "<button id=\"upload_confirm_button\">Upload</button>";
        ret += "</form>"
        ret += "</div>"
        ret += "</div>"
        return HttpResponse(ret);