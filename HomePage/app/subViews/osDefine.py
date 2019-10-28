# -*- coding: utf-8 -*-

import os
import socket
import base64
from omxplayer.player import OMXPlayer

class osDefine:
    currentPlayer = 0;
    playFileName = 0;
    @staticmethod
    def Skip(value):
        if(0 == osDefine.currentPlayer):
            return 0;
        osDefine.currentPlayer.set_position(osDefine.currentPlayer.position() + value);

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
    def PlayFile(playFileName):
        decodeStr = osDefine.Base64Decoding(playFileName);
        if(0 != osDefine.playFileName):
           osDefine.PlayerInit(); 
        executeFilePath = osDefine.LocalFilePath()+ "/" + decodeStr  
        osDefine.currentPlayer = OMXPlayer(executeFilePath);
        osDefine.currentPlayer.stopEvent += lambda _: osDefine.PlayerInit();
        osDefine.playFileName = executeFilePath
        return executeFilePath;

    @staticmethod
    def GetPlayerName():
        if("nt" == os.name):
            return '\*VLC 미디어 재생기';
        else:
            return '*omxplayer';

