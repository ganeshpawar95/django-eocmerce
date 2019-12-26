from django.urls import path
from .import views

urlpatterns = [
    path('',views.cusloginView , name='cusloginView'),
    path('login',views.loginvalue,name='login')
   
]