#-*- coding: utf-8-*-

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
from datetime import datetime;


cred = credentials.Certificate("/home/pi/Pz/FireBase/macro-aurora-227313-firebase-adminsdk-eq075-137ba0b44f.json")
default_app = firebase_admin.initialize_app(cred)


# This registration token comes from the client FCM SDKs.
registration_token = 'dTeyQCMuMxI:APA91bHY0EVD-JK7ZO6LLzhPNq_qjv5aNijxM35BKSe7WmPFpNb2l26ckZkp4vmUipHyyqgDsCx6lQUO2EK5QgPX4kbNlnUDvAmJq_I_S_y5FOZIevDF9DlCxk3RR4SiMSTM0R-_07oL'

# See documentation on defining a message payload.
message = messaging.Message(
    token=registration_token,
    data={
        "Title" : "제목",
        "Content" : "몸통",
        "Time" : datetime.now().strftime("%y.%m.%d %H:%M:%S"),
    },
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)
