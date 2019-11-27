from django.http import HttpResponse
import os
import pathlib
from .osDefine import osDefine
from .strUtil import strUtil
import base64

class fileListView(object):
    @staticmethod
    def getFileList(ext):
        http = "<http>"

        http += "<script src=\"http://code.jquery.com/jquery-1.11.2.min.js\"></script>"
        http += "<table border='1'> " 

        
        localFilePath = osDefine.LocalFilePath()
        ip = osDefine.Ip()
        fileCount = 0;       
        for (path, dir, files) in os.walk(localFilePath):
            files.sort();
            for file in files:

                fileName, ext = os.path.splitext(file);
                if(".mp4" != ext and ".mkv" != ext and ".avi" != ext):
                    continue;
                if(-1 != path.find(localFilePath)):
                     file = path.replace(localFilePath,'') + '/' + file;


                fileCount = fileCount + 1;
                http += "<tr>"
 
                fileStr = osDefine.Base64Encoding(file);
                http = http + "<td> <a href=Play\?file="+ str(fileStr) + ">" + strUtil.getMatchTitle(file) + "</a></td>"
                http = http + "<td><button id=File" + str(fileCount) + " >삭제</button>"
                http += "</tr>"
                http += "<script type=\"text/javascript\">";
                http += "$(function(){" 
                http += "$(\"#File"+str(fileCount)+"\").click(function(){"
                http += "if(false == confirm('"+ strUtil.getMatchTitle(file) + "을 삭제 하시겠습니까?')){return;}"
                http += "$.ajax({"
                http += "type:'get'"
                http += ",url:'Home/Delete'"
                http += ",dataType:'html'"
                http += ",data:{'fileName':'"+fileStr+"'}"
                http += ",error : function(data){"
                http += "alert(data);"
                http += "}"
                http += ", success : function (data){"
                http += "alert(data)}})})})</script>"
        http += "</table>"
        http = http + "</http>"
        return HttpResponse(http)

    @staticmethod
    def delete(request):
        deleteFile = osDefine.Base64Decoding(request.GET["fileName"]);
        splitPath = deleteFile.split('/',2);
        if(3 == len(splitPath)):
#          os.popen('(sudo chown pi "' + osDefine.LocalFilePath() + "/" + splitPath[1] +"\"");
          os.system('sudo chown pi "' + osDefine.LocalFilePath() + "/" + splitPath[1] +"\"");
#          return HttpResponse('sudo chown pi \"' + osDefine.LocalFilePath() + "/" + splitPath[1]+"\"");

        deleteFullPath = (osDefine.LocalFilePath() + "/" + deleteFile)    
#        return HttpResponse(deleteFullPath);
        if(False == os.path.exists(deleteFullPath)):
            return HttpResponse("");
        os.remove(deleteFullPath);
        return HttpResponse(deleteFullPath);

