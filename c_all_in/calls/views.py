# -*- coding: utf-8 -*-

import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.urlresolvers import reverse

from .forms import AnnounceForm

def index(request):
    """
    Just a dummy page that shows up.
    """
    return render(request, 'calls/index.html', {})


def handle_announcement(f):
    """
    Helper function that will take the recorded announcement and save it to a file
    in the MEDIA_ROOT directory.
    """
    # Make sure that the directory for uploads exists and create one if necessary.
    upload_dir = os.path.join(settings.MEDIA_ROOT, 'announcements')
    if not os.path.exists(upload):
        os.makedirs(upload_dir)

    # Now create the actual file and save it to the directory.
    save_to = os.path.join(upload_dir, f.name)
    with open(save_to, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_exempt
def receive_announcement(request):
    """
    The Tropo system will send the recorded message to this view using a POST request.
    """
    if request.method == 'POST':
        form = AnnounceForm(request.POST, request.FILES)
        if form.is_valid():
            print(u'Cleaned data: {}'.format(form.cleaned_data))
            handle_announcement(request.FILES['filename'])
            return render(request, 'calls/announce.html', {'title': 'Thank you'})
        else:
            response = render(request, 'calls/announce.html',
                    {'title': 'Bad stuff happened', 'form': form})
            response.status_code = 400
            return response
    else:
        return render(request, 'calls/announce.html', {'title': 'Please use POST, KTHXBYE'})


def callmenu(request):
    """
    Generate a Python script that will is downloaded and run by the Tropo server when someone
    calls in to our service.

    The URL 'http(s)://your-server/calls/callmenu.py' needs to be entered in the Tropo web service.
    """
    # We need to tell tropo where to send the finished MP3 recording.
    ctx = {'webhook_uri': request.build_absolute_uri(reverse('receive_announcement'))}

    # Now we can render the call script that will be downloaded by the tropo server.
    return render(request, 'calls/callmenu.py', ctx, content_type='text/plain')
