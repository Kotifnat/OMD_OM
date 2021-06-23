# Generated by Django 3.2.4 on 2021-06-23 08:18

from django.conf import settings
from django.db import migrations, models, transaction
import django.db.models.deletion
import datetime


@transaction.atomic
def create_superuser(apps, schema_editor):
    from django.contrib.auth.models import User
    User.objects.create_superuser(
        username='admin', password='admin', last_login=datetime.datetime.now()
    )
    User.objects.create_user(
        username='test', password='test', last_login=datetime.datetime.now()
    )


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CBU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.PositiveIntegerField(verbose_name='Рейтинг')),
                ('reach', models.CharField(max_length=255, verbose_name='Охват')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                           verbose_name='Пользователь')),
            ],
        ),
        migrations.RunPython(create_superuser, migrations.RunPython.noop)
    ]