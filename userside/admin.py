from django.contrib import admin
from userside.models import *

# Register your models here.

Models = [UserProfile, Ewaste, Offer]

admin.site.register(Models)







