# -*- coding: utf-8 -*- 
from django.http import HttpResponse
import os
import pathlib
from ..module.osDefine import osDefine
from ..module.strUtil import strUtil
import base64
from ..module.osDefine import PlayMode;
from .YoutubeView import YoutubeView;
from ..module.HtmlUtil import HtmlUtil;
from ..Data.PlayInfo import PlayInfos;
from .playView import playView;

class FileInfo:
    def __init__(self, filePath, dir, request):
        self.filePath = filePath;
        self.dir = dir;
        self.request = request;
        self.fileName, self.ext = os.path.splitext(filePath);
    def __lt__(self, other):
        return self.getTitle() < other.getTitle(); 
    def getFileName(self):
        return self.fileName;
    def getFullName(self):
        return self.dir + "/" + self.filePath;
    def getExt(self):
        return self.ext;

    def getTitle(self):
        title = strUtil.getMatchTitle(self.filePath);
        if(" " == title):
            title = self.filePath;
        return title;
    def isVideoFile(self):
        return self.getExt() in osDefine.SupportExt;
    def isDirectory(self):
        return os.path.isdir(self.getFullName());
    def visibleDeleteButton(self):
        return "" == self.filePath and "Hidden" or "Visible";
    def getThumbNailId(self):
        return "Thumbnail" + (self.isDirectory() and "Dir" or "File");
    def getEncodingFileName(self):
        return osDefine.Base64Encoding(self.getUrlPath());
    def getUrlPath(self):
        if(-1 != self.dir.find(osDefine.LocalFilePath())):
            return self.dir.replace(osDefine.LocalFilePath(), '') + '/' + self.filePath;
        return self.filePath;
    def getLink(self):
        if("" == self.filePath):
            localFilePath = osDefine.LocalFilePath();
            parentPath = self.dir.replace(localFilePath, "");
            splitParentPath = os.path.split(parentPath)[0];
            osDefine.Logger("splitParentPath : " + splitParentPath);
            
            osPath = osDefine.Base64Encoding(splitParentPath);
            if("/" != splitParentPath):
                return "location.href='" + osDefine.getRunIp(self.request) + "/Home?file=" + osPath + "'";
            return "location.href='" + osDefine.getRunIp(self.request) + "/Home'";
        if True == self.isDirectory() :
            return "location.href='" + osDefine.getRunIp(self.request) + "/Home?file="+ self.getEncodingFileName() + "'";
        else:
            return "location.href='" + osDefine.getRunIp(self.request) + "/Play?file=" + self.getEncodingFileName() + "'";

    def getTr(self, fileCount, playInfo):
        retHttp  = '<tr class="TableRow">';
        retHttp += "<td class='column_Thumbnail' id='" + self.getThumbNailId() + "'></td>";
        retHttp += "<td class='column_Title' onMouseOver=\"this.style.background='#8693ca'\" onmouseout=\"this.style.background='white'\"  OnClick=\"" + self.getLink() + "\">" ;
        retHttp += "<div>" + self.getTitle() +"</div>";
        if(True == self.isVideoFile()):
            if("" != playInfo):
                retHttp += "<div><progress class='VideoProgress' id=\"Pro_" + self.getEncodingFileName() +"\" max=100 value=" + str(playInfo.getProgressValue()) + " \"/></div>";
        retHttp += "</td>";
        retHttp += "<td class='column_Delete' id='deleteButton'>" + "<button id=File" + str(fileCount) + " style=\"visibility:" + self.visibleDeleteButton() + "\"'>삭제</button>" + " </td>";
        retHttp += "</tr>";
        retHttp += "<script type=\"text/javascript\">";
        retHttp += "$(function(){" 
        retHttp += "$(\"#File"+str(fileCount)+"\").click(function(){"
        retHttp += "if(false == confirm('"+ self.getTitle() + "을 삭제 하시겠습니까?')){return;}"
        retHttp += "$.ajax({"
        retHttp += "type:'get'"
        retHttp += ",url:'Home/Delete'"
        retHttp += ",dataType:'html'"
        retHttp += ",data:{'fileName':'"+self.getEncodingFileName()+"'}"
        retHttp += ",error : function(data){"
        retHttp += "}"
        retHttp += ", success : function (data){"
        retHttp += "window.location.reload();"
        retHttp += "}})})})</script>"

        return retHttp;

class fileListView(object):
    @staticmethod
    def getViewList(request):
        youtubeToken = osDefine.getParameter(request, "token");
        if(None == youtubeToken):
            oAuthUrl = "https://accounts.google.com/o/oauth2/auth?client_id=456241762082-m621opd3ej2g3kcdm0ajai5rv6h37una.apps.googleusercontent.com&redirect_uri=%s/YoutubeRedirect&response_type=code&scope=https://www.googleapis.com/auth/youtube" % osDefine.getRunIp(request);
            http = "<script>location.href=\"" + oAuthUrl + "\"</script>";
            osDefine.Logger("oAuth Url : " + http);
            return HttpResponse(http);

        fileListView.deleteEmptyFolder();
        try:
            requestFile = osDefine.Base64Decoding(request.GET["file"]);
            osDefine.Logger("requestFile : " + requestFile);
        except Exception:
            requestFile = "";

        http = "";
        try:
            http = HtmlUtil.getHeader();
            http += fileListView.getTitleHead();
            http += HtmlUtil.getBodyHead();
            http += fileListView.getVideoList(requestFile, request);
            http += YoutubeView.getVideoList(youtubeToken);

            http += HtmlUtil.getBodyTail();
            http += "</body>";
        except Exception as e:
            osDefine.Logger(e);
            http = "<script>location.href=\"" + osDefine.getRunIp(request)+"\/Home\";</script>";
        return HttpResponse(http); 
    @staticmethod
    def getTitleHead():
        retHttp  = '<body Onload="FormLoadFileListView()">';
        retHttp += "<input type='button' value='Torrent 페이지로' onclick='MoveTorrentPage();'></input><p>";
        retHttp += "<script>function MoveTorrentPage(){ location.href = '/Torrent';}</script>"
        retHttp += playView.getPlayView("200px", "70%");
        
        retHttp += '<input name="ViewType" id="FileRadio" Value="File" type="radio" OnChange="RadioChecked(this)"> 파일 </input>';
        retHttp += '<input name="ViewType" Value="Youtube" type="radio" OnChange="RadioChecked(this)" >Youtube</input>';
        retHttp += "<script>";
        retHttp += "function FormLoadFileListView(){"
        retHttp += "    document.getElementById('FileRadio').checked = true;"
        retHttp += "    RadioChecked(document.getElementById('FileRadio'));}";
        
        retHttp += "function RadioChecked(radio){";
        retHttp += "if(radio.value=='File')";
        retHttp += "{";
        retHttp += '    YoutubeTable.style.visibility = "collapse";';
        retHttp += '    FileViewTable.style.visibility = "visible";';
        retHttp += '}';
        retHttp += 'else';
        retHttp += '{';
        retHttp += '    FileViewTable.style.visibility = "collapse";';
        retHttp += '    YoutubeTable.style.visibility = "visible";';
        retHttp += '}}';
        retHttp += "</script>";
        return retHttp;

    @staticmethod
    def getTableHead():
        retHttp  = '				<table class="ListView" id="FileViewTable">                                                         ';
        retHttp += '					<thead>                                                     ';
        retHttp += '						<tr class="TableRow">                              ';
        retHttp += '							<th class="column_Thumbnail"></th>                       ';
        retHttp += '							<th class="column_Title">제목</th>                   ';
        retHttp += '							<th class="column_Delete"></th>                       ';
        retHttp += '						</tr>                                                   ';
        retHttp += '					</thead>                                                    ';
        retHttp += '                    <tbody>                                                     ';
        return retHttp;
    @staticmethod
    def getTableTail():
        return "</tbody></table>";

    @staticmethod
    def getVideoList(dirPath, request):
        localFilePath = osDefine.LocalFilePath()
        fileCount = 0;      
        fileInfoList = []; 
        findDir = localFilePath + dirPath;
        for file in os.listdir(findDir):
                info = FileInfo(file, findDir, request);
                if(True == info.isVideoFile() or True == info.isDirectory()):
                    fileInfoList.append(info);

        fileInfoList.sort();
        http = fileListView.getTableHead();

        infos = PlayInfos.GetPlayInfos();
        if( "" != dirPath):
            osDefine.Logger("DirPath : " + dirPath);
            parentInfo = FileInfo("", findDir, request);
            fileInfoList.insert(0,parentInfo);
        for info in fileInfoList:
            try:
                urlPath = info.getUrlPath();
            except Exception as e:
                osDefine.Logger(e);
            playInfo = infos.getPlayInfo(urlPath, False);
            http += info.getTr(fileCount, playInfo);
            fileCount = fileCount + 1;
        http += fileListView.getTableTail();
        
        return http;
    
    @staticmethod
    def deleteEmptyFolder():
        baseDir = osDefine.LocalFilePath();

        deleteFolder = "";
        for subItem in os.listdir(baseDir):
            checkItem = baseDir + "/" + subItem;
            if(True == os.path.isdir(checkItem)):
                if(True == osDefine.checkEmpty(checkItem)):
                    os.system("sudo rm -r \"" + checkItem + "\"");

    @staticmethod
    def delete(request):
        try:
            decodingFileName = osDefine.Base64Decoding(request.GET.get("fileName"));
            filePath = osDefine.LocalFilePath() + decodingFileName;
            deleteCmd = "sudo rm '%s'" % filePath;
            if(True == os.path.isdir(filePath)):
                deleteCmd = "%s -R" % deleteCmd;
            
            osDefine.Logger("Delete Cmd : " + deleteCmd);
            os.system(deleteCmd);
        except Exception as e:
            osDefine.Logger(e);
        return HttpResponse(deleteCmd);