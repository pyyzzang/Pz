from django.shortcuts import render;
from ..Data.TorrentInfo import TorrentInfos;
 
class Settings:
    @staticmethod
    def ShowPopup(request):
        torrentInfos = TorrentInfos.GetTorrentInfos();
        context = {"torrentInfos" : torrentInfos.infos};
        return render(request, "Settings.html",context);