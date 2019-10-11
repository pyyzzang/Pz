from django.http import HttpResponse
import os
import pathlib
from .osDefine import osDefine
import base64

class fileListView(object):
    @staticmethod
    def getFileList(ext):
        http = "<http>"
        http += "<table border='1'> " 

        
        localFilePath = osDefine.LocalFilePath()
        ip = osDefine.Ip()
        
        for (path, dir, files) in os.walk(localFilePath):
            for file in files:
                http += "<tr>"
 
                fileBytes = base64.b64encode(file.encode("utf-8"));
                fileStr = str(fileBytes, "utf-8");
                http = http + "<td> <a href=Play\?file="+ fileStr + ">" +file + "</a></td>"
                http = http + "<td><button width=\"100\" height=\"100\"/>11111</td>"
                http += "</tr>"
        http += "</table>"
        http = http + "</http>"
        return HttpResponse(http)
