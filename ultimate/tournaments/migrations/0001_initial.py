# Generated by Django 4.1.7 on 2023-03-27 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('contact', models.CharField(default='', max_length=60)),
                ('contact_Mail', models.CharField(blank=True, default='', max_length=80)),
                ('mail', models.CharField(blank=True, default='', max_length=80)),
                ('link', models.CharField(blank=True, default='', max_length=80)),
                ('start_Date', models.DateTimeField()),
                ('end_Date', models.DateTimeField()),
                ('location', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('t', 'Team Tournament'), ('h', 'Hat Tournament'), ('try', 'Tryout'), ('w', 'Workshop')], default='t', max_length=3)),
                ('mode', models.IntegerField(choices=[(4, '4v4'), (5, '5v5'), (7, '7v7')], default=7)),
                ('surface', models.CharField(choices=[('g', 'Grass'), ('b', 'Beach'), ('i', 'Indoor')], default='g', max_length=2)),
                ('gender', models.CharField(choices=[('rm', 'Real mixed'), ('sm', 'Soft mixed'), ('lm', 'Loose mixed'), ('w', 'Women'), ('o', 'Open')], default='rm', max_length=2)),
                ('style', models.CharField(choices=[('fu', 'Fun'), ('co', 'Competitive'), ('be', 'Beginner'), ('yo', 'Youth')], default='fu', max_length=2)),
                ('description', models.TextField(default='', max_length=5000)),
            ],
        ),
    ]
