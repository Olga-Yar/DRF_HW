# Generated by Django 4.2.1 on 2023-07-27 17:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='студент'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ManyToManyField(blank=True, null=True, to='study.course', verbose_name='курс'),
        ),
    ]