from django.urls import path
from . import views
from .models import *

app_name = 'core'
urlpatterns = [
    path('', views.item_list, name='home')
]