using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using Firebase.Messaging;
using Newtonsoft.Json;
using Sylva.Util;

namespace Sylva.Data
{

    public class Notification
    {
        private string _Title = string.Empty;
        private string _Body = string.Empty;

        [JsonProperty(PropertyName = "Title")]
        public string Title { get { return _Title; } set { _Title = value; } }
        [JsonProperty(PropertyName = "Body")]
        public string Body { get { return _Body; } set { _Body = value; } }
        public Notification(string __title, string __body)
        {
            Title = __title;
            Body = __body;
        }
    }

    public class Data
    {
        public Data(IDictionary<string,string> __data)
        {
            _Data = __data;
        }
        private IDictionary<string, string> _Data = null;

        [JsonProperty(PropertyName = "Title")]
        public string Title
        {
            get
            {
                return _Data["Title"];
            }
        }
        [JsonProperty(PropertyName = "Body")]
        public string Body
        {
            get
            {
                return _Data["Body"];
            }
        }
    }

    public class FCM_Message
    {
        public FCM_Message(RemoteMessage __remoteMessage) 
        {
            //Notification = new Notification(__remoteMessage.GetNotification().Title, __remoteMessage.GetNotification().Body);
            Data = new Data(__remoteMessage.Data);
        }
        
        [JsonProperty(PropertyName = "Notification")]
        public Notification Notification { get; set; }
        [JsonProperty(PropertyName = "Data")]
        public Data Data { get; set; }
    }

    public class FCM_List : ObservableCollection<FCM_Message>
    {
        private static FCM_List _fcm_List= null;
        public static FCM_List GetFCMList()
        {
            if (null == _fcm_List)
            {
                if (true == File.Exists(FileHelper.MsgListFilePath))
                {
                    using (StreamReader sw = new StreamReader(FileHelper.MsgListFilePath))
                    {
                        try
                        {
                            string readJsonString = sw.ReadLine();
                            Newtonsoft.Json.Linq.JArray jArray = (Newtonsoft.Json.Linq.JArray)JsonConvert.DeserializeObject(readJsonString);
                            FCM_List._fcm_List = jArray.ToObject<FCM_List>();

                        }
                        catch(Exception e)
                        {
                            _fcm_List = new FCM_List();
                        }
                    }
                }
                else
                {
                    _fcm_List = new FCM_List();
                }
            }
            return _fcm_List;
        }

        public void SaveFile()
        {
            using (StreamWriter sw = new StreamWriter(FileHelper.MsgListFilePath))
            {
                string saveJsonString = JsonConvert.SerializeObject(FCM_List._fcm_List);
                sw.WriteLine(saveJsonString);
            }
        }
    }
}