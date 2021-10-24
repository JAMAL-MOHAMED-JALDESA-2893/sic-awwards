from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime as dt


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = CloudinaryField('image')
    Bio = models.CharField(max_length=30)    
    contact=models.CharField(max_length=12,null=True)
    datecreated= models.DateField(auto_now_add=True )

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    def __str__(self):
        return self.user.username
 
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()    



class Projects(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    projectscreenshot = CloudinaryField('images')
    projecturl= models.URLField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    datecreated= models.DateField(auto_now_add=True )


    def save_projects(self):
        self.user

    def delete_projects(self):
        self.delete()    