from django.shortcuts import render, redirect
from .forms import UrlForm
from .models import Shorten
import random
import string

def home(request):
    if request.method == "POST":

        form = UrlForm(request.POST)

        if form.is_valid():
            
            slug = ''.join(random.choice(string.ascii_letters) for x in range(10))
            url = form.cleaned_data['url']
            d= 'http://localhost:8000/u/'+slug
            new_url = Shorten(url=url, slug=slug)
            new_url.save()
            form = UrlForm()
            return render(request, 'shortener/home2.html',{'short_url':d, 'slug':slug,'form':form})
    else:
        form = UrlForm()
    context = {
        'form':form
    }
    return render(request, 'shortener/home.html',context)


def urlredirect(request, slug):
    data = Shorten.objects.filter(slug=slug)
    print(data[0])
    return redirect(data[0].url)

    