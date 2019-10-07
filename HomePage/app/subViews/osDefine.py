import os
import socket

class osDefine:

    @staticmethod
    def LocalFilePath():
        if("nt" == os.name):
            return "C:\Temp"
        else:
            return "/home/pi/Downloads"

    @staticmethod
    def Ip():
        return socket.gethostbyname(socket.getfqdn()) + ":8000";

    @staticmethod
    def PlayerName():
        if("nt" == os.name):
            return "KMPlayer Ext";
        else:
            return "omxplayer"

    @staticmethod
    def PlayFile(playFileName):
        if("nt" == os.name):
            exec(playFileName)
        else:
           code = 'omxplayer '+ playVideo
           os.system(code)
