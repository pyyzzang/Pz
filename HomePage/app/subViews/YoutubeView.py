from typing import List
from requests import get
import json
from ..module.osDefine import osDefine

from  requests import get;
import json;
import re;
from ..Data.YoutubeVideo import videos;
from ..Data.YoutubeVideo import PlayerResponse;
from ..Data.YoutubeVideo import YoutubeMp4_itag;

class YoutubeRoot(object):
    def __init__(self, assets, attrs, args):
        self.assets = assets;
        self.attrs = attrs;
        self.args = args;

    def Test():
        youtubeStr = get("https://www.youtube.com/watch?v=2hafAgIlR1Y");
        baseYoutube = youtubeStr.text.encode("utf-8");
        scripts = baseYoutube.split("ytplayer.config =");
        config = scripts[1].split(";ytplayer.load =")[0];
  
        jsonString = YoutubeRoot(**json.loads(config.decode('utf-8')));
        print(jsonString.args["player_response"]);
        root = PlayerResponse(**json.loads(jsonString.args["player_response"]));
        print(root);

class YoutubeView:
    @staticmethod
    def getTableHead():
        retHttp  = '				<table id="YoutubeTable">                                                         ';
        retHttp += '					<thead>                                                     ';
        retHttp += '						<tr class="table100-head">                              ';
        retHttp += '							<th class="column1"></th>                       ';
        retHttp += '							<th class="column2"></th>                   ';
        retHttp += '							<th class="column3">제목</th>                       ';
        retHttp += '						</tr>                                                   ';
        retHttp += '					</thead>                                                    ';
        retHttp += '                    <tbody>                                                     ';
        return retHttp;

    @staticmethod
    def getVideoList():
        retHttp = YoutubeView.getTableHead();
        for (videoItem) in YoutubeView.getYoutubeVideos():
            retHttp +="<tr>"
            retHttp +="<td class='column1'><img src=\"" + videoItem["snippet"]["thumbnails"]["default"]["url"] + "\"/></td>";
            retHttp +="<td class='column2'>" + videoItem["id"] + "</td>";
            retHttp +="<td class='column3'><a href=Play\?youtube="+ osDefine.Base64Encoding(videoItem["id"]) + ">" + videoItem['snippet']['title'] + "</td>"
            retHttp +="</tr>";
        retHttp +="</table>";
        return retHttp;
    
    @staticmethod
    def getYoutubeVideos():
        searchUrl = "https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&part=snippet&key=AIzaSyBdo9wdVW-g0b57kN4rrATTY7PHNs8ytR8&regionCode=kr";

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
        for format in root.streamingData["adaptiveFormats"]:
            if((format["itag"] in YoutubeMp4_itag)):
                if("" == retFormat or YoutubeMp4_itag[retFormat["itag"]] < YoutubeMp4_itag[format["itag"]]):
                    retFormat = format;
        return retFormat;