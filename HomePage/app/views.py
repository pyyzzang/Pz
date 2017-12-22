"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .subViews.fileListView import fileListView
from .subViews.playView import playView


def home(request):
    return fileListView.getFileList("");

def play(request):
    return playView.play(request);