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
import json

class PlayMode:
    File = 0;
    Youtube = 1;
    currentMode = File;

class osDefine:
    currentPlayer = 0;
    playFileName = 0;
    @staticmethod
    def Skip(value):
        if(0 == osDefine.currentPlayer):
            return 0;
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
        osDefine.currentPlayer.play();
        
    @staticmethod
    def Pause(value):
        if(0 == osDefine.currentPlayer):
            return 0;
        osDefine.currentPlayer.pause();


    @staticmethod
    def Action(value):
        if(0 == osDefine.currentPlayer):
            return 0;
        osDefine.currentPlayer.action(value);
    @staticmethod
    def LocalFilePath():
        if("nt" == os.name):
            return "E:\Temp"
        else:
            return "/home/pi/Downloads"

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
        if(0 != osDefine.currentPlayer):
            osDefine.currentPlayer.quit();
        os.system("sudo killall -9 omxplayer")
        os.system("sudo killall -9 omxplayer.bin")
        osDefine.palyFileName = 0;
        osDefine.currentPlayer = 0;
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
    def PlayYoutube(playUrl):
        if(0 != osDefine.playFileName ):
           if(osDefine.playFileName != playUrl or 
              2 >= osDefine.getProcessCount("omxplayer")):
               osDefine.PlayerInit();
           else :
               return playUrl;
        executeFilePath = playUrl; 
        osDefine.currentPlayer = OMXPlayer(playUrl); 
        osDefine.currentPlayer.stopEvent += lambda _: osDefine.PlayerInit();
        osDefine.playFileName = playUrl; 
        return executeFilePath;
        
    @staticmethod
    def getProcessCount(processName):
        ret = subprocess.check_output('ps -ef | grep ' + processName, shell = True).decode();
        return ret.count(processName); 
    @staticmethod
    def PlayFile(playFileName):
        decodeStr = osDefine.Base64Decoding(playFileName);
        if(0 != osDefine.playFileName ):
           if(osDefine.playFileName != decodeStr or 
              2 >= osDefine.getProcessCount("omxplayer")):
               osDefine.PlayerInit();
           else :
               return decodeStr;
        executeFilePath = osDefine.LocalFilePath()+ "/" + decodeStr  
        osDefine.currentPlayer = OMXPlayer(executeFilePath);

        playInfo = PlayInfos.GetPlayInfos().getPlayInfo(decodeStr);
        
        if( "" != playInfo):
            osDefine.currentPlayer.set_position(playInfo.getPosition());
            osDefine.currentPlayer.set_volume(playInfo.getVolume());
        osDefine.currentPlayer.stopEvent += lambda _: osDefine.PlayerInit();
        osDefine.playFileName = decodeStr; 
        return executeFilePath; 

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

        osDefine.Logger("playFileName : " + str(osDefine.playFileName));
        osDefine.Logger("Position : " + str(osDefine.currentPlayer.position()));
        osDefine.Logger("Volume : " + str(osDefine.currentPlayer.volume()));

        saveInfos = PlayInfos.GetPlayInfos();
        findInfo = saveInfos.getPlayInfo(osDefine.playFileName, True);

        findInfo.setPosition(osDefine.currentPlayer.position());
        findInfo.setDuration(osDefine.currentPlayer.duration());
        findInfo.setVolume(osDefine.currentPlayer.volume());

        saveInfos.saveFile();
        return "";

