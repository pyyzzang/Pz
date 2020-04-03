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
    }
}