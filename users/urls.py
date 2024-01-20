#from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'users'
urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('register/', views.AccountRegistration.as_view(), name='register'),
]