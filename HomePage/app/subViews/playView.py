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
    def getBack600():
        retHttp  = "<script type=\"text/javascript\">"
        retHttp += "$(function(){"
        retHttp += "$(\"#Back600Button\").click(function(){"
        retHttp += "$.ajax({"
        retHttp += "type: 'get'"
        retHttp += ", url: 'Play/Back600'"
        retHttp += ", dataType : 'html'"
        retHttp += ", error : function(){"
        retHttp += "}"
        retHttp += ", success : function(data){"
        retHttp += "}"
        retHttp += "});"
        retHttp += "})"
        retHttp += "})"
        retHttp += "</script>"
        retHttp += "	<div class='buttonDiv'><button id='Back600Button' class='back600'/>	</div>                  ";
        return retHttp;

    @staticmethod
    def  getBack10():
        retHttp  = "<script type=\"text/javascript\">"
        retHttp += "$(function(){"
        retHttp += "$(\"#Back10Button\").click(function(){"
        retHttp += "$.ajax({"
        retHttp += "type: 'get'"
        retHttp += ", url: 'Play/Back'"
        retHttp += ", dataType : 'html'"
        retHttp += ", error : function(){"
        retHttp += "alert('fail!!');"
        retHttp += "}"
        retHttp += ", success : function(data){"
        retHttp += "}"
        retHttp += "});"
        retHttp += "})"
        retHttp += "})"
        retHttp += "</script>"
        retHttp += "	<div class='buttonDiv'><button id='Back10Button' class='back10'/>	</div>                      ";
        return retHttp;
    
    @staticmethod
    def getRePlay():
        retHttp = "";
        retHttp += "<script type=\"text/javascript\">"
        retHttp += "$(function(){"
        retHttp += "$(\"#ReplayButton\").click(function(){"
        retHttp += "$.ajax({"
        retHttp += "type: 'get'"
        retHttp += ", url: 'Play/Replay'"
        retHttp += ", dataType : 'html'"
        retHttp += ", error : function(){"
        retHttp += "}"
        retHttp += ", success : function(data){"
        retHttp += "replayDiv = document.getElementById('Replay');"
        retHttp += "pauseDiv = document.getElementById('Pause');"
        retHttp += "replayDiv.style.visibility='hidden';"
        retHttp += "pauseDiv.style.visibility='visible';"
        retHttp += "}"
        retHttp += "});"
        retHttp += "})"
        retHttp += "})"
        retHttp += "</script>"
        retHttp += "	    <div id='Replay' class='buttonFullDiv' style='position: relative;left:0px; top: 100%; visibility:hidden'><button id='ReplayButton' class='play' /> </div>                     ";
        return retHttp;
    @staticmethod
    def getPause():
        retHttp = "";
        retHttp += "<script type=\"text/javascript\">"
        retHttp += "$(function(){"
        retHttp += "$(\"#PauseButton\").click(function(){"
        retHttp += "$.ajax({"
        retHttp += "type: 'get'"
        retHttp += ", url: 'Play/Pause'"
        retHttp += ", dataType : 'html'"
        retHttp += ", error : function(){"
        retHttp += "alert('fail!!');"
        retHttp += "}"
        retHttp += ", success : function(data){"
        retHttp += "replayDiv = document.getElementById('Replay');"
        retHttp += "pauseDiv = document.getElementById('Pause');"
        retHttp += "replayDiv.style.visibility='visible';"
        retHttp += "pauseDiv.style.visibility='hidden';"
        retHttp += "}"
        retHttp += "});"
        retHttp += "})"
        retHttp += "})"
        retHttp += "</script>"
        retHttp += "	    <div id='Pause' class='buttonFullDiv' style='position: relative; left:0px; top: 0%; '><button id='PauseButton' class='pause' />	</div>                  ";
        return retHttp;

    @staticmethod
    def getStop():
        retHttp = "";
        retHttp += "<script type=\"text/javascript\">"
        retHttp += "$(function(){"
        retHttp += "$(\"#StopButton\").click(function(){"
        retHttp += "$.ajax({"
        retHttp += "type: 'get'"
        retHttp += ", url: 'Play/Stop'"
        retHttp += ", dataType : 'html'"
        retHttp += ", error : function(){"
        retHttp += "alert('fail!!');"
        retHttp += "}"
        retHttp += ", success : function(data){"
        retHttp += "window.location.href = '/Home';";
        retHttp += "}"
        retHttp += "});"
        retHttp += "})"
        retHttp += "})"
        retHttp += "</script>"
        retHttp += "	<div class='buttonDiv'><button id='StopButton' class='stop'/>	</div>                  ";
        return retHttp;

    @staticmethod
    def getSkip10():
        retHttp = "";
        retHttp += "<script type=\"text/javascript\">"
        retHttp += "$(function(){"
        retHttp += "$(\"#Skip10Button\").click(function(){"
        retHttp += "$.ajax({"
        retHttp += "type: 'get'"
        retHttp += ", url : 'Play/Skip'"
        retHttp += ", dataType : 'html'"
        retHttp += ", error : function(){"
        retHttp += "alert('fail!!');"
        retHttp += "}"
        retHttp += ", success : function(data){"
        retHttp += "}"
        retHttp += "});"
        retHttp += "})"
        retHttp += "})"
        retHttp += "</script>"
        retHttp += "	<div class='buttonDiv'><button id='Skip10Button' class='skip10'/>	</div>                      ";
        return retHttp;

    @staticmethod
    def getSkip600():
        retHttp = "";
        retHttp += "<script type=\"text/javascript\">"
        retHttp += "$(function(){"
        retHttp += "$(\"#Skip600Button\").click(function(){"
        retHttp += "$.ajax({"
        retHttp += "type: 'get'"
        retHttp += ", url: 'Play/Skip600'"
        retHttp += ", dataType : 'html'"
        retHttp += ", error : function(){"
        retHttp += "alert('fail!!');"
        retHttp += "}"
        retHttp += ", success : function(data){"
        retHttp += "}"
        retHttp += "});"
        retHttp += "})"
        retHttp += "})"
        retHttp += "</script>"
        retHttp += "	<div class='buttonDiv'><button id='Skip600Button' class='skip600'/>	</div>                  ";
        return retHttp;

    @staticmethod
    def getVolumeUp():
        retHttp = "";
        retHttp += "<script type=\"text/javascript\">"
        retHttp += "$(function(){"
        retHttp += "$(\"#VolumeUpButton\").click(function(){"
        retHttp += "$.ajax({"
        retHttp += "type: 'get'"
        retHttp += ", url: 'Play/VolumeUp'"
        retHttp += ", dataType : 'html'"
        retHttp += ", error : function(){"
        retHttp += "}"
        retHttp += ", success : function(data){"
        retHttp += "}"
        retHttp += "});"
        retHttp += "})"
        retHttp += "})"
        retHttp += "</script>"
        retHttp += "	<div class='volumeDiv'><button id='VolumeUpButton' class='volumeUp'/>	</div>              ";
        return retHttp;

    @staticmethod
    def getVolumeDown():
        retHttp = "";
        retHttp += "<script type=\"text/javascript\">"
        retHttp += "$(function(){"
        retHttp += "$(\"#VolumeDownButton\").click(function(){"
        retHttp += "$.ajax({"
        retHttp += "type: 'get'"
        retHttp += ", url: 'Play/VolumeDown'"
        retHttp += ", dataType : 'html'"
        retHttp += ", error : function(){"
        retHttp += "alert('fail!!');"
        retHttp += "}"
        retHttp += ", success : function(data){"
        retHttp += "}"
        retHttp += "});"
        retHttp += "})"
        retHttp += "})"
        retHttp += "</script>"
        retHttp += "	<div class='volumeDiv'><button id='VolumeDownButton' class='volumeDown'/>	</div>	        ";
        return retHttp;

    @staticmethod
    def getFormload():
        retHttp = "";
        retHttp += "<script>function FormLoad(){setInterval(UpdateTitle, 3000);}</script>"
        retHttp += "<script>";
        retHttp += "function UpdateTitle(){";
        retHttp += "$.ajax({"
        retHttp += "type: 'get'"
        retHttp += ", url: 'Play/CurFileName'"
        retHttp += ", dataType : 'html'"
        retHttp += ", success : function(data){"
        retHttp += "titleLabel = document.getElementById(\"TitleLabel\");";
        retHttp += "titleLabel.innerHTML=data;";
        retHttp += "}";
        retHttp += "});";
        retHttp += "};";
        retHttp += "</script>"
        return retHttp;

    @staticmethod
    def getPlayView(height = "100%", width="100%"):
        retHttp  = "";
        isVisiblePlayControl = osDefine.getPlayFileName() == "" and "none" or "visible";
        retHttp += "<div style=\"height:%s;width:%s;display:%s;\">" % (height, width, isVisiblePlayControl);

        retHttp += "<font><label>제목 : </label><label id=\"TitleLabel\">" + osDefine.getPlayFileName() + "</label></font>";

        retHttp += playView.getFormload();
        retHttp += "<body onload=\"FormLoad()\">"

        retHttp += "<div class='main' style='top:-100'>                                                                             ";
        retHttp += playView.getBack600();
        retHttp += playView.getBack10();
        retHttp += "   <div class='buttonDiv' style='position: relative;height=15%;width=15%'>"
        retHttp += playView.getRePlay();
        retHttp += playView.getPause();
        retHttp += "   </div>"
        retHttp += playView.getStop();
        retHttp += playView.getSkip10();
        retHttp += playView.getSkip600();
        retHttp += "</div>                                                                                         ";
        retHttp += "<div class='Empty20'>                                                                          ";
        retHttp += "	<label> </label>                                                                            ";
        retHttp += "</div>                                                                                         ";
        retHttp += "<div class='volumeMain'>       "
        retHttp += playView.getVolumeUp();
        retHttp += playView.getVolumeDown();
        retHttp += "</div>                                                                                         ";
        retHttp += "</body>    "
        retHttp += "</div>";
        return retHttp;

    @staticmethod
    def play(playVideo):
        #return HttpResponse(osDefine.LocalFilePath()+ "\\" + playVideo.GET["file"].replace('"',''));
        filePath = playVideo.GET.get("file", "");
        if (filePath != ""):
            osDefine.PlayFile(filePath);
        else :
            filePath = playVideo.GET.get("youtube", "");
            YoutubeView.play(filePath);
        http = "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no\" />"
        http += "<html> <script src=\"http://code.jquery.com/jquery-1.11.2.min.js\"></script>"
        http += "<Head> <link rel='stylesheet' href='/static/app/css/style.css'> </Head>";
        if(0):
            http += "Not Play Media.<p>"
        else:
            http += "<div>";
            http += playView.getPlayView();
            http += "</div>";

            http += "</html>"

        return HttpResponse(http)

    @staticmethod
    def moveVideo(keyMove):
        handle = pywinauto.findwindows.find_window(best_match=osDefine.GetPlayerName())
        app = pywinauto.application.Application().connect(handle=handle)
        app.window_().TypeKeys('{' + keyMove + '}')
        return HttpResponse("aaaaa");
