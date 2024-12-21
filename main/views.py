from django.shortcuts import render
from main.models import Banners

# Create your views here.
def banners(requset):
    banner = Banners.objects.all()
    return render(requset, 'index.html', locals())