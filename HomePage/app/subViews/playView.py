from django.http import HttpResponse
import os,sys
import glob
from ..module.osDefine import osDefine
from .YoutubeView import YoutubeView;
#import win32gui,win32con, time,sys, win32ui

#from tkinter import*
#import tkinter.messagebox
#import base64

class playView(object):
    @staticmethod
    def play(playVideo):
        #return HttpResponse(osDefine.LocalFilePath()+ "\\" + playVideo.GET["file"].replace('"',''));
        filePath = playVideo.GET.get("file", "");
        if (filePath != ""):
            osDefine.PlayFile(filePath);
        else :
            filePath = playVideo.GET.get("youtube", "");
            YoutubeView.play(filePath);
        http =filePath;
        http += "<html> <script src=\"http://code.jquery.com/jquery-1.11.2.min.js\"></script>"
        http += "<Head> <link rel='stylesheet' href='/static/app/css/style.css'> </Head>";
        if(0):
            http += "Not Play Media.<p>"
        else:
            http += "<script type=\"text/javascript\">"
            #Back600
            http += "$(function(){"
            http += "$(\"#Back600Button\").click(function(){"
            http += "$.ajax({"
            http += "type: 'get'"
            http += ", url: 'Back600'"
            http += ", dataType : 'html'"
            http += ", error : function(){"
            http += "}"
            http += ", success : function(data){"
            http += "}"
            http += "});"
            http += "})"
            http += "})"
            http += "</script>"


            #Back10
            http += "<script type=\"text/javascript\">"
            http += "$(function(){"
            http += "$(\"#Back10Button\").click(function(){"
            http += "$.ajax({"
            http += "type: 'get'"
            http += ", url: 'Back'"
            http += ", dataType : 'html'"
            http += ", error : function(){"
            http += "alert('fail!!');"
            http += "}"
            http += ", success : function(data){"
            http += "}"
            http += "});"
            http += "})"
            http += "})"
            http += "</script>"

            #RePlay
            http += "<script type=\"text/javascript\">"
            http += "$(function(){"
            http += "$(\"#ReplayButton\").click(function(){"
            http += "$.ajax({"
            http += "type: 'get'"
            http += ", url: 'Replay'"
            http += ", dataType : 'html'"
            http += ", error : function(){"
            http += "}"
            http += ", success : function(data){"
            http += "}"
            http += "});"
            http += "})"
            http += "})"
            http += "</script>"

            #Pause
            http += "<script type=\"text/javascript\">"
            http += "$(function(){"
            http += "$(\"#PauseButton\").click(function(){"
            http += "$.ajax({"
            http += "type: 'get'"
            http += ", url: 'Pause'"
            http += ", dataType : 'html'"
            http += ", error : function(){"
            http += "alert('fail!!');"
            http += "}"
            http += ", success : function(data){"
            http += "}"
            http += "});"
            http += "})"
            http += "})"
            http += "</script>"

            #Skip10
            http += "<script type=\"text/javascript\">"
            http += "$(function(){"
            http += "$(\"#Skip10Button\").click(function(){"
            http += "$.ajax({"
            http += "type: 'get'"
            http += ", url : 'Skip'"
            http += ", dataType : 'html'"
            http += ", error : function(){"
            http += "alert('fail!!');"
            http += "}"
            http += ", success : function(data){"
            http += "}"
            http += "});"
            http += "})"
            http += "})"
            http += "</script>"

            #Skip600
            http += "<script type=\"text/javascript\">"
            http += "$(function(){"
            http += "$(\"#Skip600Button\").click(function(){"
            http += "$.ajax({"
            http += "type: 'get'"
            http += ", url: 'Skip600'"
            http += ", dataType : 'html'"
            http += ", error : function(){"
            http += "alert('fail!!');"
            http += "}"
            http += ", success : function(data){"
            http += "}"
            http += "});"
            http += "})"
            http += "})"
            http += "</script>"

            #VolumeUpButton
            http += "<script type=\"text/javascript\">"
            http += "$(function(){"
            http += "$(\"#VolumeUpButton\").click(function(){"
            http += "$.ajax({"
            http += "type: 'get'"
            http += ", url: 'VolumeUp'"
            http += ", dataType : 'html'"
            http += ", error : function(){"
#            http += "alert('fail!!');"
            http += "}"
            http += ", success : function(data){"
            http += "}"
            http += "});"
            http += "})"
            http += "})"
            http += "</script>"

            #VolumeDown
            http += "<script type=\"text/javascript\">"
            http += "$(function(){"
            http += "$(\"#VolumeDownButton\").click(function(){"
            http += "$.ajax({"
            http += "type: 'get'"
            http += ", url: 'VolumeDown'"
            http += ", dataType : 'html'"
            http += ", error : function(){"
            http += "alert('fail!!');"
            http += "}"
            http += ", success : function(data){"
            http += "}"
            http += "});"
            http += "})"
            http += "})"
            http += "</script>"

            http += "<body>"

            http += "<div class='main'>                                                                             ";
            http += "	<div class='buttonDiv'><button id='Back600Button' class='back600'/>	</div>                  ";
            http += "	<div class='buttonDiv'><button id='Back10Button' class='back10'/>	</div>                      ";
            http += "	<div class='buttonDiv'><button id='ReplayButton' class='play' /> </div>                     ";
            http += "	<div class='buttonDiv'><button id='PauseButton' class='pause'/>	</div>                  ";
            http += "	<div class='buttonDiv'><button id='Skip10Button' class='skip10'/>	</div>                      ";
            http += "	<div class='buttonDiv'><button id='Skip600Button' class='skip600'/>	</div>                  ";
            http += "</div>                                                                                         ";
            http += "<div class='Empty20'>                                                                          ";
            http += "	<label> </label>                                                                            ";
            http += "</div>                                                                                         ";
            http += "<div class='volumeMain'>                                                                       ";
            http += "	<div class='volumeDiv'><button id='VolumeUpButton' class='volumeUp'/>	</div>              ";
            http += "	<div class='volumeDiv'><button id='VolumeDownButton' class='volumeDown'/>	</div>	        ";
            http += "</div>                                                                                         ";
            http += "</body>                                                                                        ";


            http += "</html>"

        return HttpResponse(http)

    @staticmethod
    def moveVideo(keyMove):
        handle = pywinauto.findwindows.find_window(best_match=osDefine.GetPlayerName())
        app = pywinauto.application.Application().connect(handle=handle)
        app.window_().TypeKeys('{' + keyMove + '}')
        return HttpResponse("aaaaa");
