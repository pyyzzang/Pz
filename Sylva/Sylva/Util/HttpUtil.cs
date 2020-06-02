using System;
using System.Collections.Generic;
using System.IO;
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
                return "https://192.168.219.102:8080";
#else
                return "https://192.168.219.102";
#endif
            }
        }

        public static string SendMessage(string __Url, bool __isPost = true, System.Collections.Specialized.NameValueCollection __param = null)
        {
            ServicePointManager.ServerCertificateValidationCallback += (sender, certificate, chain, sslPolicyErrors) => true;
            WebClient client = new WebClient();
            byte[] downloadByte;
            if (null == __param)
            {
                return client.DownloadString(string.Format(__Url, ServerUrl));
            }
            else
            {
                downloadByte = client.UploadValues(string.Format(__Url, ServerUrl), __isPost ? "POST" : "GET", __param);
            }
            
            return Encoding.UTF8.GetString(downloadByte);
        }

        public static string UploadFile(string __url, string __filePath)
        {
            if(false == File.Exists(__filePath))
            {
                return string.Empty;
            }

            ServicePointManager.ServerCertificateValidationCallback += (sender, certificate, chain, sslPolicyErrors) => true;

            string uploadUrl = string.Format(__url, ServerUrl);
            
            string boundary = "---------------------------" + DateTime.Now.Ticks.ToString("x");
            byte[] boundaryBytes = System.Text.Encoding.ASCII.GetBytes("\r\n--" + boundary + "\r\n");
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(uploadUrl);
            request.ContentType = "multipart/form-data; boundary=" + boundary;
            request.Method = "POST";
            request.KeepAlive = true;

            using (Stream requestStream = request.GetRequestStream())
            {
                requestStream.Write(boundaryBytes, 0, boundaryBytes.Length);

                string header = "Content-Disposition: form-data; name=\"logFile\"; filename=\"" + Path.GetFileName(__filePath ) + "\";\r\nContent-Type:multipart/form-data;\r\n\r\n";
                byte[] bytes = System.Text.Encoding.UTF8.GetBytes(header);
                requestStream.Write(bytes, 0, bytes.Length);
                byte[] buffer = new byte[32768];
                int bytesRead;
                // upload from file
                using (FileStream fileStream = File.OpenRead(__filePath))
                {
                    while ((bytesRead = fileStream.Read(buffer, 0, buffer.Length)) != 0)
                        requestStream.Write(buffer, 0, bytesRead);
                    fileStream.Close();
                }
                byte[] trailer = System.Text.Encoding.ASCII.GetBytes("\r\n--" + boundary + "--\r\n");
                requestStream.Write(trailer, 0, trailer.Length);
                requestStream.Close();
            }

            using (WebResponse response = request.GetResponse())
            {
                using (Stream responseStream = response.GetResponseStream())
                using (StreamReader reader = new StreamReader(responseStream))
                    return reader.ReadToEnd();
            }
        }
    }
}