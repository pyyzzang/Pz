from django.http import HttpResponse
import os,sys
import glob
from ..module.osDefine import osDefine
from .YoutubeView import YoutubeView
#import win32gui,win32con, time,sys, win32ui

#from tkinter import*
#import tkinter.messagebox
#import base64

from django.shortcuts import render

class Person():
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

class playView(object):

    @staticmethod 
    def getPlayViewContext(width="100%", height="100%"):
        playVideo = False if ("" == osDefine.getPlayFileName()) else True
        context = {"PlayVideo" :  playVideo,
            "height" : height,
            "width" : width,
            "fileName" : osDefine.getPlayFileName()}
        return context
    @staticmethod
    def getPlayView(request, height = "100%", width="100%"):
        playVideo = ("" == osDefine.getPlayFileName()) and False or True
        return render(request, "playView.html", playView.getPlayViewContext())
    
    @staticmethod
    def play(request):
        filePath = request.GET.get("file", "")
        if (filePath != ""):
            osDefine.PlayFile(filePath)
        else :
            filePath = request.GET.get("youtube", "")
            title = osDefine.Base64Decoding(request.GET.get("title", ""))
            osDefine.Logger("title : " + title)    
            YoutubeView.play(filePath, title)
        #return playView.getPlayView(request)
        folder = os.path.dirname(filePath)
        if("" == folder):
            url = "/Home"
        else:
            url = "/Home?file=" +folder

        context = {"URL" : url }
        return render(request, "Redirect.html", context)

    @staticmethod
    def moveVideo(keyMove):
        handle = pywinauto.findwindows.find_window(best_match=osDefine.GetPlayerName())
        app = pywinauto.application.Application().connect(handle=handle)
        app.window_().TypeKeys('{' + keyMove + '}')
        return HttpResponse("aaaaa")
