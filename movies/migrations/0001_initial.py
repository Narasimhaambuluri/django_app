# Generated by Django 5.0 on 2024-12-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_link', models.URLField(max_length=500)),
                ('series_title', models.CharField(max_length=200)),
                ('released_year', models.IntegerField()),
                ('certificate', models.CharField(max_length=10)),
                ('runtime', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=100)),
                ('imdb_rating', models.FloatField()),
                ('overview', models.TextField()),
                ('meta_score', models.IntegerField()),
                ('director', models.CharField(max_length=100)),
                ('star1', models.CharField(max_length=100)),
                ('star2', models.CharField(max_length=100)),
                ('star3', models.CharField(max_length=100)),
                ('star4', models.CharField(max_length=100)),
                ('no_of_votes', models.IntegerField()),
                ('gross', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]