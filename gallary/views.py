from unicodedata import category
from django.shortcuts import render
from . models import Category, Photo, Location

# Create your views here.

def gallary(request):
    location =request.GET.get('location')
    if location==None:
        photos=Photo.objects.all()
    else:
         photos = Photo.objects.filter(location__name = location)
    categories=Category.objects.all()
    locations=Location.objects.all()
    
    context={'locations':locations, 'categories':categories, 'photos':photos}
    return render(request,'gallary.html',context)

def viewPhoto(request,pk):
    photo=Photo.objects.get(id=pk)
    return render(request,'photo.html',{'photo':photo})    



def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched = category.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"categories": searched})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})    