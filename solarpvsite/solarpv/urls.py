from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginview, name='login'),
    path('register/', views.register, name='register'),
    path('portal/', views.portal, name='portal'),
    path('certification/', views.certification, name='certification')
]
