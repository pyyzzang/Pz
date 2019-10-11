# -*- coding: utf-8 -*-

import os
import socket
import base64
from omxplayer.player import OMXPlayer

class osDefine:
    currentPlayer = 0;
    @staticmethod
    def Skip(value):
        if(0 == osDefine.currentPlayer):
            return 0;
        osDefine.currentPlayer.set_position(osDefine.currentPlayer.position() + value);
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
    def PlayFile(playFileName):
        
        decodeByte = base64.b64decode(playFileName); 
        decodeStr = str(decodeByte, "utf-8");
        if(0 != osDefine.currentPlayer):
           return 'False';
        executeFilePath = osDefine.LocalFilePath()+ "/" + decodeStr  
#        return executeFilePath 
        osDefine.currentPlayer = OMXPlayer(executeFilePath);
        return executeFilePath;

    @staticmethod
    def GetPlayerName():
        if("nt" == os.name):
            return '\*VLC 미디어 재생기';
        else:
            return '*omxplayer';

