from django.shortcuts import render
from django.views.generic import  TemplateView


class Homeview(TemplateView):
    template_name = 'home/home.html'
# Create your views here.
