from django import forms 
from django.forms import fields 
from .models import MovieType, Movies, Reviews 

class MovieTypeForm(forms.ModelForm): 
    class Meta: 
        model=MovieType 
        fields='__all__' 

class ReviewsForm(forms.ModelForm): 
    class Meta: 
        model=Reviews 
        fields='__all__' 

class MoviesForm(forms.ModelForm): 
    class Meta: 
        model=Movies 
        fields='__all__' 