from django.shortcuts import render,get_object_or_404,redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from product.models import Product
from .forms import CartAddProductForm


@require_POST
def cart_add(request,id):
	cart=Cart(request)
	product=get_object_or_404(Product,id=id)
	form=CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'])
		print(cart)
	return redirect('/cart/cart_detail')
def cart_remove(request,id):
	cart=Cart(request)
	product = get_object_or_404(Product, id=id)
	cart.remove(product)
	return redirect('/cart/cart_detail')

def cart_detail(request):
	cart = Cart(request)
	for item in cart:
		print(item)
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
	return render(request, 'carts/detail.html', {'cart': cart})

