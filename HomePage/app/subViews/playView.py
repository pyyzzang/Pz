from django.http import HttpResponse
import os.path
import os,sys
from .osDefine import osDefine
import win32gui,win32con, time,sys

from tkinter import*
import tkinter.messagebox


class playView(object):
    @staticmethod
    def play(playVideo):
        #code = 'omxplayer '+ playVideo
        #os.system(code) # 터미널에 입력

        moviPlayer = str(win32gui.FindWindow("ApplicationFrameWindow", "영화 및 TV"))
        http = "<html> <script src=\"http://code.jquery.com/jquery-1.11.2.min.js\"></script>"
        http += "FindWindow : " + moviPlayer
        if(moviPlayer == 0):
            os.system(osDefine.LocalFilePath() + "\\" + playVideo.GET['file'])

        #win32gui.SetWindowPos(int(moviPlayer), win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
        http += "File : " + playVideo.GET['file']
        
        http += "<script type=\"text/javascript\">"
        http += "$(function(){"
        http += "$(\"#listButton\").click(function(){"
        http += "$.ajax({"
        http += "type: 'get'"
        http += ", url: 'www.naver.com'"
        http += ", dataType : 'html'"
        http += ", error : function(){"
        http += "alert('통신실패!!');"
        http += "}"
        http += ", success : function(data){"
        http += "alert(\"통신데이터 값 : \" + data) ;"
        http += "$(\"#dataArea\").html(data) ;"
        http += "}"
        http += "});"
        http += "})"
        http += "})"
        http += "</script>"

        http += "<input type='button' id=\"listButton\" value='앞으로' OnClick='ButtonClick_Event()'/>"
        http += "<input type='button' value='뒤로'/>"
        http += "<input type='button' value='소리올리기'/>"
        http += "<input type='button' value='소리내리기'/>"
        http += "</html>"

        return HttpResponse(http)
