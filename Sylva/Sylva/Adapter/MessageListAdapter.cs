using System.Collections.ObjectModel;
using System.IO;
using Android.OS;
using Android.Views;
using Android.Widget;
using Firebase.Messaging;

namespace Sylva.Data
{
    public class MessageListAdapter: ArrayAdapter
    {
        FCM_List _FCM_List
        {
            get { return Sylva.Data.FCM_List.GetFCMList(); }
        }

        Handler _MainHandler = null;
        Handler MainHandler
        {
            get
            {
                if(null == _MainHandler)
                    _MainHandler = new Handler(Looper.MainLooper);
                return _MainHandler;
            }
        }

        public void AddReceiveMsg(RemoteMessage __remoteMsg)
        {
            this.AddReceiveMsg(new FCM_Message(__remoteMsg.GetNotification().Title, __remoteMsg.GetNotification().Body));
        }

        public void AddReceiveMsg(FCM_Message __addMsg)
        {
            _FCM_List.Add(__addMsg);
            MainHandler.Post(new System.Action(Update));
            _FCM_List.SaveFile();
        }

        public void Update()
        {
            this.Clear();
            this.AddAll(_FCM_List);
            this.NotifyDataSetChanged();
        }

        public MessageListAdapter(MainActivity __mainActivity): base(__mainActivity, Android.Resource.Layout.SimpleListItem1)
        {
            mainActivity = __mainActivity;
            this.AddAll(_FCM_List);
        }

        public override View GetView(int position, View convertView, ViewGroup parent)
        {
            View v = convertView;
            FCM_Message msg = _FCM_List[position];
            if (v == null) // no view to re-use, create new
                v = mainActivity.LayoutInflater.Inflate(Resource.Layout.MessageLayout, null);
            if (null != msg)
            {
                TextView tt = (TextView)v.FindViewById(Resource.Id.txtTitle);
                TextView bt = (TextView)v.FindViewById(Resource.Id.txtBody);
                if (tt != null)
                {
                    tt.Text = "Title : " + msg.Title;
                }
                if (bt != null)
                {
                    bt.Text = "Body : " + msg.Body;
                }
            }
            return v;
        }
        private MainActivity mainActivity = null;
    }
}