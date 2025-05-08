from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False, verbose_name='管理员')
    contact = models.CharField(max_length=100, blank=True, verbose_name='联系方式')
    win_rate = models.FloatField(default=0.0, verbose_name='胜率')
    rank = models.CharField(max_length=50, default='Newbie', verbose_name='段位')
    image = models.ImageField(upload_to='user_images/', blank=True, null=True, verbose_name='头像')  # 添加头像字段

class GameRecord(models.Model):
    USER_CHOICES = [('AI', 'AI'), ('FRIEND', '好友')]
    RESULT_CHOICES = [('WIN', '胜利'), ('LOSE', '失败'), ('DRAW', '平局')]

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='game_records',
        verbose_name='用户'
    )
    opponent_type = models.CharField(
        max_length=10,
        choices=USER_CHOICES,
        default='AI',
        verbose_name='对手类型'
    )
    match_time = models.DateTimeField(
        default=timezone.now,
        verbose_name='对战时间'
    )
    result = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        verbose_name='结果'
    )

    class Meta:
        verbose_name = '游戏记录'
        verbose_name_plural = '游戏记录管理'
        ordering = ['-match_time']