using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Provider;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using Java.Lang;

namespace Sylva.Util
{
    public class Log
    {
        private bool _Init = false;
        private bool Init
        {
            get
            {
                if(false == _Init)
                {
                    _Init = true;
                    
                }
                return _Init;
            }
        }

        private Log()
        {
            Log.UploadFile();
        }



        private static string LogUploadUrl { get { return "{0}/LogFile"; } }
        private static void UploadFile()
        {
            try
            {
                HttpUtil.UploadFile(LogUploadUrl, FileHelper.LogPath);
            }catch( System.Exception e)
            {

            }

        }

        private void WriteLog(string __msg)
        {
            using (StreamWriter sw = new StreamWriter(FileHelper.LogPath, true))
            {
                sw.WriteLine(string.Format(__msg));
            }
        }

        private static Log _Instance = null;
        
        private static Log Instance
        {
            get
            {
                if (null == _Instance)
                {
                    _Instance = new Log();
                }
                return _Instance;
            }
        }

        private static object lockObj = new object();
        public static void Write(string __msg)
        {
            lock(lockObj)
            {
                Instance.WriteLog(__msg);
            }
        }
    }
}