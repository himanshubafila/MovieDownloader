
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('single' , views.singleMovie , name='single'),
    path('genres' , views.genresMovie , name = 'genres'),
    path('page' , views.page , name='page'),
    path('A-Z' , views.AZlist , name = 'A-Z'),
    path('AllMovies' , views.AllMovies , name='AllMovies'),
    path('year' , views.years , name = 'Years'),
    path('feedBackPage' , views.feedBackPage , name = 'feedBackPage'),
    path('feedBack' , views.feedBack , name = 'feedBack'),
    path('search' , views.search , name = 'search'),
    path('news' , views.news , name = 'news'),
    path('language' , views.language , name = 'language')
]
# urlpatterns = urlpatterns + staticfiles_urlpatterns()