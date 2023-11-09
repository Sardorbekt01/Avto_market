from django.shortcuts import render
from .models import Avto

def avto (request):
    avto = Avto.objects,all()
    print(avto)
# Create your views here.
