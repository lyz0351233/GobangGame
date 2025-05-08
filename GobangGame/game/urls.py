from django.urls import path
from.views import game_home, game_match, game_play, game_record

urlpatterns = [
    path('', game_home, name='game_home'),
    path('match/', game_match, name='game_match'),
    path('play/', game_play, name='game_play'),
    path('record/', game_record, name='game_record'),
]