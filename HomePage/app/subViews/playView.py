from django.http import HttpResponse
import os.path
import os,sys

import cgi
import cgitb; cgitb.enable()

class playView(object):
    @staticmethod
    def play(playVideo):
        #code = 'omxplayer '+ playVideo
        #os.system(code) # 터미널에 입력

        arguments = cgi.FieldStorage()
        http = self.request.GET.get("file")
        for i in arguments.keys():
            http += arguments[i].value
        return HttpResponse(http)
