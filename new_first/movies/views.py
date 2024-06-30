from django.shortcuts import render
from rest_framework import generics,permissions,viewsets
from django_filters.rest_framework import DjangoFilterBackend

from . import models
from .models import Movie,Actor,Review
from  .serializers import (MovieListSerializer,MovieDetailSerializer,ReviewCreateSerializer,
                           CreateRatingSerializer,ActorListSerializer,ActorDetailSerializer)

from .service import get_client_ip, MovieFilter, PaginationMovies



class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод из списка фильмов"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter
    pagination_class = PaginationMovies


    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count('rattings', filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))

        )

        return movies

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        elif self.action == 'retrieve':
            return MovieDetailSerializer



class ReviewCreateViewSet(viewsets.ModelViewSet):
    """Добавление отзыва к фильму"""
    serializer_class = ReviewCreateSerializer



class AddStarRatingViewSet(viewsets.ModelViewSet):
    """Добавление рейтинга к фильму"""
    serializer_class = CreateRatingSerializer


    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


class ActorsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод актёров и режиссёров"""
    queryset = Actor.objects.all()


    def get_serializer_class(self):
        if self.action == 'list':
            return ActorListSerializer
        elif self.action == 'retrieve':
            return ActorDetailSerializer
