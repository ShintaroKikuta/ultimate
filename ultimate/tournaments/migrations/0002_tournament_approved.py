# Generated by Django 4.1.7 on 2023-04-02 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]