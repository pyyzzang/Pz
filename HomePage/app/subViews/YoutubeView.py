from typing import List
from requests import get
import json




class pageInfo(object):
 def __init__(self, totalResults:str, resultsPerPage:str):
  self.totalResults = totalResults;
  self.resultsPerPage = resultsPerPage;

class Item(object):
 def __init__(self, kind:str):
  self.kind = kind;

class videos(object):
 def __init__(self, kind:str, etag:str, nextPageToken:str, pageInfo:List[
pageInfo], items:List[Item]):
  self.kind = kind;
  self.etag = etag;
  self.items = items;

class YoutubeView:
 @staticmethod
 def getVideoList():
  retHttp = "";
  retHttp = "<Table id='YoutubeTable' border='1'>";
  for (videoItem) in YoutubeView.getYoutubeVideos():
   retHttp +="<tr>"
   retHttp +="<td><img src=\"" + videoItem["snippet"]["thumbnails"]["default"]["url"] + "\"/></td>";
   retHttp +="<td>" + videoItem["id"] + "</td>";
   retHttp +="<td>" + videoItem['snippet']['title'] + "</td>"
   


   retHttp +="</tr>";
  retHttp +="</table>";
  return retHttp;

 @staticmethod
 def getYoutubeVideos():
  searchUrl = "https://www.googleapis.com/youtube/v3/videos?chart=mostPopular&part=snippet&key=AIzaSyBdo9wdVW-g0b57kN4rrATTY7PHNs8ytR8&regionCode=kr";

  downloadString = get(searchUrl);
  decoded_videos = videos(**json.loads(downloadString.content.decode('utf-8')));
  return decoded_videos.items;


