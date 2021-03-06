from typing import List
from requests import get
import json
from ..module.osDefine import osDefine
from ..module.Youtube_Cipher import Cipher
from django.http import HttpResponse
from enum import Enum

from  requests import get
import requests
import json
import re
from ..Data.YoutubeVideo import videos
from ..Data.YoutubeVideo import Item
from ..Data.YoutubeVideo import YoutubeRoot
from ..Data.YoutubeVideo import PlayerResponse
from ..Data.YoutubeVideo import YoutubeMp4_itag
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from ..Data.YoutubeToken import AccessToken
from django.shortcuts import render

class YoutubeSearchType(Enum):
    Search = 0
    MostPopular = Search + 1
    Activities = MostPopular + 1
    Subscript = Activities + 1
    

    @staticmethod
    def getTypeUrl(type, token):
        typeDict = {
            YoutubeSearchType.Search: "https://www.googleapis.com/youtube/v3/search?part=snippet&regionCode=kr&q=%s",
            YoutubeSearchType.MostPopular: "https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&part=snippet&regionCode=kr&maxResults=50",
            YoutubeSearchType.Activities: "https://www.googleapis.com/youtube/v3/activities?regionCode=KR&part=contentDetails,snippet&home=true&maxResults=50",
            YoutubeSearchType.Subscript: "Search"}
        return typeDict[type] + "&access_token=" + token


class YoutubeView:
    
    @staticmethod
    def getYoutubeVideos(searchUrl):
        downloadString = get(searchUrl)
        decoded_videos = videos(**json.loads(downloadString.content.decode('utf-8')))
        retList = []
        for item in decoded_videos.items:
            addItem = Item.getItem(item)
            retList.append(addItem)
        return retList
    @staticmethod
    def play(youtubeId, title):
        youtubeId = osDefine.Base64Decoding(youtubeId)
        playFormat = YoutubeView.getPlayUrl(youtubeId)
        osDefine.PlayYoutube(playFormat["url"], title)
    
    @staticmethod
    def getPlayUrl(youtubeId):
        youtubeStr = get("https://www.youtube.com/watch?v=" + youtubeId)
        baseYoutube = youtubeStr.text
        scripts = baseYoutube.split("ytplayer.config=")[1].strip()

        index = 0
        count = 0
        while(True):
            if('{' == scripts[index]):
                count = 1
                index + 1
                break
        index = index + 1
        osDefine.Logger("count(+) : " + str(count))
        while(index < len(scripts)):
            if('{' == scripts[index]):
                count = count + 1
            elif('}' == scripts[index]):
                count = count - 1
            if(0 == count):
                break
            index = index + 1

        config = scripts[0:index + 1]
        osDefine.Logger("config : " + str(config))

        jsonString = YoutubeRoot(**json.loads(config))
        root = PlayerResponse(**json.loads(jsonString.args["player_response"]))
        retFormat = ""
        for format in root.streamingData["formats"]:
            if((format["itag"] in YoutubeMp4_itag)):
                osDefine.Logger("Itag : " + str(format["itag"]))
                if(22 == format["itag"]):
                    osDefine.Logger("itag 22 Return")
                    return format
                if("" == retFormat or YoutubeMp4_itag[retFormat["itag"]] < YoutubeMp4_itag[format["itag"]]):
                    retFormat = format
        
        jsPath = "https://youtube.com" + jsonString.assets["js"]
        if("url" not in retFormat.keys()):
            try:
                retFormat["url"] = Cipher.getCipher(retFormat["cipher"], jsPath)
            except Exception as e:
                retFormat["url"] = Cipher.getCipher(retFormat["signatureCipher"], jsPath)

        return retFormat

    @staticmethod
    def youtube_search(options):

        videos = []
        channels = []
        playlists = []

        # Add each result to the appropriate list, and then display the lists of
        # matching videos, channels, and playlists.
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                       search_result["id"]["videoId"]))
            elif search_result["id"]["kind"] == "youtube#channel":
                channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                         search_result["id"]["channelId"]))
            elif search_result["id"]["kind"] == "youtube#playlist":
                playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                          search_result["id"]["playlistId"]))
        print ("Videos:\n", "\n".join(videos), "\n")
        print ("Channels:\n", "\n".join(channels), "\n")
        print ("Playlists:\n", "\n".join(playlists), "\n")

    @staticmethod
    def SearchYoutube(request):
        try:
            searchValue = osDefine.getParameter(request, "Value")
            #osDefine.Logger("searchValue : " + searchValue)
            searchUrl = "https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyAgScQJA23SuzIbwP3zmDfuSJ4plmRk13M&regionCode=kr&q=%s" % searchValue
            osDefine.Logger("searchUrl : " + searchUrl)
            youtubeItems = YoutubeView.getYoutubeVideos(searchUrl)
            context = {"YoutubeItems" : youtubeItems}
            return render(request, "YoutubeViewTable.html", context)
        except Exception as e:
            osDefine.Logger(e)
        return HttpResponse("")

    @staticmethod
    def Redirect(request):
        code = ""
        try:
            code = request.GET.get("code")
            if(True):            
                oAuthUrl = "https://accounts.google.com/o/oauth2/auth?client_id=%s&redirect_uri=%s/YoutubeRedirect&response_type=code&scope=https://www.googleapis.com/auth/youtube" % (osDefine.YoutubeClientId, osDefine.getRunIp(request))
                http = "<script>location.href=\"" + oAuthUrl + "\"</script>"
                return HttpResponse(http)
            
            osDefine.Logger("Code : " + str(code))
            data = {'code': code, 
                'client_id': osDefine.YoutubeClientId, 
                'client_secret': osDefine.YoutubeClientSecret, 
                'grant_type': 'authorization_code', 
                'redirect_uri': '%s/YoutubeRedirect' % osDefine.getRunIp(request)}
            res = requests.post("https://accounts.google.com/o/oauth2/token", data=data)
            acceseToken = AccessToken(**json.loads(res.text))
            osDefine.YoutubeToken = acceseToken.access_token
            
            osDefine.Logger("res.text : " + res.text)
            osDefine.Logger("osDefine.YoutubeToken : " + osDefine.YoutubeToken)

            redirectUrl = osDefine.getRunIp(request)

            return HttpResponse("<script>location.href=\"" + redirectUrl + "\"</script>")

        except Exception as e:
            osDefine.Logger(e)
        return HttpResponse(code)