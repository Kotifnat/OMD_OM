from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CBU(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    unit = models.PositiveIntegerField('Рейтинг')
    reach = models.JSONField('Охват')

    def __str__(self):
        return f'{self.user.username} {self.unit}'
