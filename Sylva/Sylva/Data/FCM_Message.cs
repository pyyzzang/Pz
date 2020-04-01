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
using Newtonsoft.Json;
using Sylva.Util;

namespace Sylva.Data
{
    public class FCM_Message
    {
        
        private string _Title = string.Empty;
        private string _Body = string.Empty;

        [JsonProperty(PropertyName = "Title")]
        public string Title { get { return _Title; } set { _Title = value; } }
        [JsonProperty(PropertyName = "Body")]
        public string Body { get { return _Body; } set { _Body = value; } }
        public FCM_Message(string __title, string __body)
        {
            Title = __title;
            Body = __body;
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
            using (StreamWriter sw = new StreamWriter(FileHelper.MsgListFilePath))
            {
                string saveJsonString = JsonConvert.SerializeObject(FCM_List._fcm_List);
                sw.WriteLine(saveJsonString);
            }
        }
    }
}