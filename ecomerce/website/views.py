from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils import timezone
from product.models import Product
from slider.models import  Slider
from cart.forms import CartAddProductForm
def indexView(request):
	slider=Slider.objects.all()
	products=Product.objects.all()
	context={'products':products,
			 'slider':slider}
	return render(request,'web/pagesweb/home.html',context)

def product_detilsView(request,id):
	form=CartAddProductForm()
	post=Product.objects.filter(id=id)[0]
	context={'post':post,'form':form}
	return render(request,'web/pagesweb/products_detels.html',context)

