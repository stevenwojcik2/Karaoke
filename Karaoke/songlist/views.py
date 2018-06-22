from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from songlist.models import Artist, Album, Track

# Create your views here.

class ArtistListView(ListView):
	model = Artist

class ArtistDetailView(DetailView):
	model = Artist

class ArtistCreate(CreateView):
	model = Artist
	fields = ['name', 'image']

# class ArtistUpdate(UpdateView):
# 	model = Artist
# 	fields = ['name', 'image']
# 	template_name_suffix = '_update_form'

# class ArtistDelete(DeleteView):
# 	model = Artist
# 	success_url = reverse_lazy('artist-list')

# class AlbumListView(ListView):
	# model = Album

class AlbumDetailView(DetailView):
	model = Album

class TrackDetailView(DetailView):
	model = Track

class AlbumCreate(CreateView):
	model = Album
	fields = ['title', 'artwork' 'release_date', 'artist']

# class AlbumUpdate(UpdateView):
# 	model = Album
# 	fields = ['title', 'artwork' 'release_date', 'artist']
# 	template_name_suffix = '_update_form'

# class AlbumDelete(DeleteView):
# 	model = Artist
# 	success_url = reverse_lazy('album-list')



