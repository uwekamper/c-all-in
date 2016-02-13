import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .forms import AnnounceForm
# Create your views here.

def handle_announcement(f):
    upload_dir = os.path.join(settings.MEDIA_ROOT, 'announcements')
    if not os.path.exists():
        os.makedirs(upload_dir)
    save_to = os.path.join(settings.MEDIA_ROOT, 'announcements/{}'.format(f.name))

    with open(save_to, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_exempt
def announce(request):
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
