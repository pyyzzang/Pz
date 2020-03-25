import sys;
import os;
import base64;
import pyodbc;
from urllib.parse import unquote
#parent 이상 경로 참조가 불가 함으로 상위폴더의 module폴더를 참조에 추가함.
modulePath = os.path.join(os.path.split(os.path.split(os.getcwd())[0])[0], "app/module");
sys.path.insert(0, modulePath);

from DBExecute import DBExecute;

def Base64Encoding(utfString):
        baseByte = base64.b64encode(utfString.encode("utf-8"));
        baseStr = str(baseByte, "utf-8");
        return baseStr;

if __name__ =='__main__':
    magnetUrl, name = sys.argv[2].split('&dn=');
    print(magnetUrl);
    baseUsMagnetUrl = Base64Encoding(magnetUrl);
    name = unquote(name);

    fileName, ext = os.path.splitext(name);

    dbConnection = DBExecute.GetDBConnection();

    #제목 업데이트
    #dbConnection.InsertQueryExecute("update Torrent set Title = '" + name + "' where Title='' and magnetUrl = '" + baseUsMagnetUrl + "'");
    
    #이미지 업데이트
    downloadPath = "/home/pi/Downloads";
    tmpPath = os.path.join(os.path.split(os.getcwd())[0], "static/app/Thumbnail");
    tmpThumbnailPath = os.path.join(tmpPath, fileName + ".jpg");
    downloadFilePath = os.path.join(downloadPath, name);
    if(os.path.isfile(downloadFilePath)):
        makeThumbnail = "ffmpeg -i '" + downloadFilePath + "' -ss 00:00:20 -vframes 1 '" + tmpThumbnailPath + "'";
        print(makeThumbnail);
        #os.system(makeThumbnail);
        with open(tmpThumbnailPath, "rb") as f:
            bindata = f.read();
            utfData = str(base64.b64encode(bindata), "utf-8");
            dbConnection.InsertQueryExecute("update Torrent set ThumbnailImage = '" + utfData + "' where DataLength(ThumbnailImage)=0 and magnetUrl = '" + baseUsMagnetUrl + "'");

