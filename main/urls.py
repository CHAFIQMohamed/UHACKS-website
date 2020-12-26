from django.urls import path
from .views import home,sign_up

urlpatterns=[
#path 1 content home page when we tape for example name.com 
path("",home, name="home"),
#path 2 content sin_up
path("sign_up/",sign_up, name="sign_up"),
]