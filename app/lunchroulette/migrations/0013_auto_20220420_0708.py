# Generated by Django 3.0.3 on 2022-04-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunchroulette', '0012_auto_20220419_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lunchgroup',
            name='random_placeses',
        ),
        migrations.AddField(
            model_name='lunchgroup',
            name='random_place',
            field=models.CharField(max_length=200, null=True, verbose_name='random_place'),
        ),
    ]
