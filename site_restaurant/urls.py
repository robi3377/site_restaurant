from django import views
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('feedback', views.feedback, name='feedback')

]