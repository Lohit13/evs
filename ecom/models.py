from django.db import models
import datetime
from userside.models import *
from time import strftime, gmtime


def get_upload_file_name(instance, filename):
	return "uploads/ecom/%s_%s" % (str(strftime("%Y-%m-%d-%H:%M:%S", gmtime())), filename)

# Create your models here.
class ECOM(models.Model):
	email = models.CharField(max_length=100)
	name = models.CharField(max_length=500,null=True,blank=True)
	address = models.CharField(max_length=500,null=True,blank=True)
	phno = models.CharField(max_length=10,null=True,blank=True)
	cname = models.CharField(max_length=500,null=True,blank=True)

class Product(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField()
	bought_on = models.DateTimeField()
	pic = models.FileField(upload_to=get_upload_file_name)
	user = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return self.name

