from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Movie


class MovieAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            series_title="Test Movie",
            released_year=2020,
            certificate="PG",
            runtime="120 min",
            genre="Action",
            imdb_rating=8.5,
            overview="Test overview",
            meta_score=80,
            director="Test Director",
            star1="Actor 1",
            star2="Actor 2",
            star3="Actor 3",
            star4="Actor 4",
            no_of_votes=1000,
            gross="$1M",
        )

    def test_get_movies(self):
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_top_rated_movies(self):
        response = self.client.get("/api/top-rated/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_genre_stats(self):
        response = self.client.get("/api/genre-stats/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
