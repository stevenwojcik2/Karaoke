from django.contrib import admin
from songlist.models import Artist, Album, Track

# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)