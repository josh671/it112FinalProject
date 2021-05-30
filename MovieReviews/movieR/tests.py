from django.test import TestCase
from django.contrib.auth.models import User 
from .models import MovieType, Movies, Reviews


# Create your tests here.
#tests all say okay
class MovieTypeTest(TestCase): 
    def setUp(self): 
        self.MovieTypeName = MovieType(MovieTypeName ="Dawn of Dead") 

    def test_typestring(self): 
        self.assertEqual(str(self.MovieTypeName), 'Dawn of Dead')  

    def test_tablename(self): 
         self.assertEqual(str(MovieType._meta.db_table), 'MovieType') 

#tests all say okay
class MoviesTest(TestCase): 
    def setUp(self): 
        self.user=User(username='josh') 
        self.movie=Movies(MovieName='Star', MovieGenre="horror", MovieReviewer=self.user, ReleaseDate='1/10/2021')

    def test_Moviesstring(self): 
        self.assertEqual(str(self.movie), "Star")

    def test_moviestablename(self): 
        self.assertEqual(str(Movies._meta.db_table), 'Movies') 

class Review(TestCase): 
    def setUp(self): 
        self.user=User(username='josh') 
        self.review=Reviews(MovieReview='Reviews', MovieName='Star Wars',MovieReviewerName=self.user ,ReviewDate='1/10/2021')
    
    def test_reviews(self):
        self.assertEqual(str(self.review), "Reviews")
       
    def test_reviewstablename(self): 
        self.assertEqual(str(Reviews._meta.db_table), 'Reviews') 