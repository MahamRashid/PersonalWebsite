from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name='Home'),
    path('page2', views.about, name='About')
]