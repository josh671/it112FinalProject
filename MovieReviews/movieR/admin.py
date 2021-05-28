from django.contrib import admin
#import models 
from .models import MovieType, Movies, Reviews
# Register your models here.
admin.site.register(MovieType)
admin.site.register(Movies)
admin.site.register(Reviews)