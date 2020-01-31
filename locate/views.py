from django.shortcuts import render, HttpResponse, redirect
from bs4 import BeautifulSoup
from .models import LinkTable
import random
# from django.contrib.gis.utils import GeoIP
# g = GeoIP()


def index(request):
    return render(request, 'index.html', {'title': 'Locator'})

def createLink(request):
    link_id=random.randint(1000, 50000)
    link = "/trace/"+str(link_id)
    p = LinkTable(link=link, link_id=link_id)
    p.save()
    return HttpResponse(link)

def trace(request, link_id):
    link = LinkTable.objects.filter(link_id=link_id)
    if(len(link) != 0):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
            city = g.city(ip)['city']
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(link, "\n", ip)
    else:
        print("No Recorde")
    
    return HttpResponse(ip)