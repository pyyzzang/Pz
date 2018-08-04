from django.http import HttpResponse
import os,sys
import glob
from .osDefine import osDefine
import win32gui,win32con, time,sys, win32ui

from tkinter import*
import tkinter.messagebox
import base64

class playView(object):
    @staticmethod
    def play(playVideo):

        os.system("C:\Temp\\" + playVideo.GET["file"])
        #osDefine.PlayFile(playVideo.GET["file"])

        moviPlayer = str(win32gui.FindWindow("ApplicationFrameWindow", None))
        http = "<html> <script src=\"http://code.jquery.com/jquery-1.11.2.min.js\"></script>"

        if(moviPlayer == "0"):
            http += "재생중인 미디어가 없습니다.<p>"
        else:
            #win32gui.SetWindowPos(int(moviPlayer), win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
            win32gui.SetWindowPos(int(moviPlayer), win32con.HWND_TOPMOST, 0, 0, 0, 0, 0)
        
            http += "<script type=\"text/javascript\">"
            http += "$(function(){"
            http += "$(\"#listButton\").click(function(){"
            http += "$.ajax({"
            http += "type: 'get'"
            http += ", url: 'playerMove'"
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

    @staticmethod
    def playerMove(keyMove):

        moviPlayer = win32gui.FindWindow(osDefine.PlayerName(), None)

        win32gui.PostMessage(moviPlayer, win32con.WM_KEYDOWN, win32con.VK_RIGHT, 0);
        win32gui.PostMessage(moviPlayer, win32con.WM_KEYUP, win32con.VK_RIGHT, 0);
        
        return HttpResponse(moviPlayer);