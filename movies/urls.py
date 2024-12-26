from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
)

router = DefaultRouter()
router.register(r"movies", views.MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("top-rated/", views.top_rated_movies),
    path("genre-stats/", views.genre_stats),
    path("director/<str:director_name>/", views.director_filmography),
    path("movies", MovieListView.as_view(), name="movie-list"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("movie/new/", MovieCreateView.as_view(), name="movie-create"),
    path("movie/<int:pk>/update/", MovieUpdateView.as_view(), name="movie-update"),
    path("movie/<int:pk>/delete/", MovieDeleteView.as_view(), name="movie-delete"),
]
