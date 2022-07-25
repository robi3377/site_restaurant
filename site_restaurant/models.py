from django.db import models
from django.forms import CharField


class Mancare(models.Model):
    nume = models.CharField(max_length = 50, default='')
    link_poza = models.CharField(max_length= 500, default='')

class Feedback(models.Model):
    text = models.CharField(max_length=1000, blank=False)
