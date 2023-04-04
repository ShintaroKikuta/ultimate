from email.policy import default
from django.db import models

# Create your models here.
from django.urls import reverse


class Tournament(models.Model):
    title = models.CharField(max_length=60)
    contact = models.CharField(max_length=60, default='')
    contact_Mail = models.CharField(max_length=80, default='', blank=True)
    mail = models.CharField(max_length=80, default='', blank=True)
    link = models.CharField(max_length=80, default='', blank=True)
    start_Date = models.DateTimeField()
    end_Date = models.DateTimeField()
    location = models.CharField(max_length=30)
    TYPE_CHOICES = (
        ('t', 'Team Tournament'),
        ('h', 'Hat Tournament'),
        ('try', 'Tryout'),
        ('w', 'Workshop'),
    )
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, default='t')
    MODE_CHOICES = (
        (4, '4v4'),
        (5, '5v5'),
        (7, '7v7'),
    )
    mode = models.IntegerField(choices=MODE_CHOICES, default=7)
    SURFACE_CHOICES = (
        ('g', 'Grass'),
        ('b', 'Beach'),
        ('i', 'Indoor'),
    )
    surface = models.CharField(max_length=2, choices=SURFACE_CHOICES, default='g')
    GENDER_CHOICES = (
        ('rm', 'Real mixed'),
        ('sm', 'Soft mixed'),
        ('lm', 'Loose mixed'),
        ('w', 'Women'),
        ('o', 'Open'),
        #('wo', "Women, Open"),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='rm')
    STYLE_CHOICES = (
        ('fu', 'Fun'),
        ('co', 'Competitive'),
        ('be', 'Beginner'),
        ('yo', 'Youth'),

    )
    style = models.CharField(max_length=2, choices=STYLE_CHOICES, default='fu')
    description = models.TextField(max_length=5000, default="")
    approved = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tournaments')
