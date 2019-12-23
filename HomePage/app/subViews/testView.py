#-*- coding: utf-8 -*-

import os

os.environ['DISPLAY'] = ':0'

#from omxplayer.player import OMXPlayer

#import pynput
#import keyboard
from django.http import HttpResponse
import os.path
import os,sys
from .osDefine import osDefine
import pyautogui
import time
#import pywinauto
#import win32gui,win32con, time,sys
from .strUtil import strUtil
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
        url = "https://r8---sn-ab02a0nfpgxapox-jwwk.googlevideo.com/videoplayback?expire=1577098396&ei=PEgAXo__A4Pu4wKXmbbYBg&ip=49.175.165.141&id=o-AJasv4LZTrPL6F_V5MUXYERzXfPJmdHcfE2vZsOgWhdH&itag=22&source=youtube&requiressl=yes&mm=31%2C26&mn=sn-ab02a0nfpgxapox-jwwk%2Csn-npoe7n7y&ms=au%2Conr&mv=m&mvi=7&pl=19&usequic=no&initcwndbps=2391250&mime=video%2Fmp4&ratebypass=yes&dur=608.525&lmt=1576951451372172&mt=1577076698&fvip=3&fexp=23842630&c=WEB&txp=4432432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cratebypass%2Cdur%2Clmt&sig=ALgxI2wwRgIhANPGwOjfE8quHnzsiqLAKz3aptrU5ksCNp_GwrVh27-iAiEAiaKoL0VbCySVKX_JgwmerKfhI_ewobF1jxZcKk1u3i8%3D&lsparams=mm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cusequic%2Cinitcwndbps&lsig=AHylml4wRQIhAJwxqrIn6wGdxT9TCjvmz9Wtng-P6PiEj-xOUf10F6MzAiBJTqKURH5hhXkbPsoOnD1mAakuviSS3438Gxqsk_rB6Q%3D%3D";
        searchUrl = "https://www.youtube.com/watch?v=1T9RmTK3dQc";
        decode_VideoUrl = get(searchUrl);
        content = decode_VideoUrl.content.decode('utf-8');
        content = urllib.parse.unquote(content);
        content = content.replace("\\u0026", "&");
        reguler = re.compile("&url=https.+;");
        m = reguler.findall(content);
        videoUrl = "";
        for url in m[0].split("url="):
            try:
                videoUrl = url.split(",")[0].split(";")[0];
                if videoUrl.startswith("http"):
                   break;
            except E:
                print("Error");
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

	
