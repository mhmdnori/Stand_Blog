from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import login, authenticate


class Loginview(View):
    template_name = 'account/login.html'

    def get(self, request):
        return render(request, 'account/login.html')

    def post(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'account/login.html', {'error': 'اطلاعات ورود اشتباه است.'})

# Create your views here.
