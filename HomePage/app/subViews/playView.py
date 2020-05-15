from django.http import HttpResponse
import os,sys
import glob
from ..module.osDefine import osDefine
from .YoutubeView import YoutubeView;
#import win32gui,win32con, time,sys, win32ui

#from tkinter import*
#import tkinter.messagebox
#import base64

from django.shortcuts import render

class Person():
    def __init__(self, Name, Age):
        self.Name = Name;
        self.Age = Age;

class playView(object):
    @staticmethod
    def getPlayView(request, height = "100%", width="100%"):
        ret = "";
        try:
            if("" == osDefine.getPlayFileName()):
                osDefine.Logger("Empty");
                PersonList = [];
                PersonList.append(Person("1", 10));
                context = {"PersonList" : PersonList};
                return render(request, "playView.html", context);
            else:
                osDefine.Logger("Not Empty");
                context = {"Title" : "aa"};
                return render(request, "playView.html", context);
                return ret;
        except Exception as e:
            osDefine.Logger(e);
        return ret;
    
    @staticmethod
    def play(request):
        #return HttpResponse(osDefine.LocalFilePath()+ "\\" + playVideo.GET["file"].replace('"',''));
        filePath = request.GET.get("file", "");
        if (filePath != ""):
            osDefine.PlayFile(filePath);
        else :
            filePath = request.GET.get("youtube", "");
            title = osDefine.Base64Decoding(request.GET.get("title", ""));
            osDefine.Logger("title : " + title);    
            YoutubeView.play(filePath, title);
        return playView.getPlayView(request);

    @staticmethod
    def moveVideo(keyMove):
        handle = pywinauto.findwindows.find_window(best_match=osDefine.GetPlayerName())
        app = pywinauto.application.Application().connect(handle=handle)
        app.window_().TypeKeys('{' + keyMove + '}')
        return HttpResponse("aaaaa");
