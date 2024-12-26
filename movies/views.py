from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg
from .models import Movie
from .serializers import MovieSerializer
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["series_title", "director", "genre"]
    ordering_fields = ["imdb_rating", "released_year", "meta_score"]


# Add LoginRequiredMixin to all views
class MovieListView(ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    context_object_name = "movies"
    paginate_by = 10


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"


class MovieCreateView(CreateView):
    model = Movie
    template_name = "movies/movie_form.html"
    fields = [
        "series_title",
        "released_year",
        "certificate",
        "runtime",
        "genre",
        "imdb_rating",
        "overview",
        "meta_score",
        "director",
        "star1",
        "star2",
        "star3",
        "star4",
        "no_of_votes",
        "gross",
    ]
    success_url = reverse_lazy("movie-list")


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = "movies/movie_form.html"
    fields = [
        "series_title",
        "released_year",
        "certificate",
        "runtime",
        "genre",
        "imdb_rating",
        "overview",
        "meta_score",
        "director",
        "star1",
        "star2",
        "star3",
        "star4",
        "no_of_votes",
        "gross",
    ]
    success_url = reverse_lazy("movie-list")


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "movies/movie_confirm_delete.html"
    success_url = reverse_lazy("movie-list")


@api_view(["GET"])
def top_rated_movies(request):
    movies = Movie.objects.filter(imdb_rating__gte=8.0).order_by("-imdb_rating")[:10]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def genre_stats(request):
    genre_data = Movie.objects.values("genre").annotate(
        avg_rating=Avg("imdb_rating"), avg_meta=Avg("meta_score")
    )
    return Response(genre_data)


@api_view(["GET"])
def director_filmography(request, director_name):
    movies = Movie.objects.filter(director__icontains=director_name)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
