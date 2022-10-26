from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from datetime import date


def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})


def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id
    }})

from bmstu_lab.models import Priziv

def PrizivList(request):
    return render(request, 'prizivniki.html', {'data' : {
        'current_date': date.today(),
        'Prizivniki': Priziv.objects.all()
    }})

def GetPriziv(request, id):
    return render(request, 'prizivnik.html', {'data' : {
        'current_date': date.today(),
        'Prizivnik': Priziv.objects.filter(id=id)[0]
    }})
