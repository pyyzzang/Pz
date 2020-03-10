#-*- coding:utf-8 -*-
'''
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
cursor.execute("insert into Torrent values('1111', ' ', '11', GETDATE(), 7)");
cnxn.commit();
cnxn.close();
'''
import os;
import subprocess;
import base64;
torrentUrl = "magnet-link http://192.168.219.102:8000/static/Tmp/LastUpload.Torrent";
balue = subprocess.check_output(torrentUrl, shell = True);
print(type(balue));
Binary = balue.replace("\n","");
Title = "";
Binary = base64.b64encode(Binary);
print(type(Binary));

query = "insert into Torrent values('%s', '%s', GETDATE())" % (Title, Binary);

print(query);