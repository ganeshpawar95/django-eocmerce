from django.urls import path
from .import views

urlpatterns = [
    path('',views.orederView , name='orders'),
    path('order_create',views.order_create,name='order_create')
    
]