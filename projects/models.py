from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    photo = CloudinaryField('images')
    Bio = models.CharField(max_length=30)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact=models.CharField(max_length=12,null=True)
    datecreated= models.DateField(auto_now_add=True )
