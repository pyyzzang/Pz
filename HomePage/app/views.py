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
from .subViews.Settings import Settings
from .FCM.FCM import FCM
from .module.osDefine import osDefine
from django.http import HttpResponse
from .TorrentParse.TorrentveryParse import TorrentveryParse
from .TorrentParse.TorrentSir5Parse import TorrentSir5Parse

from .Data.TorrentInfo import TorrentInfos

import inspect;

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

def YoutubeRedirect(request):
    return YoutubeView.Redirect(request);

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
def Setting(request):
    return Settings.ShowPopup(request);
def SearchTorrent(request):
    return torrent.SearchTorrent(request);
def LogFile(request):
    return HttpResponse(osDefine.SaveLogFile(request));

def API(request):
    executeFunc = "";
    value = "";
    try:
        switcher={
            "SearchYoutube":YoutubeView.SearchYoutube,
            "SendFCM":FCM.SendFireBase,
            "UpdateMsgStatus":FCM.UpdateMsgStatus,
            "ProgressValue":osDefine.ProgressValue,
            "SkipVideo":osDefine.SkipVideo,
            "DeleteTorrentInfo":TorrentInfos.DeleteTorrentInfo,
            "CPUTemp":osDefine.CPUTemp,
            "GetVideoList":fileListView.GetFileList,
        }; 
        executeFunc = switcher.get(request.GET.get("API"));
    except Exception as e:
        osDefine.Logger(e);
    if("" == executeFunc):
        return HttpResponse("Error");
    retValue = executeFunc(request);
    if(True == isinstance(retValue, HttpResponse)):
        return retValue;
    return HttpResponse(retValue);
