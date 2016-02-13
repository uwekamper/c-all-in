from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import AnnounceForm
# Create your views here.

@csrf_exempt
def announce(request):
    if request.method == 'POST':
        form = AnnounceForm(request.POST, request.FILES)
        if form.is_valid():
            print(u'Cleaned data: {}'.format(form.cleaned_data))
            return render(request, 'calls/announce.html', {'title': 'Thank you'})
        else:
            response = render(request, 'calls/announce.html',
                    {'title': 'Bad stuff happened', 'form': form})
            response.status_code = 400
            return response
    else:
        return render(request, 'calls/announce.html', {'title': 'Please use POST, KTHXBYE'})
