from django.shortcuts import render
from . models import Category, Photo, Location

# Create your views here.

def gallary(request):
    location=Location.objects.all()
    context={'location':location}
    return render(request,'gallary.html',context)

def viewPhoto(request,pk):
    return render(request,'photo.html')    