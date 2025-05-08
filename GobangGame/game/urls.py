# from django.urls import path
# from.views import game_home, game_match, game_play, game_record
#
# urlpatterns = [
#     path('', game_home, name='game_home'),
#     path('match/', game_match, name='game_match'),
#     path('play/', game_play, name='game_play'),
#     path('record/', game_record, name='game_record'),
# ]
from django.urls import path
from .views import user_dashboard, game_home, game_match, game_play, game_record, contact_change, image_change

urlpatterns = [
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    path('game_home/', game_home, name='game_home'),
    path('game_match/', game_match, name='game_match'),
    path('game_play/', game_play, name='game_play'),
    path('game_record/', game_record, name='game_record'),
    path('contact_change/', contact_change, name='contact_change'),
    path('image_change/', image_change, name='image_change'),
]