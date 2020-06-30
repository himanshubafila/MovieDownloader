from django.apps import apps
from django.shortcuts import render , redirect , HttpResponse
import random



Movie = apps.get_model('movi' , 'Movie')
Rating = apps.get_model('movi' , 'Rating')
Language = apps.get_model('movi' , 'Language')

def index(request):
    m = Rating.objects.get(rating = 8)
    # m1 = Movie.objects.all()
    m = m.movie.all()
    movie_list = []
    m1 = Language.objects.get(language = "Hindi")

    for i in range(12):
        movie_list.append(random.choice(m1.movie.all()))


    genres = []
    index_c = 0
    for j in range(4):
        index_c = index_c + 1
        count = 0
        l = []

        for i in movie_list[(index_c - 1) * 6: index_c * 6]:
            if i.rating != 'N/A' and i.rating != 'None' and i.rating != " ":
                rating = [j for j in range(int(float(i.rating) // 2))]
            else:
                rating = []
            l.append([i.Movie_name, i.poster, rating, i.year])
            count = count + 1
            # print(i.poster)
            if count == 6:
                break

        genres.append(l)


    featured = []
    while len(featured) != 6:
        random_obj = random.choice(m)
        if random_obj.poster != " " and random_obj.poster != "N/A" and random_obj.poster != "None" and len(random_obj.year) == 4 and int(random_obj.year) > 2015:
            featured.append([random_obj.Movie_name , random_obj.poster , random_obj.year])


    top_downloaded = []
    while len(top_downloaded) != 6:
        random_obj = random.choice(m)
        if random_obj.poster != " " and random_obj.poster != "N/A" and random_obj.poster != "None" and len(
                random_obj.year) == 4 and int(random_obj.year) > 2015:
            top_downloaded.append([random_obj.Movie_name, random_obj.poster, random_obj.year])


    top_rating = []
    while len(top_rating) != 6:
        random_obj = random.choice(m)
        if random_obj.poster != " " and float(random_obj.rating) > 8.7 :
            top_rating.append([random_obj.Movie_name, random_obj.poster, random_obj.year])


    recently_added = []
    while len(recently_added) != 6:
        random_obj = random.choice(m1.movie.all())
        if random_obj.poster != " " and random_obj.poster != "N/A" and random_obj.poster != "None":
            recently_added.append([random_obj.Movie_name, random_obj.poster, random_obj.year])


    popular_movie = []
    index_c = -1
    for i in range(3):
        index_c = index_c + 1
        popular_movie.append([])
        while(len(popular_movie[index_c]) != 6) :
            random_obj = random.choice(m)
            if  random_obj.image != " " and random_obj.poster != " " and random_obj.poster != "N/A" and random_obj.poster != "None":
                img =  random_obj.image.split(", ")[0]
                poster = random_obj.poster
                popular_movie[index_c].append([ random_obj.Movie_name, img , random_obj.release_date , random_obj.genres , poster])

# [[6] , [6], [6]]

    return render(request, 'index.html' , {'genres' : genres, "recently_added" : recently_added ,'featured' : featured , "top_downloaded" : top_downloaded ,"top_rating" : top_rating,'popular' : popular_movie})



