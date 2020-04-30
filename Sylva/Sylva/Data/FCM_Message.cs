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
        protected string _Date = string.Empty;
        protected string _Body = string.Empty;
        protected string _Title = string.Empty;
        protected string _MsgGUID = string.Empty;

        public FCM_Message() { }
        public FCM_Message(RemoteMessage __remoteMessage) 
        {
            if (true == __remoteMessage.Data.ContainsKey("Time"))
            {
                Date = __remoteMessage.Data["Time"];
            }
            if (true == __remoteMessage.Data.ContainsKey("Content"))
            {
                Body = __remoteMessage.Data["Content"];
            }

            if (true == __remoteMessage.Data.ContainsKey("Title"))
            {
                Title = __remoteMessage.Data["Title"];
            }
            if (true == __remoteMessage.Data.ContainsKey("MsgGUID"))
            {
                MsgGUID = __remoteMessage.Data["MsgGUID"];
            }
        }
        
        [JsonProperty(PropertyName = "Date")]
        public string Date { get { return _Date; } set { _Date = value; } }
        [JsonProperty(PropertyName = "Body")]
        public string Body{ get { return _Body; } set { _Body = value; } }
        [JsonProperty(PropertyName = "Title")]
        public string Title { get { return _Title; } set { _Title= value; } }

        private static string UpdateMsgStatus { get { return "{0}/API?API=UpdateMsgStatus"; } }
        [JsonIgnore]
        public string MsgGUID { get { return _MsgGUID; } 
            set 
            { 
                _MsgGUID = value;
                if(false == string.IsNullOrEmpty(_MsgGUID))
                {
                    System.Collections.Specialized.NameValueCollection sendValue = new System.Collections.Specialized.NameValueCollection();
                    sendValue.Add("Value", _MsgGUID);
                    HttpUtil.SendMessage(UpdateMsgStatus, true, sendValue);
                }
            } 
        }

    }

    public class FCM_List : ObservableCollection<FCM_Message>
    {
        public FCM_List()
        {

        }
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