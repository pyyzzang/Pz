# -*- coding: utf-8 -*- 
from django.http import HttpResponse
import os
import pathlib
from .osDefine import osDefine
from .strUtil import strUtil
import base64
from .osDefine import PlayMode
from .YoutubeView import YoutubeView

class FileInfo:
    def __init__(self, filePath, dir):
        self.filePath = filePath;
        self.dir = dir;
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
            return "<a href=http://192.168.219.102:8000/Home>Parent</a>";
        if True == self.isDirectory() :
            return "<a href=Home\?file="+ self.getEncodingFileName() + ">" + self.getTitle() + "</a>";
        else:
            return "<a href=Play\?file="+ self.getEncodingFileName() + ">" + self.getTitle() + "</a>";

class fileListView(object):
    @staticmethod
    def getViewList(request):
        fileListView.deleteEmptyFolder();
        try:
            deleteFile = osDefine.Base64Decoding(request.GET["file"]);
        except Exception:
            deleteFile = "";
        http = "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no\" />"
        http += "<http>";
        http += "<script src=\"http://code.jquery.com/jquery-1.11.2.min.js\"></script>"
        http += '<body Onload="FormLoad()">';
        http += '<input name="ViewType" id="FileRadio" Value="File" type="radio" OnChange="RadioChecked(this)"> 파일 </input>';
        http += '<input name="ViewType" Value="Youtube" type="radio" OnChange="RadioChecked(this)" >Youtube</input>'
        http += fileListView.getVideoList(deleteFile);
        http += YoutubeView.getVideoList();
        http += "</body>";
        http += "<script>";
        http += "function FormLoad(){"
        http += "document.getElementById('FileRadio').checked = true;"
        http += "RadioChecked(document.getElementById('FileRadio'));}";
        http += "function RadioChecked(radio){";
        http += "if(radio.value=='File')";
        http += "{";
        http += 'YoutubeTable.style.visibility = "collapse";';
        http += 'FileViewTable.style.visibility = "visible";';
        http += '}';
        http += 'else';
        http += '{';
        http += 'FileViewTable.style.visibility = "collapse";';
        http += 'YoutubeTable.style.visibility = "visible";';
        http += '}}';
        http += "</script>";
        http += "</http>";
        return HttpResponse(http); 
    @staticmethod
    def getVideoList(dirPath):
        localFilePath = osDefine.LocalFilePath()
        ip = osDefine.Ip()
        fileCount = 0;      
        fileInfoList = []; 
        findDir = localFilePath + "/" + dirPath;
        for file in os.listdir(findDir):
                info = FileInfo(file, findDir);
                if(True == info.isVideoFile() or True == info.isDirectory()):
                    fileInfoList.append(info);

        fileInfoList.sort();
        http = "<Head> <link rel='stylesheet' href='/static/app/css/style.css'></Head>";
        http += "<Table id='FileViewTable' border='1'>";
        if( "" != dirPath):
            parentInfo = FileInfo("", localFilePath);
            fileInfoList.insert(0,parentInfo);
        for info in fileInfoList:
                http += "<tr height=40>"
                fileStr = osDefine.Base64Encoding(file);
                http += "<td id='" + info.getThumbNailId() + "'></td>";
                http += "<td id='playLink'> " + info.getLink() + "</td>"
                http += "<td id='deleteButton'>";
                if( info.getTitle() != ""):
                    http += "<button id=File" + str(fileCount) + " >삭제</button>";
                http += "</tr>"
                http += "<script type=\"text/javascript\">";
                http += "$(function(){" 
                http += "$(\"#File"+str(fileCount)+"\").click(function(){"
                http += "if(false == confirm('"+ info.getTitle() + "을 삭제 하시겠습니까?')){return;}"
                http += "$.ajax({"
                http += "type:'get'"
                http += ",url:'Home/Delete'"
                http += ",dataType:'html'"
                http += ",data:{'fileName':'"+info.getEncodingFileName()+"'}"
                http += ",error : function(data){"
                http += "alert(data);"
                http += "}"
                http += ", success : function (data){"
                http += "alert(data);"
                http += "}})})})</script>"
                fileCount = fileCount + 1;
        http +="</table>";
        return http;

    @staticmethod
    def delete(request):
        deleteFile = osDefine.Base64Decoding(request.GET["fileName"]);
        splitPath = deleteFile.split('/',2);
        if(3 == len(splitPath)):
          os.system('sudo chown -R pi "' + osDefine.LocalFilePath() + "/" + splitPath[1] +"\"");

        deleteFullPath = (osDefine.LocalFilePath() + "/" + deleteFile)    
        if(False == os.path.exists(deleteFullPath)):
            return HttpResponse("");
        os.remove(deleteFullPath);
        deleteEmptyFolder();
        return HttpResponse(deleteFullPath);
    @staticmethod
    def deleteEmptyFolder():
        baseDir = osDefine.LocalFilePath();

        deleteFolder = "";
        for subItem in os.listdir(baseDir):
            checkItem = baseDir + "/" + subItem;
            if(True == os.path.isdir(checkItem)):
                if(True == osDefine.checkEmpty(checkItem)):
                    os.system("sudo rm -r \"" + checkItem + "\"");
