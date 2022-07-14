from django.db import models

# Create your models here.
class PhotoModel(models.Model):
    imageid= models.AutoField(primary_key=True)
    imagename=models.CharField(max_length=30,null=False,blank=False)
    imageurl=models.URLField(max_length = 200,null=False,blank=False)
    imagedetails=models.TextField()

