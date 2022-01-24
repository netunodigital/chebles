from django.shortcuts import render
from .models import *

def index(request):
    context = {
        'home': Home.objects.get(active=True),
        'about': About.objects.get(active=True),
        'banner': Banner.objects.get(active=True),
        'box1': Box1.objects.get(active=True),
        'box2': Box2.objects.get(active=True),
        'box3': Box3.objects.get(active=True),
        'course1': Course1.objects.get(active=True),
        'course2': Course2.objects.get(active=True),
        'local1': Local1.objects.get(active=True),
        'local2': Local2.objects.get(active=True),
    }
    return render(request, 'index.html', context)
