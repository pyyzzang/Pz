"""
Definition of views.
"""

from django.shortcuts import render
from fileListView import fileListView
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from fileListView import fileListView


def home(request):
    return fileListView.getFileList("");

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
