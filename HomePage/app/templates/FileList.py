from django.http import HttpResponse
import io

class Path(object):
    def GetFileList(ext = ""):
        fileList = io.path
        http = "<Http>"
        for file in fileList:
            http = http + file
        http = http + "<Http>"
        return HttpResponse(http)






