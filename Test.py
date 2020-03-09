#-*- coding:utf-8 -*-


import sys

import pyodbc
server ="pyyzzang.database.windows.net";
database = "RaspberryPi";
username = "pyyzzang";
password = "cndwn5069()";
driver = "{FreeTDS}";
connectString = "DRIVER="+driver+";SERVER="+server+";PORT=1433;DATABASE="+database + ";UID="+username+";PWD="+ password + ";Encrypt=yes;Connection Timeout=30;TDS_Version=7.0";
#connectString = "Driver={FreeTDS};Server=pyyzzang.database.windows.net,1433;Database=RaspberryPi;Uid=pyyzzang;Pwd=cndwn5069();Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;TDS_Version=7.4;";
print(connectString);
cnxn = pyodbc.connect(connectString);
cursor = cnxn.cursor();
cursor.execute("select * from Title");
rows = cursor.fetchall();
for row in rows:
    t = row[0];
    t = t.encode('ISO-8859-1')
    t = t.decode('euc-kr')
    print(t);
'''

str = u'\xc7\xd1\xb1\xdb';


strb = str.encode("euc-kr");
ustr = b'\xa4\xa1\xa4\xa1';
print(ustr.decode("euc-kr"));


class FileInfo:
    def __init__(self, filePath, dir):
        self.filePath = filePath;
        self.dir = dir;
        self.fileName, self.ext = os.path.splitext(filePath);
    def __lt__(self, other):
        return self.getTitle() < other.getTitle(); 
    def getFileName(self):
        return self.fileName;
    def getFullName(self):
        return self.dir + "/" + self.filePath;
    def getExt(self):
        return self.ext;

    def getTitle(self):
        title = strUtil.getMatchTitle(self.filePath);
        if(" " == title):
            title = self.filePath;
        return title;
    def isVideoFile(self):
        return self.getExt() in osDefine.SupportExt;
    def isDirectory(self):
        return os.path.isdir(self.getFullName());
    def getEncodingFileName(self):
        return osDefine.Base64Encoding(self.getUrlPath());
    def getUrlPath(self):
        if(-1 != self.dir.find(osDefine.LocalFilePath())):
            return self.dir.replace(osDefine.LocalFilePath(), '') + '/' + self.filePath;
        return self.filePath;

import os;
import sys;

base = "/home/pi/Downloads";
for fileName in os.listdir(base):
    info = FileInfo(fileName, base);
    print("Thumbnail" + (True and "Dir" or "File"));
    if(True == info.isDirectory()):
        print(info.filePath);

'''
