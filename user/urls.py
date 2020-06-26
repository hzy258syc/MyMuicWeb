from django.urls import path
from . import views

urlpatterns = [
    path('login.html', views.loginView, name='login'),
    path('logout.html', views.logoutView, name='logout')

]