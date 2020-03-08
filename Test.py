#-*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

print sys.stdin.encoding
print sys.stdout.encoding
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
    print(str(row[1]).encode("EUC_KR"));

