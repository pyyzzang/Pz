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
            for file in files:

                fileName, ext = os.path.splitext(file);
                if(".mp4" != ext):
                    continue;

                fileCount = fileCount + 1;
                http += "<tr>"
 
                fileBytes = base64.b64encode(file.encode("utf-8"));
                fileStr = str(fileBytes, "utf-8");
                http = http + "<td> <a href=Play\?file="+ str(fileStr) + ">" +file + "</a></td>"
                http = http + "<td><button id=File" + str(fileCount) + " >삭제</button>"
                http += "</tr>"
              
                http += "<script type=\"text/javascript\">";
                http += "$(function(){" 
                http += "$(\"#File"+str(fileCount)+"\").click(function(){"
                http += "$.ajax({"
                http += "type:'get'"
                http += ",url:'fileDelete'"
                http += ", dataType:'html'"
                http += ",error : function(){"
                http += "alert('fail')"
                http += "}"
                http += ", success : function (data){"
                http += "alert(data)}})})})</script>"
        http += "</table>"
        http = http + "</http>"
        return HttpResponse(http)
