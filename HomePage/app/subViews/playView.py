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
        http = "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no\" />"
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
            http += ", url: 'Play/Back600'"
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
            http += ", url: 'Play/Back'"
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
            http += ", url: 'Play/Replay'"
            http += ", dataType : 'html'"
            http += ", error : function(){"
            http += "}"
            http += ", success : function(data){"
            http += "replayDiv = document.getElementById('Replay');"
            http += "pauseDiv = document.getElementById('Pause');"
            http += "replayDiv.style.visibility='hidden';"
            http += "pauseDiv.style.visibility='visible';"
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
            http += ", url: 'Play/Pause'"
            http += ", dataType : 'html'"
            http += ", error : function(){"
            http += "alert('fail!!');"
            http += "}"
            http += ", success : function(data){"
            http += "replayDiv = document.getElementById('Replay');"
            http += "pauseDiv = document.getElementById('Pause');"
            http += "replayDiv.style.visibility='visible';"
            http += "pauseDiv.style.visibility='hidden';"
            http += "}"
            http += "});"
            http += "})"
            http += "})"
            http += "</script>"
            
            #Stop
            http += "<script type=\"text/javascript\">"
            http += "$(function(){"
            http += "$(\"#StopButton\").click(function(){"
            http += "$.ajax({"
            http += "type: 'get'"
            http += ", url: 'Play/Stop'"
            http += ", dataType : 'html'"
            http += ", error : function(){"
            http += "alert('fail!!');"
            http += "}"
            http += ", success : function(data){"
            http += "window.location.href = '/Home';";
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
            http += ", url : 'Play/Skip'"
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
            http += ", url: 'Play/Skip600'"
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
            http += ", url: 'Play/VolumeUp'"
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
            http += ", url: 'Play/VolumeDown'"
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

            http += "<div class='main' style='top:-100'>                                                                             ";
            http += "	<div class='buttonDiv'><button id='Back600Button' class='back600'/>	</div>                  ";
            http += "	<div class='buttonDiv'><button id='Back10Button' class='back10'/>	</div>                      ";
            http += "   <div class='buttonDiv' style='position: relative;height=15%;width=15%'>"
            http += "	    <div id='Replay' class='buttonFullDiv' style='position: relative;left:0px; top: 100%; visibility:hidden'><button id='ReplayButton' class='play' /> </div>                     ";
            http += "	    <div id='Pause' class='buttonFullDiv' style='position: relative; left:0px; top: 0%; '><button id='PauseButton' class='pause' />	</div>                  ";
            http += "   </div>"
            http += "	<div class='buttonDiv'><button id='StopButton' class='stop'/>	</div>                  ";
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
