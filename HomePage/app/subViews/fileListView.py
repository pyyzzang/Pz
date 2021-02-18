# -*- coding: utf-8 -*- 
from django.http import HttpResponse
import os
import pathlib
from ..module.osDefine import osDefine
from ..module.strUtil import strUtil
import base64
from ..module.osDefine import PlayMode
from .YoutubeView import YoutubeView
from ..Data.PlayInfo import PlayInfos
from .playView import playView
from django.shortcuts import render
import uuid
import json
from django.core.serializers.json import DjangoJSONEncoder

class FileInfo:
    def __init__(self, filePath, dir, request):
        self.filePath = filePath
        self.dir = dir
        self.fileName, self.ext = os.path.splitext(filePath)
        
        self.encodeName = osDefine.Base64Encoding(self.getUrlPath())
        self.thumbnailId = "Thumbnail" + (self.isDirectory() and "Dir" or "File")

        self.id = str(uuid.uuid4())

        title = strUtil.getMatchTitle(self.filePath)
        if(" " == title):
            title = self.filePath
        self.title = title

        self.link = self.getLink(request)
    
    def setPlayInfo(self, playInfo):
        self.playInfo = playInfo
    def __lt__(self, other):
        return self.getTitle() < other.getTitle() 
    def getFileName(self):
        return self.fileName
    def getFullName(self):
        return self.dir + "/" + self.filePath
    def getExt(self):
        return self.ext
    def getTitle(self):
        return self.title
    def isVideoFile(self):
        return self.getExt() in osDefine.SupportExt
    def isDirectory(self):
        return os.path.isdir(self.getFullName())
    def visibleDeleteButton(self):
        return "" == self.filePath and "Hidden" or ""
    def getThumbNailId(self):
        return self.thumbnailId
    def getEncodingFileName(self):
        return osDefine.Base64Encoding(self.getUrlPath())
    def getUrlPath(self):
        if(-1 != self.dir.find(osDefine.LocalFilePath())):
            return self.dir.replace(osDefine.LocalFilePath(), '') + self.filePath
        return self.filePath
    def getLink(self, request):
        if("" == self.filePath):
            localFilePath = osDefine.LocalFilePath()
            parentPath = self.dir.replace(localFilePath, "")
            splitParentPath = os.path.split(parentPath)[0]
            osDefine.Logger("splitParentPath : " + splitParentPath)
            
            osPath = osDefine.Base64Encoding(splitParentPath)
            if("/" != splitParentPath):
                return "location.href='" + osDefine.getRunIp(request) + "/Home?file=" + osPath + "'"
            return "location.href='" + osDefine.getRunIp(request) + "/Home'"
        if True == self.isDirectory() :
            return "location.href='" + osDefine.getRunIp(request) + "/Home?file="+ self.getEncodingFileName() + "'"
        else:
            return "location.href='" + osDefine.getRunIp(request) + "/Play?file=" + self.getEncodingFileName() + "'"

class fileListView(object):

    @staticmethod
    def GetFileList(request):
        requestFolder = osDefine.getParameter(request, "file")
        if(None == requestFolder):
            requestFolder = ""
        requestFolder = osDefine.Base64Decoding(requestFolder)
        osDefine.Logger("requestFolder : " + requestFolder)
        fileItems = fileListView.getVideoList(requestFolder, request)
        dumpString = json.dumps(fileItems, indent=4, default=lambda o: o.__dict__)
        return dumpString

    @staticmethod
    def getViewList(request):

        if("" == osDefine.YoutubeToken):
            retHttp = "<script>window.location.href='" + osDefine.getRunIp(request) + "/YoutubeRedirect'</script>"
            osDefine.Logger(retHttp)
            return HttpResponse(retHttp)

        fileListView.deleteEmptyFolder()
        try:
            requestFile = osDefine.Base64Decoding(request.GET["file"])
            osDefine.Logger("requestFile : " + requestFile)
        except Exception:
            requestFile = ""
        fileItems = fileListView.getVideoList(requestFile, request)
        context = playView.getPlayViewContext("200px", "70%")
        context["fileItmes"] = fileItems
        context["CPUTemp"] = osDefine.CPUTempStr()
        return render(request, "fileListView.html", context)
    
    @staticmethod
    def getVideoList(dirPath, request):
        localFilePath = osDefine.LocalFilePath()
        fileCount = 0      
        fileInfoList = [] 
        findDir = localFilePath + dirPath + "/"
        infos = PlayInfos.GetPlayInfos()
        for file in os.listdir(findDir):
                info = FileInfo(file, findDir, request)
                if(True == info.isVideoFile() or True == info.isDirectory()):
                    fileInfoList.append(info)
                    logInfo = infos.getPlayInfo(file)
                    if("" != logInfo):
                        osDefine.Logger(logInfo.getProgressValue())
                    info.setPlayInfo(infos.getPlayInfo(info.getUrlPath()))
        fileInfoList.sort()

        if( "" != dirPath):
            parentInfo = FileInfo("", findDir, request)
            fileInfoList.insert(0,parentInfo)
        return fileInfoList
    
    @staticmethod
    def deleteEmptyFolder():
        baseDir = osDefine.LocalFilePath()

        deleteFolder = ""
        for subItem in os.listdir(baseDir):
            checkItem = baseDir + "/" + subItem
            if(True == os.path.isdir(checkItem)):
                if(True == osDefine.checkEmpty(checkItem)):
                    os.system("sudo rm -r \"" + checkItem + "\"")

    @staticmethod
    def delete(request):
        try:
            decodingFileName = osDefine.Base64Decoding(request.GET.get("fileName"))
            filePath = osDefine.LocalFilePath() + decodingFileName
            deleteCmd = "sudo rm '%s'" % filePath
            if(True == os.path.isdir(filePath)):
                deleteCmd = "%s -R" % deleteCmd
            
            osDefine.Logger("Delete Cmd : " + deleteCmd)
            os.system(deleteCmd)
        except Exception as e:
            osDefine.Logger(e)
        return HttpResponse(deleteCmd)