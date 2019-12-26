from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User
# Create your views here.
def loginView(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        user=authenticate(username=name,password=password)
        if user is not None:
            login(request, user)
            
            return redirect('/shop/')
        else:
           messages.error(request, "Invalid Username or Password")
        return redirect('/login')
    else:
        return render(request, 'admin/login.html')
 
def logoutView(request):
    logout(request)
    messages.success(request,'admin loginout successfully')
    return redirect('/login/')