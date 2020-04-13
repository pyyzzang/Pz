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
using Xamarin.Essentials;

namespace Sylva.Data
{

    public class Notification
    {
        private string _Title = string.Empty;
        private string _Body = string.Empty;

        public string Title { get { return _Title; } set { _Title = value; } }
        public string Body { get { return _Body; } set { _Body = value; } }
        public Notification(string __title, string __body)
        {
            Title = __title;
            Body = __body;
        }
    }

    public class Data
    {
        public Data(IDictionary<string,string> __dataDic)
        {
            _DataDic = __dataDic;
        }
        private IDictionary<string, string> _DataDic = null;

        public IDictionary<string, string> DataDic { get { return _DataDic; } set { _DataDic = value; } }

        public string Title
        {
            get
            {
                return _DataDic["Title"];
            }
        }
        public string Body
        {
            get
            {
                return _DataDic["Body"];
            }
        }
    }

    public class FCM_Message
    {
        public FCM_Message(RemoteMessage __remoteMessage) 
        {
            if(null != __remoteMessage.GetNotification())
            {
                Notification = new Notification(__remoteMessage.GetNotification().Title, __remoteMessage.GetNotification().Body);
            }
            
            Data = new Data(__remoteMessage.Data);
        }
        
        [JsonProperty(PropertyName = "Notification")]
        public Notification Notification { get; set; }
        [JsonProperty(PropertyName = "Data")]
        public Data Data { get; set; }
        [JsonProperty(PropertyName = "Title")]
        public string Title
        {
            get
            {
                if (false == string.IsNullOrEmpty(Notification.Title))
                    return Notification.Title;
                return Data.Title;
            }
        }
        [JsonProperty(PropertyName = "Body")]
        public string Body
        {
            get
            {
                if (false == string.IsNullOrEmpty(Notification.Body))
                    return Notification.Body;
                return Data.Body;
            }
        }

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
            try
            {

                using (StreamWriter sw = new StreamWriter(FileHelper.MsgListFilePath))
                {
                    string saveJsonString = JsonConvert.SerializeObject(FCM_List._fcm_List);
                    sw.WriteLine(saveJsonString);
                }
            }
            catch (Exception e) { }
        }
    }
}