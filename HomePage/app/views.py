"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .subViews.fileListView import fileListView
from .subViews.playView import playView
from .subViews.testView import testView


def home(request):
    return fileListView.getFileList("");

def play(request):
    return playView.play(request);

def playerMove(request):
    return playView.playerMove(request);

def test(request):
    return testView.test(request);

