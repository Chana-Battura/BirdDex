from django.contrib import admin
from .models import Bird, BirdFound, User
# Register your models here.
admin.site.register(Bird)
admin.site.register(BirdFound)
admin.site.register(User)