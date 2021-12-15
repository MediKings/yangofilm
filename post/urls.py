from django.urls import path
from .views import Home, DetailPost, Films, Series, Documentaires, Emissions, Tele_realites, Search, Genres, Nouveautes


urlpatterns = [
    path('', Home, name='home'),
    path('search/', Search, name='search'),
    path('genre/<slug:genre>/', Genres, name='genre'),
    path('films/', Films, name='films'),
    path('series/', Series, name='series'),
    path('documentaires/', Documentaires, name='documentaires'),
    path('emissions/', Emissions, name='emissions'),
    path('tele_realites/', Tele_realites, name='tele_realites'),
    path('nouveautes/', Nouveautes, name='nouveautes'),
    path('detail_post/<str:slug>/', DetailPost, name='detail_post'),
]