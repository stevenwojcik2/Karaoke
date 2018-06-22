from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Artist(models.Model):
	name = models.CharField(max_length=1000, unique=True)
	image = models.ImageField(upload_to='songlist',blank=True)

	def __str__(self):
		return str(self.name)

	def get_absolute_url(self):
		return reverse('artist-detail', kwargs={'pk':self.pk})

class Album(models.Model):
	title = models.CharField(max_length=1000, blank=True)
	artwork = models.ImageField(upload_to='songlist', blank=True)
	release_date = models.DateField(blank=True)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE,)

	def __str__(self):
		return str(self.title)

	def get_absolute_url(self):
		return reverse('album-detail', kwargs={'pk':self.pk})

class Track(models.Model):
	title = models.CharField(max_length=1000)
	song_number = models.SlugField(max_length=10, unique=True)
	count = models.IntegerField(blank=True,null=True)
	lyrics = models.TextField(blank=True)
	is_foreign_language = models.BooleanField(blank=True, default=False)
	# album = models.ForeignKey(Album, on_delete=models.CASCADE, default=1)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE,)

	def __str__(self):
		return str(self.title)

	def get_absolute_url(self):
		return reverse('track-detail', kwargs={'pk':self.pk})

	
