from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *

def insert_Topic(request):
    TOB=Topicform()
    d={'TOB':TOB}
    if request.method=='POST':
        TBO=Topicform(request.POST)
        if TBO.is_valid():
            topic_name=TBO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=topic_name)
            TO.save()
            TQS=Topic.objects.all()
            d1={'TQS':TQS}
            return render(request,'display_Topic.html',d1)
    return render(request,'insert_Topic.html',d)
def insert_Webpages(request):
    WOB=Webpageform()
    d={'WOB':WOB}
    if request.method=='POST':
        WBO=Webpageform(request.POST)
        if WBO.is_valid():
            topic_name=WBO.cleaned_data['topic_name']
            name=WBO.cleaned_data['name']
            url=WBO.cleaned_data['url']
            email=WBO.cleaned_data['email']
            TO=Topic.objects.get(topic_name=topic_name)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
            WO.save()
            WQB=Webpage.objects.all()
            d1={'WQB':WQB}
            return render(request,'display_Webpage.html',d1)
    return render(request,'insert_Webpages.html',d)
def insert_Access(request):
    AOB=AccessRecordform()
    d={'AOB':AOB}
    if request.method=='POST':
        ABO=AccessRecordform(request.POST)
        if ABO.is_valid():
            name=ABO.cleaned_data['name']
            author=ABO.cleaned_data['author']
            date=ABO.cleaned_data['date']
            WO=Webpage.objects.get(name=name)
            AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
            AO.save()
            AQB=AccessRecord.objects.all()
            d1={'AQB':AQB}
            return render(request,'display_Access.html',d1)
    return render(request,'insert_Access.html',d)