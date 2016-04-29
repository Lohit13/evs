from django.db import models

# Create your models here.
class NGO(models.Model):
	email = models.CharField(max_length=100)
	name = models.CharField(max_length=500,null=True,blank=True)
	address = models.CharField(max_length=500,null=True,blank=True)
	phno = models.CharField(max_length=10,null=True,blank=True)
	obj = models.CharField(max_length=500,null=True,blank=True)
	chair = models.CharField(max_length=500,null=True,blank=True)
