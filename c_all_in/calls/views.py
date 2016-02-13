from django.shortcuts import render
from django.http import HttpResponse

from .forms import AnnounceForm
# Create your views here.


def announce(request):
    if request.method == 'POST':
        form = AnnounceForm(request.POST)
        if form.is_valid():
            print(u'Cleaned data: {}'.format(form.cleaned_data))
            return render(request, 'calls/announce.html', {'title': 'Thank you'})
        else:
            return HttpResponse('Bad stuff happened', status=400)
    else:
        return render(request, 'calls/announce.html', {'title': 'Please use POST, KTHXBYE'})
