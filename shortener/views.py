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
            new_url = Shorten(url=url, slug=slug)
            new_url.save()
            return redirect('/')
        else:
            form = UrlForm(request.POST)
        context = {
            'form':form
        }
    return render(request, 'shortener/home.html',context)


def urlredirect(request, slug):
    return render(request)