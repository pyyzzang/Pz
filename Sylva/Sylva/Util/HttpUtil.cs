using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Text;
using Android.Views;
using Android.Widget;

namespace Sylva.Util
{
    public class HttpUtil
    {
        private static string ServerUrl
        {
            get
            {
#if DEBUG
                return "http://192.168.219.102:8000";
#else
                return "192.168.219.102:8080";
#endif
            }
        }

        private static string UpdateUserInfo
        {
            get
            {
                return string.Format("{0}/RegisterToken", ServerUrl);
            }
        }

        public static string SendMessage(bool __isPost = true, System.Collections.Specialized.NameValueCollection __param = null)
        {
            WebClient client = new WebClient();
            byte[] downloadByte = client.UploadValues(UpdateUserInfo, __isPost ? "POST" : "GET", __param);
            return Encoding.UTF8.GetString(downloadByte);
        }
    }
}