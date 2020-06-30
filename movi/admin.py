from django.contrib import admin
from .models import Movie , MovAdmin , Year , Rating , Language , Genres , YearAdmin , GenresAdmin , RatingAdmin, FeedBack , Series , LanguageAdmin
# Register your models here.
admin.site.register(Movie , MovAdmin)
admin.site.register(Year , YearAdmin)
admin.site.register(Rating , RatingAdmin)
admin.site.register(Genres , GenresAdmin)
admin.site.register(FeedBack)
admin.site.register(Series)
admin.site.register(Language , LanguageAdmin)