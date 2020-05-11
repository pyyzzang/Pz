from django.http import HttpResponse;
import os;
from ..module.DBExecute import SQLalchemy;
from ..module.osDefine import osDefine
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
from datetime import datetime;
import time;
import threading;
import uuid

class FCM:
    @staticmethod
    def RegisterToken(request):
        id = request.POST.get("id");
        token = request.POST.get("token");
        
        connection = SQLalchemy.GetDBConnection();
        try:
            insertQuery = ("delete UserInfo where id='%s'")% (id);            
            osDefine.Logger(insertQuery);
            connection.InsertQueryExecute(insertQuery)            
            osDefine.Logger(insertQuery);
        except:
            osDefine.Logger("insert Error");
        
        updateQuery = ("insert into UserInfo values('%s' , '%s')")% (id, token);
        osDefine.Logger(updateQuery);
        connection.InsertQueryExecute(updateQuery)            
        
        return HttpResponse("");

    cred = "";
    @staticmethod
    def SendFireBaseThread():
        if("" == FCM.cred):
            FCM.cred = credentials.Certificate("/home/pi/Pz/FireBase/macro-aurora-227313-firebase-adminsdk-eq075-137ba0b44f.json");
            firebase_admin.initialize_app(FCM.cred);

        connection = SQLalchemy.GetDBConnection();
        query = "select info.token, fcm.Title, fcm.Content, fcm.SendTime, fcm.MsgGUID from FCM as fcm, UserInfo as info where fcm.Id = info.id;";
        rows = connection.QueryExecute(query);
        osDefine.Logger(query);

        if(0 == rows.rowcount):
            return "";

        for row in rows:
            try:
                # See documentation on defining a message payload.
                message = messaging.Message(
                    token=row[0].strip(),
                    data={
                        "Title" : row[1].strip(),
                        "Content" : row[2].strip(),
                        "Time" : row[3].strip(),
                        "MsgGUID" : row[4].strip(),
                    },
                )

                # Send a message to the device corresponding to the provided
                # registration token.
                response = messaging.send(message);
                osDefine.Logger(response);
            except Exception as e:
                osDefine.Logger(e);
    @staticmethod
    def SendFireBase(msg, title = "다운로드 완료"):
        try:
            connection = SQLalchemy.GetDBConnection();
            query = "insert into FCM values ('%s', '%s', '%s', '%s', '%s')" % ("1", title, msg, datetime.now().strftime("%Y.%m.%d %H:%M:%S"), str(uuid.uuid4()));
            connection.InsertQueryExecute(query);
        except Exception as e:
            osDefine.Logger(e);

    @staticmethod
    def SendFireBaseTest(msg, title = "다운로드 완료"):
        try:
            if "" == FCM.cred :
                FCM.cred = credentials.Certificate("/home/pi/Pz/FireBase/macro-aurora-227313-firebase-adminsdk-eq075-137ba0b44f.json");
                firebase_admin.initialize_app(FCM.cred);
            # This registration token comes from the client FCM SDKs.
            connection = SQLalchemy.GetDBConnection();
            query = "select token from UserInfo where id='1'";
            osDefine.Logger(query);
            rows = connection.QueryExecute(query);
            registration_token = str(rows.fetchone()[0]);
            osDefine.Logger('sent message Token :' + registration_token)
            registration_token = registration_token.strip();
            
            # See documentation on defining a message payload.
            message = messaging.Message(
                token=registration_token,
                # notification = messaging.Notification(
                #     title = "다운로드 완료",
                #     body = sendmessage + "다운로드가 완료되었습니다.",
                # ),
                data={
                    "Title" : title,
                    "Content" : msg,
                    "Time" : datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
                },
            )
        except Exception as e:
            osDefine.Logger(e);
    
        # Send a message to the device corresponding to the provided
        # registration token.
        response = messaging.send(message)

    @staticmethod
    def UpdateMsgStatus(value):
        connection = SQLalchemy.GetDBConnection();
        query = "delete FCM where MsgGUID='%s'" % value;
        osDefine.Logger(query);
        rows = connection.InsertQueryExecute(query);

    

