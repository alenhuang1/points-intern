from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name='add'),
    path('spend', views.spend, name='spend'),
    path('balance', views.balance, name='balance'),
]
