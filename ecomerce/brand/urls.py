from django.urls import path
from .import views

urlpatterns = [
    path('',views.brnadadminView , name='brand'),
    path('manage_brnad',views.manage_brnadView , name='manage_brnad'),
    path('edit_brand/<int:id>',views.edit_brnadView , name='edit_brand'),
    path('delete_brand/<int:id>',views.delete_brnadView , name='delete_brand'),

]