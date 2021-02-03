from django.shortcuts import render
from .models import StaticFileExample


# Create your views here.

def index(request):
    images = StaticFileExample.objects.all()

    context = {
        'images': images
    }

    return render(request, 'index.html', context)
