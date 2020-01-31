from django.shortcuts import render, HttpResponse, redirect
from bs4 import BeautifulSoup
from .models import LinkTable, Recordes
import random
import requests
import json
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
            # city = g.city(ip)['city']
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        # ip = "167.172.219.121"
        recorde = getRecorde(ip)
        # print(recorde)
        p = Recordes(link_id = link_id, recorde = recorde)
        p.save()

    else:
        print("No Recorde")
    
    
    return render(request, 'trace.html', {'ip': ip})


def recorde(request, link_id):
    data = {}
    recorde = Recordes.objects.filter(link_id=link_id)
    if(len(recorde) != 0):
        recs = Recordes.objects.all().filter(link_id=link_id)
        recordeData = []
        for rec in recs:
            recordeData.append({'link_id': rec.link_id, 'date': str(rec.date), 'recorde': rec.recorde})
        data = {"recorde": len(recorde), "data": recordeData}
    else:
        data = {"recorde": 0}

    data = json.dumps(data)
    print(data)
    # data = json.loads(data)
    return HttpResponse(data)





def getRecorde(ip):
    url = "http://api.ipstack.com/"+ip+"?access_key=7f563c795cee550b5b41ee583fd8e0c2&format=1"
    data = requests.post(url)
    data = json.loads(data.content)

    return data