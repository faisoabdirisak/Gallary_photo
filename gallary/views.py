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

    locations=Location.objects.all()
    categories=Category.objects.all()
    context={'locations':locations, 'categories':categories, 'photos':photos}
    return render(request,'gallary.html',context)

def viewPhoto(request,pk):
    photo=Photo.objects.get(id=pk)
    return render(request,'photo.html',{'photo':photo})    



def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched = category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"categories": searched})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})    




# def search_results(request):
#     if 'imagesearch' in request.GET and request.GET["imagesearch"]:
#         category = request.GET.get("imagesearch")
#         searched_images = Photo.search_by_category(category)
#         message = f"{category}"
#         print(searched_images)
#         return render(request, 'search_results.html', {"message": message, "images": searched_images})
#     else:
#         message = "You haven't searched for any image category"
#         return render(request, 'search_results.html', {"message": message})