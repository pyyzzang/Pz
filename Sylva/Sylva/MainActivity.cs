﻿using System;
using Android.App;
using Android.OS;
using Android.Runtime;
using Android.Support.Design.Widget;
using Android.Support.V7.App;
using Android.Views;
using Android.Widget;
using Sylva.Data;

namespace Sylva
{
    [Activity(Label = "@string/app_name", Theme = "@style/AppTheme.NoActionBar", MainLauncher = true)]
    public class MainActivity : AppCompatActivity
    {
        public static MainActivity CurrentMainActivity = null;
        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            Xamarin.Essentials.Platform.Init(this, savedInstanceState);
            SetContentView(Resource.Layout.activity_main);

            ListView msgListView = FindViewById<ListView>(Resource.Id.MsgListView);
            msgListView.Adapter = MsgListAdapter;

            CurrentMainActivity = this;
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

