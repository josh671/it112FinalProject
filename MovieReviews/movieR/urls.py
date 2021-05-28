from django.urls import path
#need to import views 5-24-2021
from . import views 
urlpatterns = [
    #first url, for homepage
    path('', views.index, name='index'), #5-24-2021 
    #last added 5-24
]