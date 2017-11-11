from django.http import HttpResponse
import os
import pathlib

class fileListView(object):
    def getFileList(ext):
        http = "<http>"
        http += "<table border='1'> " 
        
        for (path, dir, files) in os.walk("/home/pi/Downloads"):
            for file in files:
                http += "<tr>"
                http = http + "<td>" + file + "</td>"
                http = http + "<td><button width=\"100\" height=\"100\"/></td>"
                http += "</tr>"
        http += "</table>"
        http = http + "</http>"
        return HttpResponse(http)