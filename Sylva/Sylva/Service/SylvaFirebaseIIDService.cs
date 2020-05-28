using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Util;
using Android.Views;
using Android.Widget;
using Firebase.Iid;
using Sylva.Util;

namespace Sylva.Service
{
    [Service]
    [IntentFilter(new[] { "com.google.firebase.INSTANCE_ID_EVENT" })]
    public class MyFirebaseIIDService : FirebaseInstanceIdService
    {
        const string TAG = "MyFirebaseIIDService"; 
        public override void OnTokenRefresh()
        {
            var refreshedToken = FirebaseInstanceId.Instance.Token;
            Sylva.Util.Log.Write("Refreshed token: " + refreshedToken);
            SendRegistrationToServer(refreshedToken);

            BackgroundWorker dbUpdateWorker = new BackgroundWorker();
            dbUpdateWorker.DoWork += DbUpdateWorker_DoWork;
            dbUpdateWorker.RunWorkerAsync(refreshedToken);
        }

        private static string UpdateUserInfo { get { return "{0}/RegisterToken"; } }

        private void DbUpdateWorker_DoWork(object sender, DoWorkEventArgs e)
        {
            try
            {
                System.Collections.Specialized.NameValueCollection sendValue = new System.Collections.Specialized.NameValueCollection();
                sendValue.Add("id", "1");
                sendValue.Add("token", e.Argument.ToString());
                HttpUtil.SendMessage(UpdateUserInfo, true, sendValue);
            }catch(Exception ex)
            {
                Sylva.Util.Log.Write("Exception : " + e.Result);

            }
            
        }

        void SendRegistrationToServer(string token)
        {
            // Add custom implementation, as needed.
        }
    }
}
