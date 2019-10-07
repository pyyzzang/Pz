from django.http import HttpResponse
import os.path
import os,sys
from .osDefine import osDefine
#import win32gui,win32con, time,sys

#from tkinter import*
#from django.shortcuts import render_to_response
#import tkinter.messagebox


class testView():
    @staticmethod
    def test(arg):
        return HttpResponse(osDefine.Ip())

	#@staticmethod
 #   def Next(arg):
 #       return render_to_response('app/test.html')

	