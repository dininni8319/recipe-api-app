# Generated by Django 3.0.3 on 2022-04-13 16:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('lunchroulette', '0003_remove_lunchgroup_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPartecipats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='lunchgroup',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.User', verbose_name='admin_id'),
        ),
        migrations.AlterField(
            model_name='lunchgroup',
            name='number_people',
            field=models.IntegerField(blank=True, default=1, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)]),
        ),
    ]
