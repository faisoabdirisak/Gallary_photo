from django.shortcuts import render
from . models import Category, Photo, Location

# Create your views here.

def gallary(request):
    categories=Category.objects.all()
    locations=Location.objects.all()
    photos=Photo.objects.all()
    context={'locations':locations, 'categories':categories, 'photos':photos}
    return render(request,'gallary.html',context)

def viewPhoto(request,pk):
    return render(request,'photo.html')    