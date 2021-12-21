from django.urls import path
from . import views

urlpatterns = [
    path('livre',views.display_livre_dor,name = 'livre'),
    path('livre_form' ,views.display_livre_form , name = 'livre_form'),
]