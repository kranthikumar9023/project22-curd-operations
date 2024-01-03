from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.

def display_topic(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    QLTO=Topic.objects.order_by(Length('topic_name').desc())
    QLTO=Topic.objects.filter(topic_name='cricket').order_by('topic_name')
    QLTO=Topic.objects.exclude(topic_name='cricket').order_by('-topic_name')
    QLTO=Topic.objects.filter(topic_name__startswith='v')
    QLTO=Topic.objects.filter(topic_name__endswith='l')
    QLTO=Topic.objects.filter(topic_name__contains='f')
    QLTO=Topic.objects.all()

    d={'topic':QLTO}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    QLWO=Webpage.objects.filter(name='dhoni').order_by('-name')
    QLWO=Webpage.objects.filter(pk=1).order_by('-name')
    QLWO=Webpage.objects.exclude(topic_name='cricket').order_by('-name')
    QLWO=Webpage.objects.filter(name__startswith='r')
    QLWO=Webpage.objects.filter(url__startswith='h')
    QLWO=Webpage.objects.filter(url__endswith='in')
    QLWO=Webpage.objects.filter(url__contains='com')
    QLWO=Webpage.objects.filter(pk__gte=5)
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(name__startswith='r' , url__endswith='in')
    QLWO=Webpage.objects.filter(name__startswith='r' , email__endswith='in')
    QLWO=Webpage.objects.filter(Q(name__startswith='r') & Q(url__endswith='in'))
    QLWO=Webpage.objects.filter(Q(name__startswith='r') & Q(url__endswith='in'))
    QLWO=Webpage.objects.filter(Q(name__contains='r') & Q(url__contains='in'))
    QLWO=Webpage.objects.filter(Q(name__contains='r') | Q(email__contains='.'))
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


def display_accessrecord(request):
    QLAR=AccessRecord.objects.all()
    QLAR=AccessRecord.objects.all().order_by('name')
    QLAR=AccessRecord.objects.all().order_by('-name')
    QLAR=AccessRecord.objects.filter(author='dhoni').order_by('name')
    QLAR=AccessRecord.objects.exclude(author='dhoni').order_by('name')
    QLAR=AccessRecord.objects.filter(date__month=12)
    QLAR=AccessRecord.objects.filter(date__day=19)
    QLAR=AccessRecord.objects.filter(author__startswith='u')
    QLAR=AccessRecord.objects.filter(author__endswith='t')
    QLAR=AccessRecord.objects.filter(pk__gt=1)
    QLAR=AccessRecord.objects.all()
    QLAR=AccessRecord.objects.filter(author__contains='a',date__contains=12)
    QLAR=AccessRecord.objects.filter(Q(author__contains='a') | Q(date__contains=12))
    QLAR=AccessRecord.objects.filter(Q(author__startswith='a') & Q(date__contains=12))
    d={'accessrecord':QLAR}
    return render(request,'display_accessrecord.html',d)




def insert_topic(request):
    tn=input('enter tn value:')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return render(request,'display_topic.html')

def insert_webpage(request):
    pk=input('enter pk')
    n=input('enter n ')
    u=input('enter u ')
    e=input('enter e ')
    TO=Topic.objects.get(pk=pk)
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()
    return HttpResponse('insertion sucess')

def update_webpage(request):
    #Webpage.objects.filter(topic_name='bassball').update(name='kranthi')
    #Webpage.objects.filter(name='kranthi').update(url='https://kranthi.in',email='kranthi@gmail.com')
    #Webpage.objects.filter(topic_name='cricket').update(url='https://india.com')
    #Webpage.objects.filter(name='kranthi').update(topic_name='cricket')
    TO=Topic.objects.get(topic_name='bassball')
    Webpage.objects.update_or_create(name='kranthi',defaults={'topic_name':TO})
    #Webpage.objects.filter(name='kranthi').update(topic_name='football')
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)

def update_accessrecord(request):
    #AccessRecord.objects.filter(name=2).update(author='raider')
    AccessRecord.objects.filter(pk=4).update(author='chaseman')
    QLAR=AccessRecord.objects.all()
    d={'accessrecord':QLAR}
    return render(request,'display_accessrecord.html',d)