from django.http import HttpResponse
import os,sys
import glob
from .osDefine import osDefine
#import win32gui,win32con, time,sys, win32ui

#from tkinter import*
#import tkinter.messagebox
3import base64

class playView(object):
    @staticmethod
    def play(playVideo):

        os.system("C:\Temp\\" + playVideo.GET["file"])
        #osDefine.PlayFile(playVideo.GET["file"])

        moviPlayer = str(win32gui.FindWindow("ApplicationFrameWindow", None))
        http = "<html> <script src=\"http://code.jquery.com/jquery-1.11.2.min.js\"></script>"

        if(moviPlayer == "0"):
            http += "Not Play Media.<p>"
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
            http += "alert('fail!!');"
            http += "}"
            http += ", success : function(data){"
            http += "alert(\"value : \" + data) ;"
            http += "$(\"#dataArea\").html(data) ;"
            http += "}"
            http += "});"
            http += "})"
            http += "})"
            http += "</script>"

            http += "<input type='button' id=\"listButton\" value='forward' OnClick='ButtonClick_Event()'/>"
            http += "<input type='button' value='back'/>"
            http += "<input type='button' value='plus'/>"
            http += "<input type='button' value='minus'/>"
            http += "</html>"

        return HttpResponse(http)

    @staticmethod
    def playerMove(keyMove):

        #moviPlayer = win32gui.FindWindow(osDefine.PlayerName(), None)

        #win32gui.PostMessage(moviPlayer, win32con.WM_KEYDOWN, win32con.VK_RIGHT, 0);
        #win32gui.PostMessage(moviPlayer, win32con.WM_KEYUP, win32con.VK_RIGHT, 0);
        
        return HttpResponse("aaaaa");