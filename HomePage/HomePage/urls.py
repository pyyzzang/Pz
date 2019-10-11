"""
Definition of urls for HomePage.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.home, name='h=Home'),
    url(r'Play/Skip', app.views.Skip, name='Skip'),
    url(r'Play/Back', app.views.Back, name='Back'),
    url(r'Play/VolumeUp', app.views.VolumeUp, name='VolumeUp'),
    url(r'Play/VolumnDown', app.views.VolumeDown, name='VolumeDown'),
    url(r'Play', app.views.play, name='play'),
    url(r'Test', app.views.test, name='test'),
    url(r'Home', app.views.home, name='Home'),
]
