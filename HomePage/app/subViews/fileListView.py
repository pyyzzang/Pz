from django.http import HttpResponse
import os

class fileListView(object):
    def getFileList(ext):
        http = "<http>"
        for (path, dir, files) in os.walk("C:\Temp"):
            for file in files:
                http = http + file
        http = http + "</http>"
        return HttpResponse(http)