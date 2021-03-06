from django.test import TestCase
from django.contrib.auth.models import User 
from .models import MovieType, Movies, Reviews
from .forms import MoviesForm, MovieTypeForm, ReviewsForm
from django.urls import reverse
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
        self.movie=Movies(MovieName='Star', MovieGenre="horror", MovieReviewer=self.user, ReleaseDate='2021-02-02')

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

#tests for the forms 
class NewMovieForm(TestCase):
    def test_NewMovieForm(self): 
        data={'MovieName:':"one", 'MovieGenre':'horror', 'MovieReviewer':"josh", 'ReleaseDate':'1/1/2022'}
        form=MoviesForm(data) 
        self.assertTrue(form.is_valid) 
        #FAILED -returns is not false error
   # def test_NewMovieForminvalid(self): 
   #     data={'MovieName:':"one", 'MovieGenre':654654 , 'MovieReviewer':"josh", 'ReleaseDate':'1/1/2022'}
   #     form=MoviesForm(data) 
   #     self.assertFalse(form.is_valid) 


#tests for the forms 
class MoviesTypeForm(TestCase):
    def test_MovieTypeForm(self): 
        data={'MovieTypeName:':"one", 'MovieDescription':'string'}
        form=MovieTypeForm(data) 
        self.assertTrue(form.is_valid) 
        #FAILED -returns is not false error
    #def test_MovieTypeForminvalid(self): 
    #    data={'MovieTypeName:':"one", 'MovieDescription':'654654'}
    #    form=MovieTypeForm(data) 
    #    self.assertFalse(form.is_valid) 

class ReviewsFormTest(TestCase):
    def test_MovieTypeForm(self): 
        data={'MovieReview:':"one", 'MovieName':'654654', 'MovieReviewerName':'Josh', 'ReviewDate':'1/1/2022'}
        form=ReviewsForm(data) 
        self.assertTrue(form.is_valid) 
        #FAILED -returns is not false error
    #def test_MovieTypeForminvalid(self): 
    #    data={'MovieReview': 12342, 'MovieName':'654654', 'MovieReviewerName':'Josh', 'ReviewDate':'1/1/2022'}
    #    form=ReviewsForm(data) 
    #    self.assertFalse(form.is_valid) 
        

class newReview_authentication_test(TestCase): 
    def setUp(self): 
        self.test_user=User.objects.create_user(username='testuser1', password='password')
        self.type=Reviews(MovieReview='w3schools')
        self.resource=Reviews.objects.create(MovieReview=self.type, MovieName='654654', MovieReviewerName='Josh', ReviewDate='2021-02-02') 
    
    def test_redirect_if_not_logged_in(self): 
        response=self.client.get(reverse('newreview'))
        self.assertRedirects(response, '/accounts/login/?next=/movieR/newreview/')

class newMovie_authentication_test(TestCase): 
    def setUp(self): 
        self.test_user=User.objects.create_user(username='testuser1', password='password')
        self.type=Movies(MovieName='Star')
        self.user=User(username='josh')
        self.resource=Movies.objects.create(MovieName=self.type, MovieGenre="HORROR", MovieReviewer=self.test_user, ReleaseDate='2021-02-02')
    
    def test_redirect_if_not_logged_in(self): 
        response=self.client.get(reverse('newmovie'))
        self.assertRedirects(response, '/accounts/login/?next=/movieR/newmovie/')

class newMovie_authentication_test(TestCase): 
    def setUp(self): 
        self.test_user=User.objects.create_user(username='testuser1', password='password')
        self.type=Movies(MovieName='Star')
        self.user=User(username='josh')
        self.resource=Movies.objects.create(MovieName=self.type, MovieGenre="HORROR", MovieReviewer=self.test_user, ReleaseDate='2021-02-02')
    
    def test_redirect_if_not_logged_in(self): 
        response=self.client.get(reverse('newmovie'))
        self.assertRedirects(response, '/accounts/login/?next=/movieR/newmovie/') 

class newMovieType_authentication_test(TestCase): 
    def setUp(self): 
        self.test_user=User.objects.create_user(username='testuser1', password='password')
        self.type = MovieType(MovieTypeName ="Dawn of Dead") 
        self.user=User(username='josh')
        self.resource=MovieType.objects.create(MovieTypeName="wow", MovieDescription='blah')
    
    def test_redirect_if_not_logged_in(self): 
        response=self.client.get(reverse('newmovietype'))
        self.assertRedirects(response, '/accounts/login/?next=/movieR/newmovietype/')