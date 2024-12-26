from django.db import models


class Movie(models.Model):
    poster_link = models.URLField(max_length=500)
    series_title = models.CharField(max_length=200)
    released_year = models.IntegerField()
    certificate = models.CharField(max_length=10)
    runtime = models.CharField(max_length=20)
    genre = models.CharField(max_length=100)
    imdb_rating = models.FloatField()
    overview = models.TextField()
    meta_score = models.IntegerField()
    director = models.CharField(max_length=100)
    star1 = models.CharField(max_length=100)
    star2 = models.CharField(max_length=100)
    star3 = models.CharField(max_length=100)
    star4 = models.CharField(max_length=100)
    no_of_votes = models.IntegerField()
    gross = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.series_title
