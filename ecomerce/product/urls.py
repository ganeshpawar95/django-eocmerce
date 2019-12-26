from django.urls import path
from .import views

urlpatterns = [
    path('',views.productadminView , name='product'),
    path('add_product',views.add_productView , name='add_product'),
    path('load_brand',views.load_brandView , name='load_brand'),
    path('manage_product',views.manage_productView,name='manage_product'),
    path('edit_product/<int:id>',views.edit_productView ,name='edit_product'),
    path('delete_product/<int:id>', views.delete_proView,name='delete_pro'),
]