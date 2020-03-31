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
using Sylva.Util;

namespace Sylva.Data
{
    [Serializable]
    public class FCM_Message: Java.Lang.Object
    {
        private string _Title = string.Empty;
        public string Title { get { return _Title; } set { _Title = value; } }
        public string _Body = string.Empty;
        public string Body { get { return _Body; } set { _Body = value; } }
        public FCM_Message(string __title, string __body)
        {
            Title = __title;
            Body = __body;
        }
    }

    [Serializable]
    public class FCM_List : ObservableCollection<FCM_Message>
    {
        [System.ComponentModel.Localizable(false)]
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
                            BinaryFormatter serializer = new BinaryFormatter();
                            _fcm_List = (FCM_List)serializer.Deserialize(sw.BaseStream);
                        }catch(Exception e)
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
                BinaryFormatter serializer = new BinaryFormatter();
                serializer.Serialize(sw.BaseStream, _fcm_List);
            }
        }
    }
}