using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.Gms.Ads;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;

namespace Sylva.Data
{
    public class SylvaAdListener : AdListener
    {
        public override void OnAdLoaded()
        {
            base.OnAdLoaded();
        }

        public override void OnAdFailedToLoad(int p0)
        {
            switch(p0)
            {
                case AdRequest.ErrorCodeInternalError:
                    Console.WriteLine("AdRequest.ErrorCodeInternalError");
                    
                    break;
                case AdRequest.ErrorCodeInvalidRequest:
                    Console.WriteLine("AdRequest.ErrorCodeInvalidRequest");
                    break;
                case AdRequest.ErrorCodeNetworkError:
                    Console.WriteLine("AdRequest.ErrorCodeNetworkError");
                    break;
                case AdRequest.ErrorCodeNoFill:
                    Console.WriteLine("AdRequest.ErrorCodeNoFill");
                    break;
            }
            
            base.OnAdFailedToLoad(p0);
        }

        public override void OnAdClosed()
        {
            base.OnAdClosed();
        }
    }
}