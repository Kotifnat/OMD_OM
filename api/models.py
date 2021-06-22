from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CBU(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    unit = models.PositiveIntegerField('Рейтинг')
    reach = models.CharField('Охват', max_length=255)

    def __str__(self):
        return f'{self.user.username} {self.unit}'
