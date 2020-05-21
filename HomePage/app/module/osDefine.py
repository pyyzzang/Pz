# -*- coding: utf-8 -*-
import os
import socket
import base64
import enum
import re

from requests import get
from omxplayer.player import OMXPlayer
from requests import post;
import subprocess
import logging
from ..Data.PlayInfo import PlayInfo
from ..Data.PlayInfo import PlayInfos
from .strUtil import strUtil;
import json
import threading;
import time;
from urllib.parse import urlparse;
from ..Define import Define;
import datetime;
import smtplib
from email.mime.text import MIMEText
import os, threading
from django.http import HttpResponse

class PlayMode:
    File = 0;
    Youtube = 1;
    currentMode = File;

class osDefine:
    currentPlayer = 0;
    playFileName = 0;
    playTitle = 0;
    YoutubeToken = "";
    YoutubeClientId = '456241762082-m621opd3ej2g3kcdm0ajai5rv6h37una.apps.googleusercontent.com';
    YoutubeClientSecret = "95_SJoiXXd8f4keeHUzy8O8s";
    @staticmethod 
    def getPlayFileName():
        if(0 == osDefine.playTitle or "" == osDefine.playTitle):
            return "";
        return strUtil.getMatchTitle(osDefine.playTitle);
    @staticmethod
    def Skip(value, skipMode = 0):
        if(0 == osDefine.currentPlayer):
            return 0;
        cur = 0;
        if 0 == skipMode:
            cur = osDefine.currentPlayer.position() + value;
        elif 1 == skipMode:
            cur = value;
        osDefine.Logger("Skip : " + str(cur));
        osDefine.currentPlayer.set_position(cur);
        osDefine.CurPlayInfo.setPosition(cur);
    
    @staticmethod
    def SkipVideo(request):
        value = osDefine.getParameter(request);
        osDefine.Logger("value : " + str(value));
        try:
            skipPos = osDefine.CurPlayInfo.getVideoPos(int(value));
            osDefine.Skip(skipPos, 1);
            osDefine.PlayInfoSaveThread(currentPlayFile = osDefine.playFileName, isThread = False);
            
        except Exception as e:
            osDefine.Logger(e);

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
            return -1;
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
        osDefine.playFileName = 0;
        
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

    CurPlayInfo = "";
    @staticmethod
    def PlayInfoSaveThread(currentPlayFile, isThread = True):

        while(osDefine.playFileName == currentPlayFile):
            saveInfos = PlayInfos.GetPlayInfos();
            osDefine.CurPlayInfo = saveInfos.getPlayInfo(osDefine.playTitle, True);
            osDefine.CurPlayInfo.setPosition(osDefine.currentPlayer.position());
            osDefine.CurPlayInfo.setDuration(osDefine.currentPlayer.duration());
            osDefine.CurPlayInfo.setVolume(osDefine.currentPlayer.volume());

            if( 97 < osDefine.CurPlayInfo.getProgressValue()):
                saveInfos.removeInfo(osDefine.CurPlayInfo);
                isThread = False;

            saveInfos.saveFile();
            if(False == isThread):
                break;
            time.sleep(3);
        osDefine.CurPlayInfo = "";

    @staticmethod
    def ProgressValue(request):
        if("" == osDefine.CurPlayInfo):
            return -1;
        return HttpResponse(int(osDefine.CurPlayInfo.getProgressValue()));

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
        if -1 != os.getcwd().find('/home/pi/Pz'):
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

    

    @staticmethod
    def Init():
        logFilePath = os.path.join(Define.BASE_DIR, "log");
        folderName = datetime.datetime.now().strftime("%Y_%m_%d");
        logPath = os.path.join(logFilePath,folderName);
        if(False == os.path.exists(logPath)):
            cmd = "sudo mkdir " + logPath;
            os.system(cmd);
            os.system("sudo mv *.log " + logPath);
        
        removeDate = (datetime.datetime.now() + datetime.timedelta(days=-10)).strftime("%Y_%m_%d");
        deleteLogPath = os.path.join(logFilePath, removeDate);
        if(True == os.path.exists(deleteLogPath)):
            cmd = "sudo rm -R " + deleteLogPath;
            os.system(cmd);
    
    @staticmethod
    def getParameter(request, name):
        param = request.GET.get(name);
        if(None == param):
            param = request.POST.get(name);
        return param;
    
    @staticmethod
    def YoutubeTokenRefresh():
        if("" != osDefine.YoutubeToken):
            response = get("https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s"%osDefine.YoutubeToken);
            osDefine.Logger(response.text);
            accessToken = YoutubeValidToken(**json.loads(response.text));

            if("" != accessToken.error):
                osDefine.YoutubeToken = "";
                return;

            data = {'client_id': osDefine.YoutubeClientId, 
                'client_secret': osDefine.YoutubeClientSecret, 
                'grant_type': 'refresh_token', 
                'refresh_token': osDefine.YoutubeToken};
            
            response = post("https://accounts.google.com/o/oauth2/token", data);
            osDefine.Logger(response.text);
    
    @staticmethod
    def SaveLogFile(request):
        try:
            fileBinary = request.FILES[0];
            tmpTorrentFile = os.path.join(osDefine.getRunDir(), "HomePage/app/static/Tmp/LastUpload");
            f = open(tmpTorrentFile, 'wb+');
            for chunk in fileBinary.chunks():
                f.write(chunk)
            f.close();
        except Exception as e:
            osDefine.Logger("Exception");
            osDefine.Logger(e);
            return "Exception";
        return "Success";

    @staticmethod
    def CPUTempStr():
        temp = os.popen("vcgencmd measure_temp").readline()
        result = temp.replace("temp=","").replace("'C", "")
        return result;
    
    @staticmethod
    def CPUTemp(request):
        return HttpResponse(osDefine.CPUTempStr());



class YoutubeValidToken():
    def __init__(self, audience = "", user_id = "", scope = "", expires_in="", error="", issued_to="", access_type = ""):
        self.audience = audience ;
        self.user_id = user_id;
        self.scope = scope;
        self.expires_in = expires_in;
        self.error=error;
        self.issued_to = issued_to;
        self.access_type = access_type;

osDefine.Init();