using System;
using System.Collections.ObjectModel;
using System.IO;
using Android.App;
using Android.OS;
using Android.Support.V4.App;
using Android.Views;
using Android.Widget;
using Firebase.Messaging;
using Java.Interop;
using static Android.Views.View;

namespace Sylva.Data
{
    public class MessageListAdapter : ArrayAdapter
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
                if (null == _MainHandler)
                    _MainHandler = new Handler(Looper.MainLooper);
                return _MainHandler;
            }
        }

        public void AddReceiveMsg(RemoteMessage __remoteMsg)
        {
            this.AddReceiveMsg(new FCM_Message(__remoteMsg));
        }

        public void AddReceiveMsg(FCM_Message __addMsg, bool __isAdd = true)
        {
            if(true == __isAdd)
            {
                _FCM_List.Insert(0, __addMsg);
                mainActivity.Noti(__addMsg.Date, __addMsg.Body);
            }
            else
            {
                _FCM_List.Remove(__addMsg);
            }
            MainHandler.Post(new System.Action(Update));
            _FCM_List.SaveFile();
        }

        public void Update()
        {
            this.Clear();
            this.AddAll(_FCM_List);
            this.NotifyDataSetChanged();
        }

        public MessageListAdapter(MainActivity __mainActivity) : base(__mainActivity, Android.Resource.Layout.SimpleListItem1)
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

            TextView txtViewDate = (TextView)v.FindViewById(Resource.Id.txtDate);
            TextView txtViewBody = (TextView)v.FindViewById(Resource.Id.txtBody);
            if (null != msg)
            {
                if (txtViewBody != null)
                {
                    txtViewBody.Text = msg.Body;
                }
                if (null != txtViewDate)
                {
                    txtViewDate.Text = msg.Date;
                }
            }

            v.Click += V_Click;
            v.Tag = msg;
            
            txtViewDate.Tag = v;
            txtViewBody.Tag = v;

            txtViewDate.Click += TxtView_Click;
            txtViewBody.Click += TxtView_Click;

            Button btnDelete = (Button)v.FindViewById(Resource.Id.btnDelete);
            btnDelete.Tag = v;
            btnDelete.Click += BtnDelete_Click;


            return v;
        }

        private void BtnDelete_Click(object sender, EventArgs e)
        {
            if(null == CurrentView)
            {
                return;
            }

            UpdateButtonStatus(CurrentView, ViewStates.Invisible);
            FCM_Message msg = (FCM_Message)CurrentView.Tag;
            AddReceiveMsg(msg, false);
            CurrentView = null;
        }

        private void TxtView_Click(object sender, EventArgs e)
        {
            TextView view = sender as TextView;
            if(null == view)
            {
                return;
            }
            V_Click(view.Tag, null);
        }

        private View CurrentView { get; set; }

        private void UpdateButtonStatus(View __view , ViewStates __states)
        {
            Button btn = __view.FindViewById<Button>(Resource.Id.btnDelete);
            btn.Visibility = __states;
        }

        private void V_Click(object sender, EventArgs e)
        {
            View v = (View)sender;
            if (null == v)
            {
                return;
            }

            if (null != CurrentView)
            {
                UpdateButtonStatus(CurrentView, ViewStates.Invisible);
            }
            CurrentView = v;
            UpdateButtonStatus(CurrentView, ViewStates.Visible);
        }

        private MainActivity mainActivity = null;
    }
}