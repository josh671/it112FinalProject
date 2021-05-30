from django.shortcuts import get_object_or_404, render
from .models import MovieType, Movies, Reviews
# Create your views here.
#5-24-2021
def index(request): 
    return render(request, 'movieR/index.html')  


def movies(request):
    movies_list=MovieType.objects.all()
    return render(request, 'movieR/movies.html', {'movies_list': movies_list}) 

def moviesdetails(request, id): 
    movies=get_object_or_404(Movies, pk=id) 
    return render(request, 'movieR/moviesdetails.html', {'movies':movies})

def reviews(request): 
    reviews_list=Reviews.objects.all()
    return render(request, 'movieR/reviews.html', {'reviews_list': reviews_list}) 