from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from sprawlapp.forms import FindSprawlForm
from .pictures import getPicture

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        start = str(request.POST['start'])
        end = str(request.POST['end'])
        getPicture(city, start, end)

        #produce URL
        image_urls = {}
        for year in range(int(start), int(end)+1):
            image_urls[str(year)] = city + "_image_" + str(year) + ".png"
        form = FindSprawlForm()
        return render(request,
            'sprawlapp/index.html',
            {'form': form, 'image_urls': image_urls})
    else:
        return render(request,
            'sprawlapp/index.html',
            {})

