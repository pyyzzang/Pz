import os

class osDefine:
    
    @staticmethod
    def LocalFilePath():
        if("nt" == os.name):
            return "C:\Temp"
        else:
            return "/home/pi/Downloads"

    @staticmethod
    def Ip():
        if("nt" == os.name):
            return "http://localhost:8000"
        else:
            return "192.168.219.105:8000"

    @staticmethod
    def PlayFile(playFileName):
        #if("nt" == os.Name):
            exec(playFileName)
        #else:
         #   code = 'omxplayer '+ playVideo
          #  os.system(code) # 터미널에 입력