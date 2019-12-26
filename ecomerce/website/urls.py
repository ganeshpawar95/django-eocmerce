from django.urls import path
from .import views

urlpatterns = [
    path('',views.indexView , name='index'),
     path('product_detils/<int:id>',views.product_detilsView , name='product_detils'),
]