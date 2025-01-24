from django.shortcuts import render
from.models import Language,Doctor

# Create your views here.

def hello(request):
    return render(request,'hello.html')

def langChoice(request):
    languages=Language.objects.all()
    return render(request,'langchoice.html',{'languages':languages})

def docview(request,pk):
    language=Language.objects.get(pk=pk)
    doctors=language.doctor_set.all()
    return render(request,'docdisplay.html',{'language':language,'doctors':doctors})