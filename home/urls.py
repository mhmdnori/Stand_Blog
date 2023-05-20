from django.urls import path
from .views import *

urlpatterns = [
    path('', Homeview.as_view(), name='home')
]