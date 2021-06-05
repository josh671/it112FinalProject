from django.urls import path
#need to import views 5-24-2021
from . import views 
urlpatterns = [
    #first url, for homepage
    path('', views.index, name='index'), #5-24-2021 
    #last added 5-24
    path('movies/', views.movies, name='movies'), 
    
    path('moviesdetails/<int:id>', views.moviesdetails, name='movies'),
    path('reviews/', views.reviews, name='reviews' ), 

    #paths for forms 
    path('newmovietype/', views.newMovieType, name='newmovietype'),

    path('newmovie/', views.newMovie, name='newmovie'),
    path('newreview/', views.newMovieReview, name='newreview'),

    #paths for login/out
     #adding login/out
    path('loginmessage', views.loginmessage, name='loginmessage'),
    path('logoutmessage', views.logoutmessage, name='logoutmessage'),
]