from django.shortcuts import render

# Create your views here.
#5-24-2021
def index(request): 
    return render(request, 'movieR/index.html') 