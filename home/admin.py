from django.contrib import admin

# Register your models here.
from home.models import movie_list,fav_list

admin.site.register(movie_list)
admin.site.register(fav_list)


