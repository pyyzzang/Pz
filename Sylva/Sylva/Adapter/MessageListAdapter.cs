using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.IO;
using System.Linq;
using Android.App;
using Android.Graphics;
using Android.OS;
using Android.Support.V4.App;
using Android.Views;
using Android.Widget;
using Firebase.Messaging;
using Java.Interop;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Sylva.Util;
using static Android.Views.View;

namespace Sylva.Data
{
    public class MessageListAdapter : ArrayAdapter
    {
        
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
            mainActivity.Noti(__addMsg.Date, __addMsg.Body);
        }

        public void Update()
        {
            this.Clear();
            this.AddAll(CurVideoList);
            this.NotifyDataSetChanged();
        }

        public MessageListAdapter(MainActivity __mainActivity) : base(__mainActivity, Android.Resource.Layout.SimpleListItem1)
        {
            mainActivity = __mainActivity;
            MainHandler.Post(new System.Action(Update));
        }

        private static string GetVideoList { get { return "{0}/API?API=GetVideoList"; } }
        private List<FileItem> CurVideoList
        {
            get
            {
                string fileList = HttpUtil.SendMessage(GetVideoList);
                Newtonsoft.Json.Linq.JArray jArray = (Newtonsoft.Json.Linq.JArray)JsonConvert.DeserializeObject(fileList);
                List<FileItem> retList = new List<FileItem>();
                foreach (JToken jToken in jArray)
                {
                    retList.Add(new FileItem(jToken));
                }
                return retList;                
            }
        }

        public override View GetView(int position, View convertView, ViewGroup parent)
        {
            View v = convertView;
            FileItem msg = CurVideoList.ElementAt(position);
            if (v == null) // no view to re-use, create new
                v = mainActivity.LayoutInflater.Inflate(Resource.Layout.MessageLayout, null);

            TextView txtViewDate = (TextView)v.FindViewById(Resource.Id.txtBody);
            TextView txtViewBody = (TextView)v.FindViewById(Resource.Id.txtBody);
            if (null != msg)
            {
                if (txtViewBody != null)
                {
                    txtViewBody.Text = msg.FileName;
                }
                if (null != txtViewDate)
                {
                    txtViewDate.Text = msg.Title;
                }
            }

            v.Click += V_Click;
            if (0 == position%2)
            {
                v.SetBackgroundColor(new Color(0xd3, 0xd3, 0xd3));
            }
            else
            {
                v.SetBackgroundColor(new Color(0xff, 0xff, 0xff));
            }
            
            txtViewDate.Tag = v;
            txtViewBody.Tag = v;

            txtViewDate.Click += TxtView_Click;
            txtViewBody.Click += TxtView_Click;

            Button playButton = v.FindViewById<Button>(Resource.Id.Play);
            playButton.Tag = msg;
            playButton.Click += PlayButton_Click;

            return v;
        }

        private static string PlayVideoUrl { get { return "{0}/Play?file={1}"; } }
        private void PlayButton_Click(object sender, EventArgs e)
        {
            Button btn = sender as Button;
            if(null == btn)
            {
                return;
            }
            FileItem item = btn.Tag as FileItem;
            if(null == item)
            {
                return;
            }

            string playUrl = string.Format(PlayVideoUrl, "{0}", item.EncodeName);
            HttpUtil.SendMessage(playUrl);
        }

        private void BtnDelete_Click(object sender, EventArgs e)
        {
            if(null == CurrentView)
            {
                return;
            }

            UpdateButtonLayoutStatus(CurrentView, ViewStates.Invisible);
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

        private void UpdateButtonLayoutStatus(View __view , ViewStates __states)
        {
            LinearLayout PlayerLayout = (LinearLayout)__view.FindViewById(Resource.Id.PlayerLayout);
            PlayerLayout.Visibility = __states;
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
                UpdateButtonLayoutStatus(CurrentView, ViewStates.Gone);
            }
            CurrentView = v;
            UpdateButtonLayoutStatus(CurrentView, ViewStates.Visible);
        }

        private MainActivity mainActivity = null;
    }
}