from django.urls import path
from . import views

urlpatterns = [
    path('reponces', views.see_reponces ,name ='reponces')
]