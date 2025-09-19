from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='indexPage'),
    path('register/', views.registerPage, name='registerPage'),
    path('login/', views.loginPage, name='loginPage'),
]