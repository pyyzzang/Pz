from django.http import HttpResponse
import os.path
import os,sys
from .osDefine import osDefine
import pyautogui
import time
import pywinauto
#import win32gui,win32con, time,sys

#from tkinter import*
#from django.shortcuts import render_to_response
#import tkinter.messagebox


class testView():
    @staticmethod
    def test(arg):
        handle = pywinauto.findwindows.find_window(best_match='*VLC 미디어 재생기')
        app = pywinauto.application.Application().connect(handle=handle)
        app.window_().TypeKeys('{LEFT}')
        
        return HttpResponse("E:\\Temp\\1.mp4")

	#@staticmethod
 #   def Next(arg):
 #       return render_to_response('app/test.html')

	