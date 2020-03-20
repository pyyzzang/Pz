# -*- coding: utf-8 -*- 
from django.http import HttpResponse
import os
import pathlib
from ..module.osDefine import osDefine
from ..module.strUtil import strUtil
import base64
from ..module.osDefine import PlayMode;
from .YoutubeView import YoutubeView;

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
    def getThumbNailId(self):
        return "Thumbnail" + (self.isDirectory() and "Dir" or "File");
    def getEncodingFileName(self):
        return osDefine.Base64Encoding(self.getUrlPath());
    def getUrlPath(self):
        if(-1 != self.dir.find(osDefine.LocalFilePath())):
            return self.dir.replace(osDefine.LocalFilePath(), '') + '/' + self.filePath;
        return self.filePath;
    def getLink(self):
        if("" == self.filePath):
            return "<a href=http://192.168.219.102:8000/Home>Parent</a>";
        if True == self.isDirectory() :
            return "<a href=Home\?file="+ self.getEncodingFileName() + ">" + self.getTitle() + "</a>";
        else:
            return "<a href=Play\?file="+ self.getEncodingFileName() + ">" + self.getTitle() + "</a>";

    def getTr(self, fileCount):
        retHttp  = "<tr>";
        retHttp += "<td class='column1' id='" + self.getThumbNailId() + "'></td>";
        retHttp += "<td class='column2' id='" + self.getLink() + "'>" + self.getLink() + "</td>";
        retHttp += "<td class='column2' id='deleteButton'>" + "<button id=File" + str(fileCount) + " >삭제</button>" + " </td>";
        retHttp += "</tr>";
        retHttp += "<script type=\"text/javascript\">";
        retHttp += "$(function(){" 
        retHttp += "$(\"#File"+str(fileCount)+"\").click(function(){"
        retHttp += "if(false == confirm('"+ self.getTitle() + "을 삭제 하시겠습니까?')){return;}"
        retHttp += "$.ajax({"
        retHttp += "type:'get'"
        retHttp += ",url:'Home/Delete'"
        retHttp += ",dataType:'html'"
        retHttp += ",data:{'fileName':'"+self.getEncodingFileName()+"'}"
        retHttp += ",error : function(data){"
        retHttp += "alert(data);"
        retHttp += "}"
        retHttp += ", success : function (data){"
        retHttp += "alert(data);"
        retHttp += "}})})})</script>"

        return retHttp;

class fileListView(object):
    @staticmethod
    def getViewList(request):
        fileListView.deleteEmptyFolder();
        try:
            deleteFile = osDefine.Base64Decoding(request.GET["file"]);
        except Exception:
            deleteFile = "";
        http = fileListView.getHeader();
        http += fileListView.getTitleHead();

        http += fileListView.getBodyHead();

        http += fileListView.getVideoList(deleteFile);
        http += YoutubeView.getVideoList();

        http += fileListView.getBodyTail();
        http += "</body>";
        return HttpResponse(http); 
    @staticmethod
    def getTitleHead():
        retHttp  = '<body Onload="FormLoad()">';
        retHttp += '<input name="ViewType" id="FileRadio" Value="File" type="radio" OnChange="RadioChecked(this)"> 파일 </input>';
        retHttp += '<input name="ViewType" Value="Youtube" type="radio" OnChange="RadioChecked(this)" >Youtube</input>';
        retHttp += "<script>";
        retHttp += "function FormLoad(){"
        retHttp += "    document.getElementById('FileRadio').checked = true;"
        retHttp += "    RadioChecked(document.getElementById('FileRadio'));}";
        
        retHttp += "function RadioChecked(radio){";
        retHttp += "if(radio.value=='File')";
        retHttp += "{";
        retHttp += '    YoutubeTable.style.visibility = "collapse";';
        retHttp += '    FileViewTable.style.visibility = "visible";';
        retHttp += '}';
        retHttp += 'else';
        retHttp += '{';
        retHttp += '    FileViewTable.style.visibility = "collapse";';
        retHttp += '    YoutubeTable.style.visibility = "visible";';
        retHttp += '}}';
        retHttp += "</script>";
        return retHttp;


    @staticmethod
    def getHeader():
        retHttp = "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no\" />";
        retHttp += "<script src=\"http://code.jquery.com/jquery-1.11.2.min.js\"></script>"
        retHttp += ' <head>																												';
        retHttp += ' 	<meta charset="UTF-8">                                                                                          ';
        retHttp += ' 	<meta name="viewport" content="width=device-width, initial-scale=1">                                            ';
        retHttp += ' <!--===============================================================================================-->	            ';
        retHttp += ' 	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>                                             ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">                           ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">                ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">                                       ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">                                   ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">                   ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="/static/app/css/util.css">                                                     ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="/static/app/css/main.css?version=1.2">                                                     ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="/static/app/css/style.css">                                                     ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += '                                                                                                                     ';
        retHttp += ' <!--===============================================================================================-->	            ';
        retHttp += ' 	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>                                                       ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<script src="vendor/bootstrap/js/popper.js"></script>                                                           ';
        retHttp += ' 	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>                                                    ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<script src="vendor/select2/select2.min.js"></script>                                                           ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<script src="js/main.js"></script>                                                                              ';
        retHttp += '                                                                                                                     ';
        retHttp += ' </head>                                                                                                             ';
        return retHttp;

    @staticmethod
    def getBodyHead():
        retHttp = '<div class="limiter">                                                           ';
        retHttp += '	<div class="container-table100">                                            ';
        retHttp += '		<div class="wrap-table100">                                             ';
        retHttp += '			<div class="table100">                                              ';
        return retHttp;

    @staticmethod
    def getBodyTail():
        retHttp  = '			</div class="table100">                                              ';
        retHttp += '		</div class="wrap-table100">                                             ';
        retHttp += '	</div class="container-table100">                                            ';
        retHttp += '</div class="limiter">                                                           ';
        return retHttp;

    @staticmethod
    def getTableHead():
        retHttp  = '				<table id="FileViewTable">                                                         ';
        retHttp += '					<thead>                                                     ';
        retHttp += '						<tr class="table100-head">                              ';
        retHttp += '							<th class="column1"></th>                       ';
        retHttp += '							<th class="column2">제목</th>                   ';
        retHttp += '							<th class="column3"></th>                       ';
        retHttp += '						</tr>                                                   ';
        retHttp += '					</thead>                                                    ';
        retHttp += '                    <tbody>                                                     ';
        return retHttp;
    @staticmethod
    def getTableTail():
        return "</tbody></table>";

    @staticmethod
    def getVideoList(dirPath):
        localFilePath = osDefine.LocalFilePath()
        ip = osDefine.Ip()
        fileCount = 0;      
        fileInfoList = []; 
        findDir = localFilePath + "/" + dirPath;
        for file in os.listdir(findDir):
                info = FileInfo(file, findDir);
                if(True == info.isVideoFile() or True == info.isDirectory()):
                    fileInfoList.append(info);

        fileInfoList.sort();
        http = fileListView.getTableHead();
        if( "" != dirPath):
            parentInfo = FileInfo("", localFilePath);
            fileInfoList.insert(0,parentInfo);
        for info in fileInfoList:
            http += info.getTr(fileCount);
            fileCount = fileCount + 1;
        http += fileListView.getTableTail();
        
        return http;

    @staticmethod
    def delete(request):
        deleteFile = osDefine.Base64Decoding(request.GET["fileName"]);
        splitPath = deleteFile.split('/',2);
        if(3 == len(splitPath)):
          os.system('sudo chown -R pi "' + osDefine.LocalFilePath() + "/" + splitPath[1] +"\"");

        deleteFullPath = (osDefine.LocalFilePath() + "/" + deleteFile)    
        if(False == os.path.exists(deleteFullPath)):
            return HttpResponse("");
        os.remove(deleteFullPath);
        deleteEmptyFolder();
        return HttpResponse(deleteFullPath);
    @staticmethod
    def deleteEmptyFolder():
        baseDir = osDefine.LocalFilePath();

        deleteFolder = "";
        for subItem in os.listdir(baseDir):
            checkItem = baseDir + "/" + subItem;
            if(True == os.path.isdir(checkItem)):
                if(True == osDefine.checkEmpty(checkItem)):
                    os.system("sudo rm -r \"" + checkItem + "\"");
