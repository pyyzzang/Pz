#-*- coding: utf-8 -*-

import os

os.environ['DISPLAY'] = ':0'

from omxplayer.player import OMXPlayer

import pynput
import keyboard
from django.http import HttpResponse
import os.path
import os,sys
from .osDefine import osDefine
import pyautogui
import time
#import pywinauto
#import win32gui,win32con, time,sys

#from tkinter import*
#from django.shortcuts import render_to_response
#import tkinter.messagebox
import time 

class testView():
    @staticmethod
    def test(arg):
#        handle = pywinauto.findwindows.find_window(best_match='*VLC 미디어 재생기')
#        app = pywinauto.application.Application().connect(handle=handle)
#        app.window_().TypeKeys('{LEFT}')
#        os.popen('omxplayer "/home/pi/Downloads/봉오동 전투 戰鬪, The Battle Roar to Victory.2019.1080p.FHDRip.H264.AAC.mp4"'); 

         localFilePath = osDefine.LocalFilePath()
         http = "";
         fileCount = 0;
         for (path, dir, files) in os.walk(localFilePath):
            for file in files:
                if(-1 != path.find(localFilePath)):
                     file = path.replace(localFilePath,'') + '/' + file;
                    
                http += "Path : " + path;
                http += "file : " + file;
         return HttpResponse(http); 



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

	
