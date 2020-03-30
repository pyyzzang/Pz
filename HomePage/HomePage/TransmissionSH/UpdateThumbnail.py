import sys;
import os;
import base64;
import pyodbc;
from urllib.parse import unquote
#parent 이상 경로 참조가 불가 함으로 상위폴더의 module폴더를 참조에 추가함.
modulePath = os.path.join(os.path.split(os.path.split(os.getcwd())[0])[0], "app/module");
sys.path.insert(0, modulePath);

from DBExecute import DBExecute;

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

def Base64Encoding(utfString):
        baseByte = base64.b64encode(utfString.encode("utf-8"));
        baseStr = str(baseByte, "utf-8");
        return baseStr;

class SendCompleteMessage:
    @staticmethod
    def SendFireBase(sendmessage):
        cred = credentials.Certificate("/home/pi/Pz/FireBase/macro-aurora-227313-firebase-adminsdk-eq075-137ba0b44f.json")
        firebase_admin.initialize_app(cred)

        # This registration token comes from the client FCM SDKs.
        registration_token = 'eIy_nFNUkhc:APA91bGlblPjjRsRgwz2Ez2GF07wNt5P9UpiBEvDIiKxR2tWXpJucausB4fk_skuEBBXi3NM_S19LufFRfg8KWMNUuFaokhcCb4HP_o2MgIK_r43T08vJg2NA6O-QqAcKTb3VJNkA1-B'

        # See documentation on defining a message payload.
        message = messaging.Message(
            token=registration_token,
            notification = messaging.Notification(
                title = "다운로드 완료",
                body = sendmessage + "다운로드가 종료되었습니다.",
            )
        )
    
        # Send a message to the device corresponding to the provided
        # registration token.
        response = messaging.send(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)



if __name__ =='__main__':
    splitArg = sys.argv[2].split('&');

    magnetUrl = "";
    name = "";
    for arg in splitArg:
        if(True == arg.startswith("magnet:?")):
            magnetUrl = arg;
        elif(True == arg.startswith("dn=")):
            name = arg.replace("dn=", "");

    print("magnetUrl : " + magnetUrl);
    print("Name : " + name);
    baseUsMagnetUrl = Base64Encoding(magnetUrl);
    name = unquote(name);

    fileName, ext = os.path.splitext(name);

 
    SendCompleteMessage.SendFireBase(name);


        
    
    

        

