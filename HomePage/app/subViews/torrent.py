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
from ..FCM.FCM import FCM;
from urllib.parse import unquote
from datetime import datetime


class RowEnum(Enum):
    Title = 0
    MagnetUrl = Title + 1;
    ModifyDate = MagnetUrl + 1;
    idx = ModifyDate + 1;
    ThumbnailImage = idx + 1;

class TorrentData:
    def __init__(self, title, magnetUrl, modifyDate, idx):
        self.title = title;
        self.magnetUrl = magnetUrl.strip();
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
        ret += "<script type=\"text/javascript\">$(function(){$(\"#Delete"+self.getStrIdx()+"\").click(function(){$.ajax({type: 'post', data:{'magnetUrl' : '"+self.getMagnetUrl()+"'}, url: 'Torrent/TorrentDelete', dataType : 'html', error : function(){	alert();}, success : function(data){alert(\"토렌트 삭제 하였습니다.\"); document.getElementById('TR_" +self.getMagnetUrl() + "').style.display = \"none\";}});})})</script>";
        return ret;

    def getHttpScript(self):

        focusFunc = "FocusOut" + self.getMagnetUrl();
        ret = "<script>";
        ret += "function " +focusFunc + "(){";
        ret += "$.ajax({";
        ret += "type: 'post', "
        ret += "data:{"
        ret += "'magnetUrl' : '"+ self.getMagnetUrl() + "',";
        ret += "'Title' : document.getElementById('" +self.getMagnetUrl() + "').textContent},";
        ret += "url: 'Torrent/TorrentUpdate',";
        ret += "dataType : 'html',"
        ret += "error : function(){},";
        ret += "success : function(data){}";
        ret += "});}";
        ret += "</script>";


        
        ret += "<script>";
        ret += "$(function(){$(\"#" + self.getMagnetUrl() + "\").dblclick(function(){";
        ret += "var pPanel = document.getElementById(\"" + self.getMagnetUrl() + "\");";
        ret += "pPanel.contentEditable = true;";
        ret += "pPanel.removeEventListener('focusout', " + focusFunc + ");";
        ret += "pPanel.addEventListener('focusout', " + focusFunc + ");";
        ret += "})})";
        ret += "</script>";

        return ret;

    def getHttpRow(self):
        ret = "<tr  Id=\"TR_" + self.getMagnetUrl() + "\"><td><p Id=\"" + self.getMagnetUrl() + "\">" + self.getTitle() + "<p></td>";
        ret += "<td>" + self.getModifyDate() + "</td>";
        ret += "<td style='display:none'>" + self.getMagnetUrl() + "</td>";
        ret += "<td><panel >";
        ret += "<input id=\"AddRow" + self.getStrIdx() + "\" type=\"Button\" Value=\"토렌트 추가\"></input>";
        ret += "<input id=\"Delete" + self.getStrIdx() + "\"type=\"Button\" Value=\"토렌트 삭제\"></input>";
        ret += "</panel></td>";        
        ret += self.getAjaxScript();
        ret += "</tr>";
        ret += self.getHttpScript();
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
        try:
            magnetUrl = request.POST.get("magnetUrl").strip();
            osDefine.Logger("MagnetUrl : " + magnetUrl);
            magnetUrl = osDefine.Base64Decoding(magnetUrl);
            osDefine.Logger("MagnetUrl : " + magnetUrl);
            currentTime = datetime.now();
            addCmd = "sudo transmission-remote -a \"" + magnetUrl + "\" -n \"pi\":\"cndwn5069()\" -s";
            if (10 < currentTime.hour and currentTime.hour < 24):
                addCmd = "sudo transmission-remote -a \"" + magnetUrl + "\" -n \"pi\":\"cndwn5069()\" -S";
            osDefine.Logger("ExecuteCommand" + addCmd);
            os.system(addCmd);
        except Exception as e:
            osDefine.Logger(e);
        return HttpResponse(addCmd);
    @staticmethod
    def TorrentDelete(request):
        osDefine.Logger("TorrentDelete(+)");
        magnetUrl = request.POST.get("magnetUrl").strip();
        #magnetUrl = osDefine.Base64Decoding(magnetUrl);
        osDefine.Logger("MagnetUrl : " + magnetUrl);
        connection = DBExecute.GetDBConnection();
        deleteQuery = ("delete from Torrent where magnetUrl='%s'" % magnetUrl);
        osDefine.Logger("Delete Query : " + deleteQuery);
        connection.InsertQueryExecute(deleteQuery);
        return HttpResponse("");
    @staticmethod
    def torrentInsert(request, title, magnet, genre = 99):
        try:
            tmpTorrentFile = os.path.join(osDefine.getRunDir(), "HomePage/app/static/Tmp/LastUpload.Torrent");
            osDefine.Logger("TempFilePath : " + tmpTorrentFile);
            fileBinary = request.FILES["torrent_files"];
            f = open(tmpTorrentFile, 'wb+');
            for chunk in fileBinary.chunks():
                f.write(chunk)
            f.close();
            
            torrentUrl = "magnet-link " + osDefine.getRunIp(request) + "/static/Tmp/LastUpload.Torrent";
            magnetUrl = subprocess.check_output(torrentUrl, shell = True).decode("utf-8");
            Binary = magnetUrl.replace("\n", "");
            base64Magnet = osDefine.Base64Encoding(Binary);
            if( True == os.path.isfile(tmpTorrentFile)):
                os.system("sudo rm " + tmpTorrentFile);

        except Exception as ex:
            Binary = "";
        
        if "" == Binary:
            Binary = magnet;
            base64Magnet = osDefine.Base64Encoding(Binary);
        
        session = DBExecute.GetDBConnection();
        query = "select * from Torrent where magnetUrl='%s'" % (base64Magnet);
        osDefine.Logger("selectQuery : " + query);
        rows = session.QueryExecute(query);
        row = rows.fetchone();
        if None != row:
            osDefine.Logger("rows.cursor.arraysize : " + str(rows.cursor.arraysize));
            osDefine.Logger("Equals Torrent Exists " + row[0]);
            return HttpResponse("<script> location.href='" + osDefine.getRunIp(request) + "/Torrent'</script>");

        query = "insert into Torrent (Title, MagnetUrl, modifyDate, ThumbnailImage, genre) values ('%s', '%s', GETDATE(), '', %s)" % (title, base64Magnet, genre);
        osDefine.Logger("Torrent : " + query);
        
        session.InsertQueryExecute(query);
        return HttpResponse("<script> location.href='" + osDefine.getRunIp(request) + "/Torrent'</script>");

    @staticmethod
    def torrentUpload(request):
        Title = request.POST.get("torrentTitle");
        magnet = request.POST.get("torrent_upload_url")

        osDefine.Logger("torrentUpload_magnet : " + magnet);
        return torrent.torrentInsert(request, title=Title, magnet=magnet);

        

    @staticmethod 
    def getTorrentAddDiv():
        retHttp  = "<input type='button' value='Torrent 페이지로' onclick='MoveTorrentPage();'></input><p>";
        retHttp += "<script>function MoveTorrentPage(){ location.href = '/Home';}</script>"
        retHttp += "<div style=\"position: relative; left:0px; top: 0px;border:1px solid rgb(119,119,119); background-color: #FFFFF0\">";
        retHttp += "<div class=\"dialog_window\" id=\"dialog_Window\">";
        retHttp += "<div class=\"dialog_logo\" id=\"upload_dialog_logo\"></div>";
        retHttp += "<h2 class=\"dialog_heading\">Upload Torrent Files</h2>";
        retHttp += "<form action=\"/Torrent/Upload\" method=\"post\" id=\"torrent_upload_form\"";
        retHttp += "enctype=\"multipart/form-data\">";
        retHttp += "<div class=\"dialog_message\">";
        retHttp += "<label\">제목을 입력하세요(*) : </label>";
        retHttp += "<input type=\"TextBox\" name=\"torrentTitle\" id=\"torrentTitle\" autocomplete=\"off\"/>";
        retHttp += "<P><label for=\"torrent_upload_file\">Please select a torrent file to upload:</label>";
        retHttp += "<input type=\"file\" name=\"torrent_files\" id=\"torrent_files\" multiple=\"multiple\" />";
        retHttp += "<p><label for=\"torrent_upload_url\" >Or enter a URL:</label>";
        retHttp += "<input type=\"url\" name=\"torrent_upload_url\" id=\"torrent_upload_url\" autocomplete=\"off\"/>";
        retHttp +=  "</div>"
        retHttp += "<button id=\"upload_confirm_button\">Upload</button>";
        retHttp += "</form>"
        retHttp += "</div>"
        retHttp += "</div>"
        return retHttp;

    @staticmethod
    def getTableHead():
        retHttp  = '				<table class="ListView">                                                         ';
        retHttp += '					<thead>                                                     ';
        retHttp += '						<tr class="table100-head">                              ';
        retHttp += '							<th class="column_Title">제목</th>                       ';
        retHttp += '							<th class="column_Date"></th>                           ';
        retHttp += '							<th class="column_Add"></th>                           ';
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
        rows = session.QueryExecute("select title, MagnetUrl, modifyDate, idx from Torrent  order by modifyDate desc");
        ret += torrent.getTableHead();
        for row in rows:
            data = TorrentData.createTorrenData(row);
            ret += data.getHttpRow();
        ret += "</tbody></table>"
        ret += HtmlUtil.getBodyTail();
        ret += "</html>"

        
        return HttpResponse(ret);

    @staticmethod
    def torrentUpdate(request):
        magnetUrl = request.POST.get("magnetUrl");
        title = request.POST.get("Title");

        osDefine.Logger("magnetUrl : " + magnetUrl);
        osDefine.Logger("title : " + title);

        session = DBExecute.GetDBConnection();
        updateQuery = "update Torrent set title='" + title + "' where magnetUrl='" + magnetUrl +"'";
        osDefine.Logger("UpdateQuery : " + updateQuery);
        session.InsertQueryExecute(updateQuery);
        return HttpResponse("");

    @staticmethod
    def MakeFile(fileName, name, baseUsMagnetUrl):
        
        dbConnection = DBExecute.GetDBConnection();
        #제목 업데이트
        #dbConnection.InsertQueryExecute("update Torrent set Title = '" + name + "' where Title='' and magnetUrl = '" + baseUsMagnetUrl + "'");

        #이미지 업데이트
        downloadPath = "/home/pi/Downloads";
        tmpPath = os.path.join(os.getcwd(), "app/static/app/Thumbnail");
        
        tmpThumbnailPath = os.path.join(tmpPath, fileName + ".jpg");
        osDefine.Logger("tmpThumbnailPath : " + tmpThumbnailPath);
        downloadFilePath = os.path.join(downloadPath, name);
    
        if(os.path.isfile(downloadFilePath)):
            makeThumbnail = "ffmpeg -y -i '" + downloadFilePath + "' -ss 00:00:20 -vframes 1 '" + tmpThumbnailPath + "'";
            osDefine.Logger(makeThumbnail);
            os.system(makeThumbnail);
            with open(tmpThumbnailPath, "rb") as f:
                bindata = f.read();
                utfData = str(base64.b64encode(bindata));
                updateQuery = "update Torrent set ThumbnailImage = '" + utfData + "' where DataLength(ThumbnailImage)=0 and magnetUrl = '" + baseUsMagnetUrl + "'";
                osDefine.Logger(updateQuery)
                dbConnection.InsertQueryExecute(updateQuery);

    @staticmethod
    def SMI2SRT(curPath):
        for subList in os.listdir(curPath):
            subItem = os.path.join(curPath, subList);
            if( True == os.path.isdir(subItem)):
                SMI2SRT(subItem);
            elif(True == os.path.isfile(subItem)):
                fileName, ext = os.path.splitext(subItem);
                if('.smi' == ext.lower()):
                    subs = ("subs -c srt %s.smi -o %s_tmp.srt") % (fileName, fileName);
                    os.system(subs);
                    subs = ("iconv -f euc-kr -t utf8 %s_tmp.srt -o %s.srt") % (fileName, fileName);
                    os.system(subs);
        os.system("cd " + curPath);
        os.system("rm *_tmp.srt");

    @staticmethod
    def torrentDownloadComplete(request):
        osDefine.Logger("torrentDownloadComplete (+) " + os.getcwd());
        name = request.POST.get("name");
        magnetUrl = request.POST.get("MagnetUrl");

        osDefine.Logger("Name : " + name);
        osDefine.Logger("echo magnetUrl : " + magnetUrl);

        fileName, ext = os.path.splitext(name);
        try :
            torrent.MakeFile(fileName, name, magnetUrl);
        except Exception as e:
            osDefine.Logger("Thumbnail Create Exception");
            osDefine.Logger(e);
        osDefine.Logger("FCM.SendFireBase(name)");
        FCM.SendFireBase(name);

        torrent.SMI2SRT(osDefine.LocalFilePath());
        return HttpResponse("");

    @staticmethod
    def getMeta(param):
        connection = DBExecute.GetDBConnection();
        selectQuery = "select value from meta where name='%sindex'" % param;
        rows = connection.QueryExecute(selectQuery);
        listRow = list(rows);
        return str(listRow[0][0]).strip();

    @staticmethod
    def updateTorrentIndex(index, metaName):
        connection = DBExecute.GetDBConnection();
        if(int(index) > 100):
            selectQuery = ("update meta set value='%s' where name='%sIndex'" % (index, metaName));
            rows = connection.InsertQueryExecute(selectQuery);
        return torrent.getMeta(metaName);

    @staticmethod
    def updateEntIndex(index):
        metaName = "Ent";
        return torrent.updateTorrentIndex(index, metaName);

    @staticmethod
    def updateDocuIndex(index):
        metaName = "Docu";
        return torrent.updateTorrentIndex(index, metaName);

    @staticmethod
    def updateTvendIndex(index):
        metaName = "Tvend";
        return torrent.updateTorrentIndex(index, metaName);

    @staticmethod
    def updateDramaIndex(index):
        metaName = "drama";
        return torrent.updateTorrentIndex(index, metaName);
            

