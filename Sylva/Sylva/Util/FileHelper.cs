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
    public class FileHelper
    {
        public static string MsgListFilePath
        {
            get
            {
                return Path.Combine(Android.App.Application.Context.DataDir.AbsolutePath, "MsgList");
            }
        }

        public static string LogPath
        {
            get
            {
                return Path.Combine(Android.App.Application.Context.DataDir.AbsolutePath, string.Format("%s_Log.log", DateTime.Now.ToString("yyyy_MM_dd")));
            }
        }
    }
}