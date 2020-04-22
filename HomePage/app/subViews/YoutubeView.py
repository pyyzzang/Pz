from typing import List
from requests import get
import json
from ..module.osDefine import osDefine
from ..module.Youtube_Cipher import Cipher;
from django.http import HttpResponse

from  requests import get;
import json;
import re;
from ..Data.YoutubeVideo import videos;
from ..Data.YoutubeVideo import YoutubeRoot;
from ..Data.YoutubeVideo import PlayerResponse;
from ..Data.YoutubeVideo import YoutubeMp4_itag;
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from ..Data.YoutubeVideo import Items;


class YoutubeView:
    @staticmethod
    def getTableHead():
        retHttp  = '				<table id="YoutubeTable">                                                         \n';
        retHttp += '					<thead>                                                     \n';
        retHttp += '						<tr class="table100-head">                              \n';
        retHttp += '							<th class="column1"></th>                       \n';
        retHttp += '							<th class="column2"></th>                   \n';
        retHttp += '							<th class="column3">제목</th>                       \n';
        retHttp += '						</tr>                                                   \n';
        retHttp += '					</thead>                                                    \n';
        retHttp += '                    <tbody>                                                     \n';
        return retHttp;
    @staticmethod
    def getSearchView():
        retHttp = "";
        retHttp += "<input type='text' id='txtSearch' />\n";
        retHttp += "<input type='button' id='btnSearch' value='검색'/>\n";
        retHttp += "<script type='text/javascript'>\n";
        retHttp += "$(function(){\n"
        retHttp += "$(\"#btnSearch\").click(function(){\n"
        retHttp += "searchValue = document.getElementById('txtSearch').value;\n"
        retHttp += "jsonData = {'API' : 'SearchYoutube', 'Value' : searchValue};\n";
        retHttp += "$.ajax({\n"
        retHttp += "type: 'get'\n"
        retHttp += ", url: '/API'\n";
        retHttp += ", dataType : 'html'\n";
        retHttp += ", data:jsonData\n";
        retHttp += ", error : function(request,status,error){\n"
        retHttp += "alert(request);\n";
        retHttp += "alert(status);\n";
        retHttp += "alert(error);\n";
        retHttp += "}\n"
        retHttp += ", success : function(data){\n"
        retHttp += "alert('11 : ' + data);\n";
        retHttp += "}\n"
        retHttp += "});\n"
        retHttp += "})\n"
        retHttp += "})\n"
        retHttp += "</script>\n"
        return retHttp;

    @staticmethod
    def getVideoTable(searchUrl = "https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&part=snippet&key=AIzaSyBdo9wdVW-g0b57kN4rrATTY7PHNs8ytR8&regionCode=kr"):
        retHttp = YoutubeView.getTableHead();
        for (videoItem) in YoutubeView.getYoutubeVideos(searchUrl):
            retHttp +="<tr>"
            retHttp +="<td class='column1'><img src=\"" + videoItem["snippet"]["thumbnails"]["default"]["url"] + "\"/></td>";
            retHttp +="<td class='column2'>" + Items.getVideoId(videoItem) + "</td>";
            retHttp +="<td class='column3'><a href=Play\?youtube="+ osDefine.Base64Encoding(Items.getVideoId(videoItem)) + ">" + videoItem['snippet']['title'] + "</td>"
            retHttp +="</tr>";
        retHttp +="</table>";
        return retHttp;

    @staticmethod
    def getVideoList():
        retHttp =  YoutubeView.getSearchView();
        retHttp += YoutubeView.getVideoTable();
        return retHttp;
    
    @staticmethod
    def getYoutubeVideos(searchUrl):

        downloadString = get(searchUrl);
        decoded_videos = videos(**json.loads(downloadString.content.decode('utf-8')));
        return decoded_videos.items;
    @staticmethod
    def play(youtubeId):
        youtubeId = osDefine.Base64Decoding(youtubeId);
        playFormat = YoutubeView.getPlayUrl(youtubeId);
        osDefine.PlayYoutube(playFormat["url"]);
    
    @staticmethod
    def getPlayUrl(youtubeId):
        youtubeStr = get("https://www.youtube.com/watch?v=" + youtubeId);
        baseYoutube = youtubeStr.text;
        scripts = baseYoutube.split("ytplayer.config =");
        config = scripts[1].split(";ytplayer.load =")[0];
  
        jsonString = YoutubeRoot(**json.loads(config));
        root = PlayerResponse(**json.loads(jsonString.args["player_response"]));
        retFormat = "";
        for format in root.streamingData["formats"]:
            if((format["itag"] in YoutubeMp4_itag)):
                osDefine.Logger("Itag : " + str(format["itag"]));
                if(22 == format["itag"]):
                    osDefine.Logger("itag 22 Return");
                    return format;
                if("" == retFormat or YoutubeMp4_itag[retFormat["itag"]] < YoutubeMp4_itag[format["itag"]]):
                    retFormat = format;
        
        jsPath = "https://youtube.com" + jsonString.assets["js"];
        if("url" not in retFormat.keys()):
            retFormat["url"] = Cipher.getCipher(retFormat["cipher"], jsPath);

        return retFormat;

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
    def getSearchYoutube(searchValue):
        try:
            searchUrl = "https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyBdo9wdVW-g0b57kN4rrATTY7PHNs8ytR8&regionCode=kr&q=%s" % searchValue;
            retHttp = YoutubeView.getVideoTable(searchUrl)
            osDefine.Logger(retHttp);
        except Exception as e:
            osDefine.Logger(e);
        return HttpResponse(retHttp);
