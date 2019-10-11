import os
import socket
import pyautogui

class osDefine:

    currentPlayer;

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
        executeFilePath = "\""+osDefine.LocalFilePath()+ "\\" + playFileName + "\""
        if("nt" != os.name):
           executeFilePath = 'omxplayer '+ executeFilePath;
        os.popen(executeFilePath)

    @staticmethod
    def GetPlayerName():
        if("nt" == os.name):
            return '*VLC 미디어 재생기';
        else:
            return '*omxplayer';

