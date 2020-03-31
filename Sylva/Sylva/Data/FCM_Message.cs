using System;
using System.Collections.Generic;
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
    public class FCM_Message: Java.Lang.Object
    {
        public string Title { get; set; }
        public string Body { get; set; }
        public FCM_Message(string __title, string __body)
        {
            Title = __title;
            Body = __body;
        }
    }
}