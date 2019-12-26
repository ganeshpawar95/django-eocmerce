from django.urls import path
from .import views

urlpatterns = [
    path('',views.sliderView , name='slider'),
    path('manage_slider',views.manage_sliderview,name='manage_slider'),
    path('delete_slider/<int:id>',views.delete_sliderview,name='delete_slider')

]