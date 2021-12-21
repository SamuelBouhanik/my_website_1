from django.urls import path
from . import views

urlpatterns = [
    path('' , views.Display_homepage , name = 'home'),
    path('info',views.Display_info , name = 'info'),
]