from django.urls import path
from . import views

urlpatterns = [
        path('', views.imageView,name='image'),
        path('edit_image/<int:id>',views.editview,name='edit_image')


]