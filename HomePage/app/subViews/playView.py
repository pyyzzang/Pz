from django.http import HttpResponse
import os.path
import os,sys
from .osDefine import osDefine
import win32gui,win32con, time,sys

class playView(object):
    @staticmethod
    def play(playVideo):
        #code = 'omxplayer '+ playVideo
        #os.system(code) # 터미널에 입력

        os.system(osDefine.LocalFilePath() + "\\" + playVideo.GET['file'])

        moviPlayer = str(win32gui.FindWindow("ApplicationFrameWindow", "영화 및 TV"))
        http = "FindWindow : " + moviPlayer

        win32gui.SetWindowPos(int(moviPlayer), win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
        http += "File : " + playVideo.GET['file']

        return HttpResponse(http)