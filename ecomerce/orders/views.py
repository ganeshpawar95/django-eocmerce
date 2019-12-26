from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
def orederView(request):
	return render(request,'orders/created.html')


def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				OrderItem.objects.create(
					Shipping=order,
					product=item['product'],
					price=item['price'],
					quantity=item['quantity']
				)
			cart.clear()
		return render(request, 'orders/created.html', {'order': order})
	else:
		form = OrderCreateForm()
	return render(request, 'orders/order_create.html', {'form': form})
	