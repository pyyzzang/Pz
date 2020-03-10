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

    url(r'Play/Back600', app.views.Back600, name='Back600'),
    url(r'Play/Back', app.views.Back, name='Back'),
    url(r'Play/Replay', app.views.Replay, name='Replay'),
    url(r'Play/Pause', app.views.Pause, name='Pause'),
    url(r'Play/Skip600', app.views.Skip600, name='Skip600'),
    url(r'Play/Skip', app.views.Skip, name='Skip'),
    url(r'Play/VolumeUp', app.views.VolumeUp, name='VolumeUp'),
    url(r'Play/VolumeDown', app.views.VolumeDown, name='VolumeDown'),

    url(r'Home/Delete', app.views.Delete, name='Delete'),
    url(r'Play', app.views.play, name='play'),
    url(r'Test', app.views.test, name='test'),
    url(r'Home', app.views.home, name='Home'),
    url(r'Torrent/Upload', app.views.TorrentUpload, name='TorrentUpload'),
    url(r'Torrent/TorrentAdd', app.views.TorrentAdd, name='TorrentAdd'),
    url(r'Torrent', app.views.Torrent, name='Torrent'),
    
]
