from django.http import HttpResponse
import os
import pathlib
from .osDefine import osDefine
import base64

class fileListView(object):
    @staticmethod
    def getFileList(ext):
        http = "<http>"

        http += "<script src=\"http://code.jquery.com/jquery-1.11.2.min.js\"></script>"
        http += "<table border='1'> " 

        
        localFilePath = osDefine.LocalFilePath()
        ip = osDefine.Ip()
        fileCount = 0;       
        for (path, dir, files) in os.walk(localFilePath):
            files.sort();
            for file in files:

                fileName, ext = os.path.splitext(file);
                if(".mp4" != ext and ".mkv" != ext):
                    continue;
                if(-1 != path.find(localFilePath)):
                     file = path.replace(localFilePath,'') + '/' + file;


                fileCount = fileCount + 1;
                http += "<tr>"
 
                fileStr = osDefine.Base64Encoding(file);
                http = http + "<td> <a href=Play\?file="+ str(fileStr) + ">" +file + "</a></td>"
                http = http + "<td><button id=File" + str(fileCount) + " >삭제</button>"
                http += "</tr>"
              
                http += "<script type=\"text/javascript\">";
                http += "$(function(){" 
                http += "$(\"#File"+str(fileCount)+"\").click(function(){"
                http += "$.ajax({"
                http += "type:'get'"
                http += ",url:'Home/Delete'"
                http += ",dataType:'html'"
                http += ",data:{'fileName':'"+fileStr+"'}"
                http += ",error : function(){"
                http += "alert('fail')"
                http += "}"
                http += ", success : function (data){"
                http += "alert(data)}})})})</script>"
        http += "</table>"
        http = http + "</http>"
        return HttpResponse(http)

    @staticmethod
    def delete(request):
        deleteFile = osDefine.Base64Decoding(request.GET["fileName"]);
        deleteFullPath = (osDefine.LocalFilePath() + "/" + deleteFile)    
        if(False == os.path.exists(deleteFullPath)):
            return HttpResponse("");
        os.remove(deleteFullPath);
        return HttpResponse(deleteFullPath);

