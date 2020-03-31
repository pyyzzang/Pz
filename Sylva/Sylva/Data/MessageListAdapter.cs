using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;

namespace Sylva.Data
{
    public class MessageListAdapter: ArrayAdapter
    {
        private ObservableCollection<FCM_Message> _FCM_List = null;
        public ObservableCollection<FCM_Message> FCM_List
        {
            get
            {
                if (null == _FCM_List)
                    _FCM_List = new ObservableCollection<FCM_Message>();
                return _FCM_List;
            }
            set { }
        }

        public MessageListAdapter(MainActivity __mainActivity): base(__mainActivity, Android.Resource.Layout.SimpleListItem1)
        {
            mainActivity = __mainActivity;
            FCM_List.Add(new FCM_Message("Title_ 1", "Body _ 1"));
            FCM_List.Add(new FCM_Message("Title_ 2", "Body _ 2"));
            FCM_List.Add(new FCM_Message("Title_ 3", "Body _ 3"));
            FCM_List.Add(new FCM_Message("Title_ 4", "Body _ 4"));
            this.AddAll(FCM_List);
        }

        public override View GetView(int position, View convertView, ViewGroup parent)
        {
            View v = convertView;
            FCM_Message msg = FCM_List[position];
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

        private List<string> list;
        
    }
}