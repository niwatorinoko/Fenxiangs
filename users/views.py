from django.shortcuts import render
from django.views import generic
from users.models import Account
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import AccountForm, AddAccountForm # ユーザーアカウントフォーム
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .forms import LoginForm
from . import forms

# Create your views here.
class TopView(TemplateView):
    template_name = "users/top.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "users/home.html"

class LoginView(LoginView):
    """ログインページ"""
    form_class = forms.LoginForm
    template_name = "users/login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = "users/login.html"

class  AccountRegistration(TemplateView):

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
            return render(request, 'users/home.html')
        else:
            context = {
                'account_form': account_form,
                'add_form': add_form,
            }
            return render(request, 'users/register.html', context)