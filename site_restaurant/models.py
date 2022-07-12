from django.db import models
from django.forms import CharField


class Mancare(models.Model):
    nume = models.CharField(max_length = 50, default='Doamne ajuta')
    link_poza = models.CharField(max_length= 500, default='Doamne ajuta')

class Feedback(models.Model):
    text = models.CharField(max_length=1000, blank=False)