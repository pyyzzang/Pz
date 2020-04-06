from django.http import HttpResponse;
import os;
from ..module.DBExecute import SQLalchemy;
from ..module.osDefine import osDefine

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

class FCM:
    @staticmethod
    def RegisterToken(request):
        id = request.POST.get("id");
        token = request.POST.get("token");
        
        connection = SQLalchemy.GetDBConnection();
        try:
            insertQuery = ("insert into UserInfo values('%s' , '%s')")% (id, token);
            osDefine.Logger(insertQuery);
            connection.InsertQueryExecute(insertQuery)            
        except:
            osDefine.Logger("insert Error");
        
        updateQuery = ("update UserInfo set token='%s' where id='%s'")% (token, id);
        osDefine.Logger(updateQuery);
        connection.InsertQueryExecute(updateQuery)            
        
        return HttpResponse("");
    
    @staticmethod
    def SendFireBase(sendmessage):
        try:
            cred = credentials.Certificate("/home/pi/Pz/FireBase/macro-aurora-227313-firebase-adminsdk-eq075-137ba0b44f.json")
            firebase_admin.initialize_app(cred)
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
                notification = messaging.Notification(
                    title = "다운로드 완료",
                    body = sendmessage + "다운로드가 완료되었습니다.",
                ),
                data={
                    "Title" : "다운로드 완료",
                    "Content" : sendmessage + "다운로드가 완료되었습니다.",
                },
            )
        except Exception as e:
            osDefine.Logger(e);
    
        # Send a message to the device corresponding to the provided
        # registration token.
        response = messaging.send(message)
        # Response is a message ID string.
        osDefine.Logger('Successfully sent message:', response)