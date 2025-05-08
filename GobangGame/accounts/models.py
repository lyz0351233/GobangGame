from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    win_rate = models.FloatField(default=0.0)
    rank = models.CharField(max_length=50, default='Newbie')
    contact = models.CharField(max_length=100, blank=True)  # 新增联系方式字段


class GameRecord(models.Model):
    game_id = models.CharField(max_length=100)
    player1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='player1_games')
    player2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='player2_games')
    board_state = models.TextField()
    result = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

