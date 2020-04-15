#-*- coding: utf-8 -*-

import os

os.environ['DISPLAY'] = ':0'

#from omxplayer.player import OMXPlayer

#import pynput
#import keyboard
from django.http import HttpResponse
import os.path
import os,sys
from ..module.osDefine import osDefine
#import pyautogui
import time
#import pywinauto
#import win32gui,win32con, time,sys
from ..module.strUtil import strUtil
#from tkinter import*
#from django.shortcuts import render_to_response
#import tkinter.messagebox
import time 
import re
from omxplayer.player import OMXPlayer
from requests import get
import urllib.parse


from .fileListView import fileListView 

class testView():
    @staticmethod
    def test(arg):
        searchUrl = "https://www.youtube.com/watch?v=SvscXx9ADbA";
        decode_VideoUrl = get(searchUrl);
        content = decode_VideoUrl.content.decode('utf-8');
        content = urllib.parse.unquote(content);
        content = content.replace("\\u0026", "&");
        reguler = re.compile("&url=https.+;");
        m = reguler.findall(content);
        videoUrl = "";
        print(content);
        return HttpResponse(content);
        for url in m[0].split("url="):
            try:
                videoUrl = url.split(",")[0].split(";")[0];
                if videoUrl.startswith("http"):
                 break;
            except:
             print("Error");
        return HttpResponse(videoUrl);
        OMXPlayer(videoUrl);
        return HttpResponse(content);



#        handle = pywinauto.findwindows.find_window(best_match='*VLC 미디어 재생기')
#        app = pywinauto.application.Application().connect(handle=handle)
#        app.window_().TypeKeys('{LEFT}')
#        os.popen('omxplayer "/home/pi/Downloads/봉오동 전투 戰鬪, The Battle Roar to Victory.2019.1080p.FHDRip.H264.AAC.mp4"'); 
'''
         localFilePath = osDefine.LocalFilePath()
         return HttpResponse(fileListView.deleteEmptyFolder());
         http = "";
         fileCount = 0;
         files = [  "[tvN] 수요일은 음악프로.E01.191002.450p-MreD.mp4	"
                    ,"그것이 알고 싶다.E1189.191102.720p-NEXT.mp4	"
                    ,"나쁜 녀석들 더 무비 THE BAD GUYS REIGN OF CHAOS.2019.1080p.FHDRip.H264.AAC.mp4	"
                    ,"백종원의 골목식당.E90.191030.720p-NEXT.mp4	"
                    ,"수요일은 음악프로.E04.191023.720p-NEXT.mp4	"
                    ,"수요일은 음악프로.E05.191030.720p-NEXT.mp4	"
                    ,"시베리아 선발대.E01.190926.720p-NEXT.mp4	"
                    ,"시베리아 선발대.E02.191003.720p-NEXT.mp4	"
                    ,"시베리아 선발대.E03.191010.720p-NEXT.mp4	"
                    ,"시베리아 선발대.E04.191017.720p-NEXT.mp4	"
                    ,"시베리아 선발대.E05.191024.720p-NEXT.mp4	"
                    ,"시베리아 선발대.E06.191031.720p-NEXT.mp4	"
                    ,"쌉니다 천리마마트.E07.191101.720p-NEXT.mp4	"
                    ,"책 읽어드립니다.E06.191029.720p-NEXT.mp4	"
                    ,"수요일은 음악프로.E02.191009.720p-NEXT/수요일은 음악프로.E02.191009.720p-NEXT.mp4	"
                    ,"수요일은 음악프로.E03.191016.720p-NEXT/수요일은 음악프로.E03.191016.720p-NEXT.mp4	"
                    ,"[tvN] 도깨비.E01-E16.720p-NEXT/[tvN] 도깨비 스페셜.170114.모든 날이 좋았다.720p-NEXT.mp4	"
                    ,"[tvN] 도깨비.E01-E16.720p-NEXT/[tvN] 도깨비.E10.161231.720p-NEXT.mp4	"
                    ,"[tvN] 도깨비.E01-E16.720p-NEXT/[tvN] 도깨비.E11.170106.720p-NEXT.mp4	"
                    ,"[tvN] 도깨비.E01-E16.720p-NEXT/[tvN] 도깨비.E12.170107.720p-NEXT.mp4	"
                    ,"[tvN] 도깨비.E01-E16.720p-NEXT/[tvN] 도깨비.E13.170113.720p-NEXT.mp4	"
                    ,"[tvN] 도깨비.E01-E16.720p-NEXT/[tvN] 도깨비.E14.170120.720p-NEXT.mp4	"
                    ,"[tvN] 도깨비.E01-E16.720p-NEXT/[tvN] 도깨비.E15.170121.720p-NEXT.mp4	"
                    ,"[tvN] 도깨비.E01-E16.720p-NEXT/[tvN] 도깨비.E16.END.170121.720p-NEXT.mp4	"
                    ,"청일전자 미쓰리.E12.191031.720p-NEXT/청일전자 미쓰리.E12.191031.720p-NEXT.mp4"];
            
         for file in files:
                http += "file : " + str(strUtil.getMatchTitle(file));
                http += "<p>";
         return HttpResponse(http); 

'''

#        pyautogui.moveTo(300,300);
#        pyautogui.keyUp('space'); 
#        pyautogui.keyDown('left');
         
#        keyboard_button = pynput.keyboard.Controller();
#        keyboard_key = pynput.keyboard.Key;

#        keyboard_button.press(pynput.keyboard.Key.space);
#        keyboard_button.release(pynput.keyboard.Key.space);
        
#        return HttpResponse(pyautogui.position())

	#@staticmethod
 #   def Next(arg):
 #       return render_to_response('app/test.html')

	
