"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .subViews.fileListView import fileListView
from .subViews.YoutubeView import YoutubeView
from .subViews.playView import playView
from .subViews.playerMove import playerMove
from .subViews.torrent import torrent
from .subViews.testView import testView
from .FCM.FCM import FCM
from .module.osDefine import osDefine;
from django.http import HttpResponse
from .TorrentParse.TorrentveryParse import TorrentveryParse;

def home(request):
    return fileListView.getViewList(request);
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

def Stop(request):
    return playerMove.Stop(request);

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
def CurFileName(request):
    return playerMove.CurFileName(request);
def test(request):
    return testView.test(request);
def Torrent(request):
    return torrent.getTorrent(request);
def TorrentUpload(request):
    return torrent.torrentUpload(request);
def TorrentDownloadComplete(request):
    return torrent.torrentDownloadComplete(request);
def TorrentAdd(request):
    return torrent.torrentAdd(request);
def TorrentDelete(request):
    return torrent.TorrentDelete(request);
def TorrentUpdate(request):
    return torrent.torrentUpdate(request);
def RegisterToken(request):
    return FCM.RegisterToken(request);
def API(request):
    executeFunc = "";
    value = "";
    try:
        switcher={
            "UpdateEntIndex":torrent.updateEntIndex,
            "UpdateDocuIndex":torrent.updateDocuIndex,
            "UpdateTvendIndex":torrent.updateTvendIndex,
            "UpdateDramaIndex":torrent.updateDramaIndex,
            "CrawlingTorrent":TorrentveryParse.CrawlingTorrent,
            "SearchYoutube":YoutubeView.getSearchYoutube,
        }; 
        executeFunc = switcher.get(request.GET.get("API"));
        value = request.GET.get("Value")
    except Exception as e:
        osDefine.Logger(e);
    if("" == executeFunc):
        return HttpResponse("Error");
    return HttpResponse(executeFunc(value));
