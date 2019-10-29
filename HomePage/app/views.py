"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .subViews.fileListView import fileListView
from .subViews.playView import playView
from .subViews.playerMove import playerMove
from .subViews.testView import testView


def home(request):
    return fileListView.getFileList("");
def Delete(request):
    return fileListView.delete(request);

def Back600(request):
    return playerMove.Back600(request);
def Back(request):
    return playerMove.Back(request);

def Replay(request):
    return playerMove.Replay(request);
def Pause(request):
    return playerMove.Pause(request);

def Skip(request):
    return playerMove.Skip(request);
def Skip600(request):
    return playerMove.Skip600(request);

def VolumeDown(request):
    return playerMove.VolumeDown(request);
def play(request):
    return playView.play(request);
def VolumeUp(request):
    return playerMove.VolumeUp(request);
def VolumeDown(request):
    return playerMove.VolumeDown(request);
def test(request):
    return testView.test(request);
