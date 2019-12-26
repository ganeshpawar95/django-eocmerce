from django.shortcuts import render,redirect
from .models import Login
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def cusloginView(request):
	if request.method=='POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		password=request.POST.get('password')
		Login.objects.create(name=name,email=email,password=password)
		messages.success(request, 'user sign up succssfully')
		return redirect('/cus_login/')
	else:
	    return  render(request,'login/login.html')


def loginvalue(request):
	if request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('password')
		emplooye = Login.objects.filter(email=email, password=password)
		if emplooye:
			email = request.POST['email']
			request.session['email'] = email
			messages.success(request,email)
			return redirect('/website/')
		else:
			messages.error(request, 'Email and password not found')
			return redirect('cus_login')
	else:
	  return  render(request,'login/login.html')

