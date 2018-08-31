from django.db import models

# Create your models here.

class UserModel(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	email = models.EmailField()

class PhotoModel(models.Model):
	photo = models.TextField()
	userid = models.ForeignKey(UserModel,on_delete=models.PROTECT)
	numberOfFavorites = models.IntegerField()

class TagModel:
	photoid = models.ForeignKey(PhotoModel,on_delete=models.PROTECT)
	name = models.CharField(max_length=100)

