from django.http import HttpResponse
import os
import pathlib

class fileListView(object):
    @staticmethod
    def getFileList(ext):
        http = "<http>"
        http += "<table border='1'> " 

        if("nt" == os.name):
            localFilePath = "C:\Temp"
            ip = "http://localhost:8000"
        else:
            localFilePath = "/home/pi/Downloads"
            ip = "http://192.168.25.3:8000"
        
        for (path, dir, files) in os.walk(localFilePath):
            for file in files:
                http += "<tr>"
                http = http + "<td> <a href=\"" + ip + "/Play&file=" + file + "\">" +file + "</a></td>"
                http = http + "<td><button width=\"100\" height=\"100\"/></td>"
                http += "</tr>"
        http += "</table>"
        http = http + "</http>"
        return HttpResponse(http)