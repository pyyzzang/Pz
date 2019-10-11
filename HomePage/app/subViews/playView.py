from django.http import HttpResponse
import os,sys
import glob
from .osDefine import osDefine
#import win32gui,win32con, time,sys, win32ui

#from tkinter import*
#import tkinter.messagebox
#import base64

class playView(object):
    @staticmethod
    def play(playVideo):
        #return HttpResponse(osDefine.LocalFilePath()+ "\\" + playVideo.GET["file"].replace('"',''));

        http= osDefine.PlayFile(playVideo.GET["file"].replace('"',''))

        #moviPlayer = str(win32gui.FindWindow("ApplicationFrameWindow", None))
        http += "<html> <script src=\"http://code.jquery.com/jquery-1.11.2.min.js\"></script>"

        if(0):
            http += "Not Play Media.<p>"
        else:
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
    def moveVideo(keyMove):
        handle = pywinauto.findwindows.find_window(best_match=osDefine.GetPlayerName())
        app = pywinauto.application.Application().connect(handle=handle)
        app.window_().TypeKeys('{' + keyMove + '}')
        return HttpResponse("aaaaa");
