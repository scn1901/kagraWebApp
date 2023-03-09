from django.urls import path, include
from . import views


app_name = 'graphapp'



urlpatterns = [
    path('', views.index_view, name="home"),
    path('index/', views.index_view, name="index"),
    path('files/', views.files_view, name="files"),
    path('about/', views.about_view, name="about"),
    path('test/', views.test, name="test"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
]
