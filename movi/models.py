from django.db import models
from django.contrib import admin

# Create your models here.

class MovAdmin(admin.ModelAdmin):
    list_display = ('sno' , 'Movie_name' , 'genres', 'year' , 'language' , 'rating')
    search_fields = ('Movie_name' , 'year' , 'rating' , 'language' ,  'genres')


class Movie(models.Model):
    sno = models.AutoField(primary_key = True)
    Movie_name = models.CharField(max_length=50 , default=" ")
    year = models.CharField(max_length=20 , default=" ")
    genres = models.CharField(max_length = 50 , default=" ")
    cast = models.CharField(max_length=100000000 , default=" ")
    language = models.CharField(max_length = 10000 , default=" ")
    type = models.CharField(max_length=50 , default=" ")
    desc = models.CharField(max_length=100000000 , default=" ")
    awards = models.CharField(max_length=200 , default=" ")
    boxoffice = models.CharField(max_length=200 , default=" ")
    link = models.CharField(max_length=100000000 , default=" ")
    poster = models.CharField(max_length=10000000 , default=" ")
    image = models.CharField(max_length=100000000, default=" ")
    trailer = models.CharField(max_length=10000000 , default=" ")
    rating = models.CharField(max_length=20 , default=" ")
    director = models.CharField(max_length=1000 , default=" ")
    writer = models.CharField(max_length=1000 , default=" ")
    release_date = models.CharField(max_length=50 , default=" ")


    def __str__(self):
        return self.Movie_name


class YearAdmin(admin.ModelAdmin):
    list_display = ('year' , 'no_of_movies')


class Year(models.Model):
    year = models.CharField(max_length=20 , default=" ")
    movie = models.ManyToManyField(Movie , related_name="YearMovies" , blank=True)
    no_of_movies = models.IntegerField(default=0)

    def __str__(self):
        return self.year


class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating' , 'no_of_movies')


class Rating(models.Model):
    rating = models.CharField(max_length=20 , default=" ")
    movie = models.ManyToManyField(Movie , related_name="RatingMovies" , blank=True)
    no_of_movies = models.IntegerField(default=0)

    def __str__(self):
        return self.rating


class GenresAdmin(admin.ModelAdmin):
    list_display = ('genres' , 'no_of_movies')


class Genres(models.Model):
    genres = models.CharField(max_length=20 , default=" ")
    movie = models.ManyToManyField(Movie ,related_name="GenresMovies" ,blank=True)
    no_of_movies = models.IntegerField(default=0)

    def __str__(self):
        return self.genres


class FeedBack(models.Model):
    First_Name = models.CharField(max_length=500 , default=" ")
    Last_Name = models.CharField(max_length=500 , default=" ")
    email = models.CharField(max_length=1000 , default=" ")
    subject = models.CharField(max_length=1000 , default=" ")
    message = models.CharField(max_length=1000000, default=" ")


    def __str__(self):
        return self.First_Name


class Series(models.Model):
    Series_name = models.CharField(max_length=10000 , default=" ")
    year = models.CharField(max_length=20, default=" ")
    genres = models.CharField(max_length=50, default=" ")
    cast = models.CharField(max_length=100000000, default=" ")
    language = models.CharField(max_length=10000, default=" ")
    type = models.CharField(max_length=50, default=" ")
    desc = models.CharField(max_length=100000000, default=" ")
    awards = models.CharField(max_length=200, default=" ")
    boxoffice = models.CharField(max_length=200, default=" ")
    link = models.CharField(max_length=1000000000 , default=" ")
    poster = models.CharField(max_length=10000000, default=" ")
    image = models.CharField(max_length=100000000, default=" ")
    trailer = models.CharField(max_length=10000000, default=" ")
    rating = models.CharField(max_length=20, default=" ")
    director = models.CharField(max_length=1000, default=" ")
    writer = models.CharField(max_length=1000, default=" ")
    release_date = models.CharField(max_length=50, default=" ")


    def __str__(self):
        return self.Series_name


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language' , 'no_of_movies')


class Language(models.Model):
    language = models.CharField(max_length=20, default=" ")
    movie = models.ManyToManyField(Movie, related_name="LanguageMovies", blank=True)
    no_of_movies = models.IntegerField(default=0)

    def __str__(self):
        return self.language