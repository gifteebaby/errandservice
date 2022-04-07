from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name="home"),
     path('service', views.service, name="service"),
     path('about', views.about, name="about"),
     path('login', views.login, name="login"),
     path('signup', views.signup, name="signup"),
     path('outline', views.outline, name='outline'),
]
