# -*- coding: utf-8 -*-

import os
import socket
import base64
import enum
import re

from requests import get
from omxplayer.player import OMXPlayer
from requests import get
import subprocess
import logging
from ..Data.PlayInfo import PlayInfo
from ..Data.PlayInfo import PlayInfos
from .strUtil import strUtil;
import json
import threading;
import time;
from urllib.parse import urlparse

class PlayMode:
    File = 0;
    Youtube = 1;
    currentMode = File;

class osDefine:
    currentPlayer = 0;
    playFileName = 0;
    playTitle = 0;
    @staticmethod 
    def getPlayFileName():
        if(0 == osDefine.playTitle or "" == osDefine.playTitle):
            return "";
        return strUtil.getMatchTitle(osDefine.playTitle);
    @staticmethod
    def Skip(value):
        if(0 == osDefine.currentPlayer):
            return 0;
        osDefine.Logger("Skip : " + str(value));
        osDefine.currentPlayer.set_position(osDefine.currentPlayer.position() + value);
    

    SupportExt = ['.mp4', '.mkv', '.avi'];
    NotDeleteExt = SupportExt + ['.part'];
    @staticmethod
    def checkEmpty(basePath):
        for subItem in os.listdir(basePath):
            subItemPath = basePath + "/" + subItem;
            if(True == os.path.isdir(subItemPath)):
                if(False == osDefine.checkEmpty(subItemPath)):
                    return False;
            else :
                path, ext = os.path.splitext(subItemPath);
                if(True == (ext in osDefine.NotDeleteExt)):
                    return False;
        return True;
    @staticmethod
    def Replay(value):
        if(0 == osDefine.currentPlayer):
            return 0;
        osDefine.Logger("Replay ");
        osDefine.currentPlayer.play();
        
    @staticmethod
    def Pause(value):
        if(0 == osDefine.currentPlayer):
            return 0;
        osDefine.Logger("Pause");
        osDefine.currentPlayer.pause();


    @staticmethod
    def Action(value):
        if(0 == osDefine.currentPlayer):
            return 0;
        osDefine.Logger("Action : " + str(value));
        osDefine.currentPlayer.action(value);
    @staticmethod
    def LocalFilePath():
        if("nt" == os.name):
            return "E:\Temp"
        else:
            return "/home/pi/Downloads/"

    @staticmethod
    def Ip():
        if("nt" == os.name):
            return socket.gethostbyname(socket.getfqdn()) + ":8000"
        else:
            return "192.168.219.102:8000"

    @staticmethod
    def PlayerName():
        if("nt" == os.name):
            return "KMPlayer Ext";
        else:
            return "omxplayer"
    @staticmethod
    def PlayerInit():
        osDefine.Logger("PlayerInit");
        if(0 != osDefine.currentPlayer):
            try:
                osDefine.currentPlayer.quit();
            except Exception as e:
                osDefine.Logger(e);
            
        os.system("sudo killall -9 omxplayer")
        os.system("sudo killall -9 omxplayer.bin")
        osDefine.palyFileName = 0;
        osDefine.currentPlayer = 0;
        osDefine.playTitle = 0;
        
    @staticmethod
    def Base64Encoding(utfString):
        baseByte = base64.b64encode(utfString.encode("utf-8"));
        baseStr = str(baseByte, "utf-8");
        return baseStr;

    @staticmethod
    def Base64Decoding(convString):
        utfByte = base64.b64decode(convString, ' /');
        utfStr = str(utfByte, "utf-8");
        return utfStr;

    @staticmethod
    def PlayYoutube(playUrl, title):
        return osDefine.PlayFile(playUrl, isDecode=False, isYoutube = True, title=title);
        
    @staticmethod
    def getProcessCount(processName):
        ret = subprocess.check_output('ps -ef | grep ' + processName, shell = True).decode();
        return ret.count(processName); 
    @staticmethod
    def PlayFile(playFileName , isDecode = True, isPause = True, isYoutube = False, title = ""):
        if(True == isDecode):
            decodeStr = osDefine.Base64Decoding(playFileName);
        else:
            decodeStr = playFileName;
        if(0 != osDefine.playFileName ):
           if(osDefine.playFileName != decodeStr or 
              2 >= osDefine.getProcessCount("omxplayer")):
               osDefine.PlayerInit();
           else :
               return decodeStr;
        executeFilePath = isYoutube and decodeStr or (osDefine.LocalFilePath() + "/" + decodeStr);
        osDefine.Logger("executeFilePath : " + executeFilePath);
        if(0 != osDefine.currentPlayer):
            osDefine.currentPlayer.quit();

        osDefine.currentPlayer = OMXPlayer(executeFilePath, pause=True);
        
        osDefine.playFileName = decodeStr; 
        if(True == isYoutube):
            osDefine.playTitle = title;
        else:
            osDefine.playTitle = osDefine.playFileName;
            
        osDefine.Logger("title : " + title);
        osDefine.Logger("osDefine.playTitle : " + osDefine.playTitle);
        osDefine.currentPlayer.stopEvent += lambda _: osDefine.PlayerInit();
        osDefine.currentPlayer.exitEvent += lambda _, exit_code: osDefine.ExitEvent(exit_code)
        
        osDefine.currentPlayer.playEvent += lambda _: osDefine.PlayerPlay();
        osDefine.currentPlayer.play();
        
        saveThread = threading.Thread(target=osDefine.PlayInfoSaveThread, args=(osDefine.playFileName,));
        saveThread.start();

        return executeFilePath; 

    @staticmethod
    def PlayInfoSaveThread(currentPlayFile):

        while(osDefine.playFileName == currentPlayFile):
            saveInfos = PlayInfos.GetPlayInfos();
            findInfo = saveInfos.getPlayInfo(osDefine.playTitle, True);

            findInfo.setPosition(osDefine.currentPlayer.position());
            findInfo.setDuration(osDefine.currentPlayer.duration());
            findInfo.setVolume(osDefine.currentPlayer.volume());

            saveInfos.saveFile();
            time.sleep(3);

    @staticmethod 
    def playNextVideo():
        playFilePath = osDefine.playFileName;
        fileDir, fileName = os.path.split(playFilePath);
        if("/" == fileDir):
            return 0;

        findDir = osDefine.LocalFilePath() + fileDir;
        nextFile = "";
        findFile = False;
        fileTuple = os.listdir(findDir);
        fileTuple.sort();
        for file in fileTuple:
            osDefine.Logger("File : " + file);
            if(True == findFile):
                nextFile = file;
                break;
            if(file == fileName):
                findFile = True;
        
        if(True == findFile):
            nextPlayFile = os.path.join(fileDir, nextFile);
            osDefine.PlayFile(nextPlayFile, False, False);

    @staticmethod
    def ExitEvent(exit_status):
        osDefine.Logger("ExitEvent : " + str(exit_status));
        if( 0 == exit_status or 1 == exit_status):
            osDefine.playNextVideo();

    @staticmethod
    def PlayerPlay():
        playInfo = PlayInfos.GetPlayInfos().getPlayInfo(osDefine.playTitle);
        osDefine.Logger("PlayerPlay : " + str(osDefine.playTitle));
        
        if( "" != playInfo):
            if( playInfo.getPosition() + 10 < playInfo.getDuration()):
                osDefine.currentPlayer.set_position(playInfo.getPosition());
            
            osDefine.currentPlayer.set_volume(playInfo.getVolume());

    @staticmethod
    def GetPlayerName():
        if("nt" == os.name):
            return '\*VLC 미디어 재생기';
        else:
            return '*omxplayer';
    @staticmethod
    def Logger(msg):
        return logging.getLogger("HomePage").info(msg);

    @staticmethod
    def Stop(request):
        try:
            osDefine.Logger("Stop");
            osDefine.PlayerInit();
        except Exception as e:
            osDefine.Logger(e);
        return "";
    
    @staticmethod
    def getIsDev():
        if '/home/pi/Pz/HomePage' == os.getcwd() : 
            return True;
        return False;

    @staticmethod
    def getRunIp(request = None):
        try:
            url = urlparse(request.build_absolute_uri());
            return "%s://%s" % (url.scheme, url.netloc);
        except Exception as e:
            osDefine.Logger(e);
            if(True == osDefine.getIsDev()):
                return "https://192.168.219.102:8080"
            return "https://192.168.219.102"
    @staticmethod
    def getRunDir():
        if(True == osDefine.getIsDev()):
            return "/home/pi/Pz/"
        return "/home/pi/Sylva/Pz/"

    

