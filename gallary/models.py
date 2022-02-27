from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=100, null=False, blank=False)

    # def __str__(self):
    #     return self.name

   

    def save_category(self):
        self.save()


class Location(models.Model):
    name= models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


    def save_location(self):
        self.save()


class Photo (models.Model):
    image=models.ImageField(null=False,blank=False,)
    description= models.TextField(max_length=500, null=False, blank=False)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True, blank=True)


    @classmethod
    def search_by_category(cls,search_term):
        photo = cls.objects.filter(name__icontains=search_term)
        return photo

    def __str__(self):
        return self.description        