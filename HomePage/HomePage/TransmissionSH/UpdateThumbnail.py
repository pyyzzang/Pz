import sys;
import base64;
import os;
from urllib.parse import unquote
import urllib.parse
import urllib.request



def getIsDev():
    if True == os.getcwd().startswith('/home/pi/Pz/HomePage') : 
        return True;
    return False;

def getRunIp():
    if(True == getIsDev()):
        return "http://192.168.219.102:8000"
    return "http://192.168.219.102:80"

def Base64Encoding(utfString):
    baseByte = base64.b64encode(utfString.encode("utf-8"));
    baseStr = str(baseByte, "utf-8");
    return baseStr;

def Write(log):
    os.system("echo " + log + " >> Bach.log");

if __name__ =='__main__':
    splitArg = sys.argv[2].split('&');

    magnetUrl = "";
    name = "";
    for arg in splitArg:
        if(True == arg.startswith("magnet:?")):
            magnetUrl = arg;
        elif(True == arg.startswith("dn=")):
            name = arg.replace("dn=", "");

    Write("echo magnetUrl : " + magnetUrl);
    Write("Name : " + name);
    baseUsMagnetUrl = Base64Encoding(magnetUrl);
    name = unquote(name);

    test_url = getRunIp() + "/Torrent/TorrentDownloadComplete";
    data = urllib.parse.urlencode({"name" : name, "MagnetUrl" : baseUsMagnetUrl});
    req = urllib.request.Request(test_url, data=data.encode("utf-8"))
    response = urllib.request.urlopen(req)
    result =  response.read().decode("utf-8")
    