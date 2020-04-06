#-*- coding: utf-8-*-

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate("/home/pi/Pz/FireBase/macro-aurora-227313-firebase-adminsdk-eq075-137ba0b44f.json")
default_app = firebase_admin.initialize_app(cred)


# This registration token comes from the client FCM SDKs.
registration_token = 'eIy_nFNUkhc:APA91bGlblPjjRsRgwz2Ez2GF07wNt5P9UpiBEvDIiKxR2tWXpJucausB4fk_skuEBBXi3NM_S19LufFRfg8KWMNUuFaokhcCb4HP_o2MgIK_r43T08vJg2NA6O-QqAcKTb3VJNkA1-B'

# See documentation on defining a message payload.
message = messaging.Message(
    token=registration_token,
    notification = messaging.Notification(
        title = "제목",
        body = "Python test body",
    )
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)
