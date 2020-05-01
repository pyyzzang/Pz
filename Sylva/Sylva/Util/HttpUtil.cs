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
                return "https://192.168.219.102";
            }
        }

        public static string SendMessage(string __Url, bool __isPost = true, System.Collections.Specialized.NameValueCollection __param = null)
        {
            ServicePointManager.ServerCertificateValidationCallback += (sender, certificate, chain, sslPolicyErrors) => true;
            WebClient client = new WebClient();
            byte[] downloadByte = client.UploadValues(string.Format(__Url, ServerUrl), __isPost ? "POST" : "GET", __param);
            return Encoding.UTF8.GetString(downloadByte);
        }
    }
}