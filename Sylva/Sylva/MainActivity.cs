using System;
using System.Collections.ObjectModel;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;
using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Support.Design.Widget;
using Android.Support.V4.App;
using Android.Support.V7.App;
using Android.Util;
using Android.Views;
using Android.Widget;
using Newtonsoft.Json;
using Sylva.Data;
using Sylva.Util;

namespace Sylva
{
    [Activity(Label = "@string/app_name", Theme = "@style/AppTheme.NoActionBar", MainLauncher = true)]
    public class MainActivity : AppCompatActivity
    {
        public static string TAG { get { return "MainActivity"; } }
        public static MainActivity CurrentMainActivity = null;
        static int NOTIFICATION_ID = 1006;
        static string CHANNEL_ID = "Sylva_Notification";

        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            Xamarin.Essentials.Platform.Init(this, savedInstanceState);
            SetContentView(Resource.Layout.activity_main);

            ListView msgListView = FindViewById<ListView>(Resource.Id.MsgListView);
            msgListView.Adapter = MsgListAdapter;

            CurrentMainActivity = this;
            NotiServiceCreat();
        }

        private void NotiServiceCreat()
        {
            if (Build.VERSION.SdkInt < BuildVersionCodes.O)
            {
                // Notification channels are new in API 26 (and not a part of the
                // support library). There is no need to create a notification
                // channel on older versions of Android.
                return;
            }

            var name = "Name";
            var description = "description";
            var channel = new Android.App.NotificationChannel(CHANNEL_ID, name, Android.App.NotificationImportance.Default)
            {
                Description = description
            };
            var notificationManager = (Android.App.NotificationManager)GetSystemService(NotificationService);
            notificationManager.CreateNotificationChannel(channel);
        }

        public void Noti(string __msg)
        {
            // When the user clicks the notification, SecondActivity will start up.
            var resultIntent = new Intent(this, typeof(MainActivity));

            // Construct a back stack for cross-task navigation:
            var stackBuilder = Android.Support.V4.App.TaskStackBuilder.Create(this);
            stackBuilder.AddParentStack(Java.Lang.Class.FromType(typeof(MainActivity)));
            stackBuilder.AddNextIntent(resultIntent);

            // Create the PendingIntent with the back stack:            
            var resultPendingIntent = stackBuilder.GetPendingIntent(0, (int)PendingIntentFlags.UpdateCurrent);

            // Build the notification:
            var builder = new NotificationCompat.Builder(this, CHANNEL_ID)
                          .SetAutoCancel(true) // Dismiss the notification from the notification area when the user clicks on it
                          .SetContentIntent(resultPendingIntent) // Start up this activity when the user clicks the intent.
                          .SetContentTitle("다운로드 완료") // Set the title
                          .SetSmallIcon(Resource.Drawable.ic_mtrl_chip_checked_black) // This is the icon to display
                          .SetContentText(__msg); // the message to display.

            // Finally, publish the notification:
            var notificationManager = NotificationManagerCompat.From(this);
            notificationManager.Notify(NOTIFICATION_ID, builder.Build());
        }

        public MessageListAdapter _MsgListAdapter = null;
        public MessageListAdapter MsgListAdapter
        {
            get
            {
                if (null == _MsgListAdapter)
                    _MsgListAdapter = new MessageListAdapter(this);
                return _MsgListAdapter;
            }

        }

        public override bool OnCreateOptionsMenu(IMenu menu)
        {
            MenuInflater.Inflate(Resource.Menu.menu_main, menu);
            return true;
        }

        public override bool OnOptionsItemSelected(IMenuItem item)
        {
            int id = item.ItemId;
            if (id == Resource.Id.action_settings)
            {
                return true;
            }

            return base.OnOptionsItemSelected(item);
        }
    }
}

