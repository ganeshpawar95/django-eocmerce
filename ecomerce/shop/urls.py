from django.urls import path
from .import views

urlpatterns = [
    path('',views.shopadminView , name='shopadmin'),
    path('add_cat',views.addcatView , name='addcat'),
    path('manage_cat',views.manage_catView , name='manage_cat'),
    path('edit_cat/<int:id>',views.edit_catView , name='edit_cat'),
    path('delete_cat/<int:id>',views.delete_catView , name='delet_cat'),
]