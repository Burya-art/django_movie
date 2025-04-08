from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Movie


class MoviesView(ListView):
    """Список фільмів"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"


class MovieDetailView(DetailView):
    """Повний опис фільму"""

    model = Movie
    slug_field = "url"


class AddReview(View):
    """Відгуки"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie_id = pk
            form.save()
        return redirect(movie.get_absolute_url())
