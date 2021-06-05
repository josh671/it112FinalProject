from django.shortcuts import get_object_or_404, render
from .models import Movies, MovieType, Reviews
from django.urls import reverse_lazy
#adding form stuff 5-31-2021
#adding login stuffs 
from django.contrib.auth.decorators import login_required 
from .forms import MovieTypeForm, ReviewsForm, MoviesForm
# Create your views here.
#5-24-2021
def index(request): 
    return render(request, 'movieR/index.html')  


def movies(request):
    movies_list=Movies.objects.all()
    return render(request, 'movieR/movies.html', {'movies_list': movies_list}) 

def moviesdetails(request, id): 
    movies=get_object_or_404(Movies, pk=id) 
    return render(request, 'movieR/moviesdetails.html', {'movies':movies})

def reviews(request): 
    reviews_list=Reviews.objects.all()
    return render(request, 'movieR/reviews.html', {'reviews_list': reviews_list})  

#views for the form 
@login_required
def newMovieType(request): 
    form=MovieTypeForm 
    if request.method=='POST': 
        form =MovieTypeForm(request.POST)
        if(form.is_valid()): 
            post=form.save(commit=True)
            post.save() 
            form=MovieTypeForm()
    else: 
        form=MovieTypeForm
    return render(request, 'movieR/newmovietype.html', {'form':form})

@login_required
def newMovie(request): 
    form=MoviesForm 
    if request.method=='POST': 
        form =MoviesForm(request.POST)
        if(form.is_valid()): 
            post=form.save(commit=True)
            post.save() 
            form=MoviesForm()
    else: 
        form=MoviesForm
    return render(request, 'movieR/newmovie.html', {'form':form})
#required login
@login_required
def newMovieReview(request): 
    form=ReviewsForm 
    if request.method=='POST': 
        form =ReviewsForm(request.POST)
        if(form.is_valid()): 
            post=form.save(commit=True)
            post.save() 
            form=ReviewsForm()
    else: 
        form=ReviewsForm
    return render(request, 'movieR/newmovie.html', {'form':form})   


#start of login/out
def loginmessage(request): 
    return render(request, 'movieR/loginmessage.html')
    
def logoutmessage(request): 
    return render(request, 'movieR/logoutmessage.html')