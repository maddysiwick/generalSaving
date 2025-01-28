from django.shortcuts import render
from.models import Language,Doctor
from  django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

# Create your views here.

def hello(request):
    return render(request,'hello.html')

def langChoice(request):
    languages=Language.objects.all()
    return render(request,'langchoice.html',{'languages':languages})

def docview(request,pk):
    language=Language.objects.get(pk=pk)
    p=Point(-73.63671790047512,45.518782951806266)
    radius=10
    doctors=language.doctor_set.filter(location__distance_lt=(p,Distance(km=radius)))
    return render(request,'docdisplay.html',{'language':language,'doctors':doctors})