from typing import Any
from django.shortcuts import render
from django.views import generic
from users.models import Account
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from .forms import AccountForm, AddAccountForm # ユーザーアカウントフォーム
from django.contrib.auth import authenticate
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm
from . import forms

# Create your views here.
class TopView(TemplateView):
    template_name = "users/top.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "users/home.html"

class LoginView(FormView):
    """ログインページ"""
    form_class = UserLoginForm
    template_name = "users/login.html"

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(request.POST)
        if user:
            account = Account.objects.get(user=user)
            context = {
                'user_name' : user.username,
                'user_email' : user.email,
                'user_icon_image' : account.icon_image,
                'user_graduate_at' : account.graduate_at,
                'user_graduate_at_summer' : account.graduate_at_summer,
            }
            return render(request, 'users/home.html', context)
        else:
            return render(request, 'users/login.html')
        

class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = "users/login.html"

class AccountRegistration(TemplateView):

    def get(self, request, *args, **kwargs):
        context = {
            'account_form': AccountForm(),
            'add_form': AddAccountForm(),
        }
        return render(request, 'users/register.html', context)
    
    def post(self, request):
        add_form = AddAccountForm(request.POST, request.FILES, prefix='add')
        account_form = AccountForm(request.POST, prefix='account')

        if account_form.is_valid() and add_form.is_valid():
            new_account = account_form.save()
            new_add = add_form.save(commit=False)
            new_add.user = new_account
            new_add.save()
            context = {
                'user_name' : new_add.user.username,
                'user_email' : new_add.user.email,
                'user_icon_image' : new_add.icon_image,
                'user_graduate_at' : new_add.graduate_at,
                'user_graduate_at_summer' : new_add.graduate_at_summer,
            }
            return render(request, 'users/home.html', context)
        else:
            context = {
                'account_form': account_form,
                'add_form': add_form,
            }
            return render(request, 'users/register.html', context)
        
