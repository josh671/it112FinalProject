from django.db import models
#import User as a model
from django.contrib.auth.models import User
from django.db.models.fields import DateField
# Create your models here.

class MovieType(models.Model): 
    MovieTypeName=models.CharField(max_length=255)
    MovieDescription=models.TextField(null=True, blank=True)

    def __str__(self): 
        return self.MovieTypeName

    class Meta: 
        db_table="MovieType" 

class Movies(models.Model): 
    MovieName=models.CharField(max_length=255)
    MovieGenre=models.CharField(max_length=100) 
    MovieReviewer=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ReleaseDate=models.DateField() 
    
    def __str__(self): 
        return self.MovieName 

    class Meta: 
        db_table="Movies" 

class Reviews(models.Model): 
    MovieReview=models.TextField()
    Movieid=models.ForeignKey(Movies, on_delete=models.CASCADE)
    ReviewDate=DateField() 

    def __str__(self): 
        return self.MovieReview 

    class Meta: 
        db_table='Reviews'