#-*- coding:utf-8 -*-
from django.http import HttpResponse

from ..module.DBExecute import DBExecute;
from enum import Enum;
import datetime;
import base64;
import os;
import subprocess;
from ..module.osDefine import osDefine;
from ..module.DBExecute import SQLalchemy;
from ..module.HtmlUtil import HtmlUtil;


class RowEnum(Enum):
    Title = 0
    MagnetUrl = Title + 1;
    ModifyDate = MagnetUrl + 1;
    idx = ModifyDate + 1;

class TorrentData:
    def __init__(self, title, magnetUrl, modifyDate, idx):
        self.title = title;
        self.magnetUrl = magnetUrl;
        self.modifyDate = modifyDate;
        self.idx = idx;

    def getTitle(self):
        return self.title;
        
    def getModifyDate(self):
        return self.modifyDate.strftime("%Y년 %m월 %d일");
    def getMagnetUrl(self):
        return self.magnetUrl;
    def getIdx(self):
        return self.idx;
    def getStrIdx(self):
        return str(self.getIdx());

    def getAjaxScript(self):
        ret = "<script type=\"text/javascript\">$(function(){$(\"#AddRow"+self.getStrIdx()+"\").click(function(){$.ajax({type: 'post', data:{'magnetUrl' : '"+self.getMagnetUrl()+"'}, url: 'Torrent/TorrentAdd', dataType : 'html', error : function(){	alert();}, success : function(data){alert(\"토렌트 추가 하였습니다.\");}});})})</script>";
        return ret;

    def getHttpRow(self):
        ret = "<tr><td>" + self.getTitle() + "</td>";
        ret += "<td>" + self.getModifyDate() + "</td>";
        ret += "<td style='display:none'>" + self.getMagnetUrl() + "</td>";
        ret += "<td><input type=\"Button\" id=\"AddRow" + self.getStrIdx() + "\" Value=\"토렌트 추가\"></input></td>";
        ret += self.getAjaxScript();
        ret += "</tr>";
        return ret;
    
    @staticmethod
    def createTorrenData(row):
        retData = TorrentData(
        DBExecute.ConvetHangul(row[RowEnum.Title.value]),
        row[RowEnum.MagnetUrl.value],
        row[RowEnum.ModifyDate.value],
        row[RowEnum.idx.value]);
        return retData;

class torrent:
    @staticmethod
    def torrentAdd(request):
        magnetUrl = request.POST.get("magnetUrl");
        magnetUrl = osDefine.Base64Decoding(magnetUrl);
        addCmd = "sudo transmission-remote -a \"" + magnetUrl + "\" -n \"pi\":\"cndwn5069()\"";
        os.system(addCmd);
        return HttpResponse(addCmd);
    @staticmethod
    def torrentUpload(request):
        Title = request.POST.get("torrentTitle");
        magnet = request.POST.get("torrent_upload_url")

        osDefine.Logger("torrentUpload_magnet : " + magnet);

        try:
            tmpTorrentFile = "/home/pi/Pz/HomePage/app/static/Tmp/LastUpload.Torrent";
            fileBinary = request.FILES["torrent_files"];
            f = open(tmpTorrentFile, 'wb+');
            for chunk in fileBinary.chunks():
                f.write(chunk)
            f.close();
            
            torrentUrl = "magnet-link http://192.168.219.102:8000/static/Tmp/LastUpload.Torrent";
            magnetUrl = subprocess.check_output(torrentUrl, shell = True).decode("utf-8");
            Binary = magnetUrl.replace("\n", "");
            base64Magnet = osDefine.Base64Encoding(Binary);
            if( True == os.path.isfile(tmpTorrentFile)):
                os.system("sudo rm " + tmpTorrentFile);

        except Exception as ex:
            Binary = "";
        
        if "" == Binary:
            Binary = request.POST.get("torrent_upload_url", "");
            base64Magnet = osDefine.Base64Encoding(Binary);

        query = "insert into Torrent values('%s', '%s', GETDATE())" % (Title, base64Magnet);
        osDefine.Logger(query);
        session = DBExecute.GetDBConnection();
        session.InsertQueryExecute(query);
        return HttpResponse(query);

    @staticmethod 
    def getTorrentAddDiv():
        ret = "<div style=\"position: relative; left:0px; top: 0px;border:1px solid rgb(119,119,119); background-color: #FFFFF0\">";
        ret += "<div class=\"dialog_window\" id=\"dialog_Window\">";
        ret += "<div class=\"dialog_logo\" id=\"upload_dialog_logo\"></div>";
        ret += "<h2 class=\"dialog_heading\">Upload Torrent Files</h2>";
        ret += "<form action=\"/Torrent/Upload\" method=\"post\" id=\"torrent_upload_form\"";
        ret += "enctype=\"multipart/form-data\">";
        ret += "<div class=\"dialog_message\">";
        ret += "<label\">제목을 입력하세요(*) : </label>";
        ret += "<input type=\"TextBox\" name=\"torrentTitle\" id=\"torrentTitle\" autocomplete=\"off\"/>";
        ret += "<P><label for=\"torrent_upload_file\">Please select a torrent file to upload:</label>";
        ret += "<input type=\"file\" name=\"torrent_files\" id=\"torrent_files\" multiple=\"multiple\" />";
        ret += "<p><label for=\"torrent_upload_url\" >Or enter a URL:</label>";
        ret += "<input type=\"url\" name=\"torrent_upload_url\" id=\"torrent_upload_url\" autocomplete=\"off\"/>";
        ret +=  "</div>"
        ret += "<button id=\"upload_confirm_button\">Upload</button>";
        ret += "</form>"
        ret += "</div>"
        ret += "</div>"
        return ret;

    @staticmethod
    def getTableHead():
        retHttp  = '				<table id="TorrenViewTable">                                                         ';
        retHttp += '					<thead>                                                     ';
        retHttp += '						<tr class="table100-head">                              ';
        retHttp += '							<th class="column1">제목</th>                       ';
        retHttp += '							<th class="column2"></th>                           ';
        retHttp += '							<th class="column3"></th>                           ';
        retHttp += '						</tr>                                                   ';
        retHttp += '					</thead>                                                    ';
        retHttp += '                    <tbody>                                                     ';
        return retHttp;

    @staticmethod
    def getTorrent(request):
        ret = HtmlUtil.getHeader();
        ret += torrent.getTorrentAddDiv();

        ret += HtmlUtil.getBodyHead();
        ret += "<Table width:'100%' border='1'>";
        session = DBExecute.GetDBConnection();
        rows = session.QueryExecute("select title, MagnetUrl, modifyDate, idx from Torrent");
        ret += torrent.getTableHead();
        for row in rows:
            data = TorrentData.createTorrenData(row);
            ret += data.getHttpRow();
        ret += "</tbody></table>"
        ret += HtmlUtil.getBodyTail();
        ret += "</html>"

        
        return HttpResponse(ret);