from django.db import models

class NetflixShow(models.Model):
    show_id = models.CharField(max_length=10, unique=True)
    show_type = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255, blank=True, null=True)
    cast = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    rating = models.CharField(max_length=10, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    listed_in = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

