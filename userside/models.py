from django.db import models
import datetime
from time import strftime, gmtime


# Create your models here.

def get_upload_file_name(instance, filename):
	return "uploads/user/%s_%s" % (str(strftime("%Y-%m-%d-%H-%M-%S", gmtime())), filename)

# Model for User
class UserProfile(models.Model):
	email = models.CharField(max_length=100)
	points = models.IntegerField(default=0)
	isNgo = models.BooleanField(default=False)
	isEcom = models.BooleanField(default=False)
	# Rest are not necessary
	name = models.CharField(max_length=100, blank=True, null=True)
	number = models.CharField(max_length=100, blank=True, null=True)
	address = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.name


class Ewaste(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField()
	bought_on = models.DateTimeField()
	pic = models.FileField(upload_to=get_upload_file_name)
	user = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return self.name
