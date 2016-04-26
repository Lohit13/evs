from django.db import models

# Create your models here.

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
