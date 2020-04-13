using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;

namespace Sylva.Util
{
    public class Log
    {
        private static object lockObj = new object();
        public static void Write(string __msg)
        {
            lock(lockObj)
            {
                using (StreamWriter sw = new StreamWriter(FileHelper.LogPath, true))
                {
                    sw.WriteLine(string.Format(__msg));
                }
            }
        }
    }
}