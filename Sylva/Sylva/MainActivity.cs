using System.Threading;
using Android.App;
using Android.Content;
using Android.Gms.Ads;
using Android.OS;
using Android.Support.V4.App;
using Android.Support.V7.App;
using Android.Views;
using Android.Widget;
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

        protected AdView adsView;

        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            Xamarin.Essentials.Platform.Init(this, savedInstanceState);
            SetContentView(Resource.Layout.content_main);

            ListView msgListView = FindViewById<ListView>(Resource.Id.MsgListView);
            msgListView.Adapter = MsgListAdapter;

            Thread t = new Thread(new ThreadStart(InitView));
            t.Start();

            InitPlayerLayout();
        }

        private void InitPlayerLayout()
        {
            Button btnBack = FindViewById<Button>(Resource.Id.Back);
            btnBack.Click += BtnBack_Click;

            Button btnReplay = FindViewById<Button>(Resource.Id.Replay);
            btnReplay.Click += BtnBack_Click;

            Button btnPause = FindViewById<Button>(Resource.Id.Pause);
            btnPause.Click += BtnBack_Click;

            Button btnStop = FindViewById<Button>(Resource.Id.Stop);
            btnStop.Click += BtnBack_Click;

            Button btnSkip = FindViewById<Button>(Resource.Id.Skip);
            btnSkip.Click += BtnBack_Click;

        }

        private void BtnBack_Click(object sender, System.EventArgs e)
        {
            Button btn = sender as Button;
            if(null == btn)
            {
                return;
            }
            string url = string.Format("{0}/Play/{1}","{0}", btn.Text.ToString());
            HttpUtil.SendMessage(url);
        }

        private static string CurFileNameUrl { get { return "{0}/Play/CurFileName"; } }
        
        private void InitView()
        {
            CurrentMainActivity = this;
            NotiServiceCreat();

            //광고
            //Android.Gms.Ads.MobileAds.Initialize(ApplicationContext, this.Resources.GetString(Resource.String.AdMobID));
            //adsView = (AdView)FindViewById(Resource.Id.adView);
            //adsView.AdListener = new SylvaAdListener();
            //AdRequest request = new AdRequest.Builder().Build();
            //adsView.LoadAd(request);

            Thread CurPlayerUpdate = new Thread(CurPlayerUpdateThread);
            CurPlayerUpdate.Start();
        }

        Handler _MainHandler = null;
        Handler MainHandler
        {
            get
            {
                if (null == _MainHandler)
                    _MainHandler = new Handler(Looper.MainLooper);
                return _MainHandler;
            }
        }

        private void CurPlayerUpdateThread()
        {
            while(true)
            {
                MainHandler.Post(UpdateTitle);
                Thread.Sleep(1000);
            }
        }

        private string CurFileName
        {
            get
            {
                return HttpUtil.SendMessage(CurFileNameUrl);
            }
        }

        private void UpdateTitle()
        {
            LinearLayout curPlayer = FindViewById<LinearLayout>(Resource.Id.CurPlayer);
            if (true == string.IsNullOrEmpty(CurFileName))
            {
                curPlayer.Visibility = ViewStates.Gone;
            }
            else
            {
                curPlayer.Visibility = ViewStates.Visible; 
            }
            
            TextView title = FindViewById<TextView>(Resource.Id.Title);
            title.Text = CurFileName;
        }

        protected override void OnResume()
        {
            base.OnResume();
            if(null != adsView)
            {
                adsView.Resume();
            }
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

        public void Noti(string __title, string __msg)
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
                          .SetContentTitle(__title) // Set the title
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

