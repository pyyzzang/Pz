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

    def getExt(self):
        return self.ext;

    def getTitle(self):
        return strUtil.getMatchTitle(self.filePath);
    def isVideoFile(self):
        return self.getExt() in osDefine.SupportExt;
    def getEncodingFileName(self):
        return osDefine.Base64Encoding(self.getUrlPath());
    def getUrlPath(self):
        if(-1 != self.dir.find(osDefine.LocalFilePath())):
            return self.dir.replace(osDefine.LocalFilePath(), '') + '/' + self.filePath;
        return self.filePath;

class fileListView(object):
    @staticmethod
    def getViewList(ext):
        http = "<http>";
        http += "<script src=\"http://code.jquery.com/jquery-1.11.2.min.js\"></script>"
        http += '<body Onload="FormLoad()"/>';
        http += fileListView.getVideoList('');
        http += YoutubeView.getVideoList();
        http += "</body>";
        http += "<script>";
        http += "function FormLoad(){";
        http += "if(FileViewTable.style.visibility == 'collapse')";
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
    def getVideoList(ext):
        
        localFilePath = osDefine.LocalFilePath()
        ip = osDefine.Ip()
        fileCount = 0;      
        fileInfoList = []; 
        for (path, dir, files) in os.walk(localFilePath):
            for file in files:
                info = FileInfo(file, path);
                if(True == info.isVideoFile()):
                    fileInfoList.append(info);

        fileInfoList.sort();
        http = "";
        http += "<Table id='FileViewTable' border='1'>";
        for info in fileInfoList:
                http += "<tr>"
                fileStr = osDefine.Base64Encoding(file);
                http = http + "<td> <a href=Play\?file="+ info.getEncodingFileName() + ">" + info.getTitle() + "</a></td>"
                http = http + "<td><button id=File" + str(fileCount) + " >삭제</button>"
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
                http += "}"
                http += ", success : function (data){"
                http += "}})})})</script>"
                fileCount = fileCount + 1;
        http +="</table>";
        return http;

    @staticmethod
    def delete(request):
        deleteFile = osDefine.Base64Decoding(request.GET["fileName"]);
        splitPath = deleteFile.split('/',2);
        if(3 == len(splitPath)):
          os.system('sudo chown pi "' + osDefine.LocalFilePath() + "/" + splitPath[1] +"\"");

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
