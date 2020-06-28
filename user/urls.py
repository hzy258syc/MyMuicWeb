from django.urls import path
from . import views

urlpatterns = [
    path('login.html', views.loginView, name='login'),
    path('logout.html', views.logoutView, name='logout'),
    # 用户中心
    path('home/<int:page>.html', views.homeView, name='home')

]