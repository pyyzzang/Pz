#-*- coding:utf-8 -*-
from django.http import HttpResponse

from ..module.DBExecute import DBExecute;
import datetime;
import base64;
import os;
import subprocess;
from ..module.osDefine import osDefine;
from ..module.DBExecute import SQLalchemy;
from ..FCM.FCM import FCM;
from urllib.parse import unquote

from ..Data.TorrentInfo import TorrentInfos;
from ..Data.TorrentInfo import torrentInfo;
from django.shortcuts import render;
from ..Data.TorrentData import TorrentData;
from ..Data.TorrentData import RowEnum;


class torrent:

    @staticmethod
    def torrentRemoteAdd(magnetUrl, title):
        osDefine.Logger("Title : " + title);
        TorrentInfos.updateTorrentInfo(title);

        addCmd = "sudo transmission-remote -a \"" + magnetUrl + "\" -n \"pi\":\"cndwn5069()\" -s";
        if (False == osDefine.IsWorkTime()):
            addCmd = "sudo transmission-remote -a \"" + magnetUrl + "\" -n \"pi\":\"cndwn5069()\" -S";
        osDefine.Logger("ExecuteCommand : " + addCmd);
        os.system(addCmd);
        return addCmd;

    @staticmethod
    def torrentAdd(request):
        try:
            magnetUrl = request.POST.get("magnetUrl").strip();
            magnetUrl = osDefine.Base64Decoding(magnetUrl);
            title = request.POST.get("title").strip();
            addCmd = torrent.torrentRemoteAdd(magnetUrl, title);
        except Exception as e:
            osDefine.Logger(e);
        return HttpResponse(addCmd);
    @staticmethod
    def TorrentDelete(request):
        osDefine.Logger("TorrentDelete(+)");
        magnetUrl = request.POST.get("magnetUrl").strip();
        #magnetUrl = osDefine.Base64Decoding(magnetUrl);
        osDefine.Logger("MagnetUrl : " + magnetUrl);
        connection = DBExecute.GetDBConnection();
        deleteQuery = ("delete from Torrent where magnetUrl='%s'" % magnetUrl);
        osDefine.Logger("Delete Query : " + deleteQuery);
        connection.InsertQueryExecute(deleteQuery);
        return HttpResponse("");
    @staticmethod
    def torrentInsert(request, title, magnet, genre = 99):
        try:
            tmpTorrentFile = os.path.join(osDefine.getRunDir(), "HomePage/app/static/Tmp/LastUpload.Torrent");
            fileBinary = request.FILES["torrent_files"];
            f = open(tmpTorrentFile, 'wb+');
            for chunk in fileBinary.chunks():
                f.write(chunk)
            f.close();
            
            torrentUrl = "magnet-link " + osDefine.getRunIp(request) + "/static/Tmp/LastUpload.Torrent";
            magnetUrl = subprocess.check_output(torrentUrl, shell = True).decode("utf-8");
            Binary = magnetUrl.replace("\n", "");
            base64Magnet = osDefine.Base64Encoding(Binary);
            if( True == os.path.isfile(tmpTorrentFile)):
                os.system("sudo rm " + tmpTorrentFile);

        except Exception as ex:
            Binary = "";
        
        if "" == Binary:
            Binary = magnet;
            base64Magnet = osDefine.Base64Encoding(Binary);
        
        session = DBExecute.GetDBConnection();
        query = "select * from Torrent where magnetUrl='%s'" % (base64Magnet);
        osDefine.Logger("selectQuery : " + query);
        rows = session.QueryExecute(query);
        row = rows.fetchone();
        if None != row:
            osDefine.Logger("rows.cursor.arraysize : " + str(rows.cursor.arraysize));
            osDefine.Logger("Equals Torrent Exists " + row[0]);
            return HttpResponse("<script> location.href='" + osDefine.getRunIp(request) + "/Torrent'</script>");

        query = "insert into Torrent (Title, MagnetUrl, modifyDate, ThumbnailImage, genre) values ('%s', '%s', GETDATE(), '', %s)" % (title.replace('\'', '\'\''), base64Magnet, genre);
        session.InsertQueryExecute(query);
        osDefine.Logger("Torrent : " + query);
        return HttpResponse("<script> location.href='" + osDefine.getRunIp(request) + "/Torrent'</script>");

    @staticmethod
    def torrentUpload(request):
        Title = request.POST.get("torrentTitle");
        magnet = request.POST.get("torrent_upload_url")

        osDefine.Logger("torrentUpload_magnet : " + magnet);
        return torrent.torrentInsert(request, title=Title, magnet=magnet);

    @staticmethod
    def getTorrentTable(genre):
        session = DBExecute.GetDBConnection();
        query = "select top 100 title, MagnetUrl, modifyDate, idx from Torrent ";
        if("" != genre and None != genre):
            query += " where genre='" + genre + "'";
        query += " order by modifyDate desc";
        
        rows = session.QueryExecute(query);
        
        torrentItems = [];
        for row in rows:
            item = TorrentData.createTorrenData(row);
            torrentItems.append(item);
        return torrentItems;

    @staticmethod
    def getTorrent(request):
        value = request.GET.get("Value");
        if(None == value):
            value = request.POST.get("Value");
        context = {"items" : torrent.getTorrentTable(value)};
        context["CPUTemp"] = osDefine.CPUTempStr();
        return render(request, "TorrentView.html", context);

    @staticmethod
    def torrentUpdate(request):
        magnetUrl = request.POST.get("magnetUrl");
        title = request.POST.get("Title");

        osDefine.Logger("magnetUrl : " + magnetUrl);
        osDefine.Logger("title : " + title);

        session = DBExecute.GetDBConnection();
        updateQuery = "update Torrent set title='" + title + "' where magnetUrl='" + magnetUrl +"'";
        osDefine.Logger("UpdateQuery : " + updateQuery);
        session.InsertQueryExecute(updateQuery);
        return HttpResponse("");

    @staticmethod
    def MakeFile(fileName, name, baseUsMagnetUrl):
        
        dbConnection = DBExecute.GetDBConnection();
        #제목 업데이트
        #dbConnection.InsertQueryExecute("update Torrent set Title = '" + name + "' where Title='' and magnetUrl = '" + baseUsMagnetUrl + "'");

        #이미지 업데이트
        downloadPath = "/home/pi/Downloads";
        tmpPath = os.path.join(os.getcwd(), "app/static/app/Thumbnail");
        
        tmpThumbnailPath = os.path.join(tmpPath, fileName + ".jpg");
        osDefine.Logger("tmpThumbnailPath : " + tmpThumbnailPath);
        downloadFilePath = os.path.join(downloadPath, name);
    
        if(os.path.isfile(downloadFilePath)):
            makeThumbnail = "ffmpeg -y -i '" + downloadFilePath + "' -ss 00:00:20 -vframes 1 '" + tmpThumbnailPath + "'";
            osDefine.Logger(makeThumbnail);
            os.system(makeThumbnail);
            with open(tmpThumbnailPath, "rb") as f:
                bindata = f.read();
                utfData = str(base64.b64encode(bindata));
                updateQuery = "update Torrent set ThumbnailImage = '" + utfData + "' where DataLength(ThumbnailImage)=0 and magnetUrl = '" + baseUsMagnetUrl + "'";
                osDefine.Logger(updateQuery)
                dbConnection.InsertQueryExecute(updateQuery);

    @staticmethod
    def SMI2SRT(curPath):
        try:
            for subList in os.listdir(curPath):
                subItem = os.path.join(curPath, subList);
                if( True == os.path.isdir(subItem)):
                    torrent.SMI2SRT(subItem);
                elif(True == os.path.isfile(subItem)):
                    fileName, ext = os.path.splitext(subItem);
                    if('.smi' == ext.lower()):
                        subs = ("subs -c srt %s.smi -o %s_tmp.srt") % (fileName, fileName);
                        os.system(subs);
                        subs = ("iconv -f euc-kr -t utf8 %s_tmp.srt -o %s.srt") % (fileName, fileName);
                        os.system(subs);
            os.system("cd " + curPath);
            os.system("rm *_tmp.srt");
        except Exception as e:
            osDefine.Logger(e);

    @staticmethod
    def torrentDownloadComplete(request):
        osDefine.Logger("torrentDownloadComplete (+) " + os.getcwd());
        name = request.POST.get("name");
        magnetUrl = request.POST.get("MagnetUrl");

        osDefine.Logger("Name : " + name);
        osDefine.Logger("echo magnetUrl : " + magnetUrl);

        fileName, ext = os.path.splitext(name);
        try :
            torrent.MakeFile(fileName, name, magnetUrl);
        except Exception as e:
            osDefine.Logger("Thumbnail Create Exception");
            osDefine.Logger(e);
        osDefine.Logger("FCM.SendFireBase(name)");
        FCM.SendFireBase(msg = name + "다운로드가 완료되었습니다.");

        torrent.SMI2SRT(osDefine.LocalFilePath());
        return HttpResponse("");


    @staticmethod
    def updateEntIndex(index):
        metaName = "Ent";
        return torrent.updateTorrentIndex(index, metaName);

    @staticmethod
    def updateDocuIndex(index):
        metaName = "Docu";
        return torrent.updateTorrentIndex(index, metaName);

    @staticmethod
    def updateTvendIndex(index):
        metaName = "Tvend";
        return torrent.updateTorrentIndex(index, metaName);

    @staticmethod
    def updateDramaIndex(index):
        metaName = "drama";
        return torrent.updateTorrentIndex(index, metaName);

    @staticmethod
    def SearchTorrent(request):
        findTitle = osDefine.getParameter(request,"SearchTorrent");
        findInfo = torrentInfo(findTitle);
        connection = DBExecute.GetDBConnection();
        rows = connection.QueryExecute("select title, MagnetUrl, modifyDate, idx from Torrent");
        dicData = {};
        for row in rows:
            if True == findInfo.getSimilar(torrentInfo(row[RowEnum.Title.value].strip()), 0.4):
                dicData[row[RowEnum.MagnetUrl.value]] = TorrentData.createTorrenData(row);

        rows = connection.QueryExecute("select title, MagnetUrl, modifyDate, idx from Torrent where title like '%" + findTitle + "%'");
        for row in rows:
            if False == (row[RowEnum.MagnetUrl.value] in dicData.keys()):
                dicData[row[RowEnum.MagnetUrl.value]] = TorrentData.createTorrenData(row);
        
        torrentData = list(dicData.values());

        context = {"infos" : torrentData};
        return render(request, "SearchTorrent.html", context);
            

