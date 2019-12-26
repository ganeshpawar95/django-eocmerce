from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils import timezone
from .models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

def shopadminView(request):
    return render(request,'shop/pages/home.html')


def addcatView(request):
    if request.method =='POST':
        post=Category(cat_name=request.POST.get('cat_name'))
        post.save()
        messages.success(request,'category add successfully')
        return redirect('/shop/manage_cat')
    else:
        return render(request,'shop/pages/add_cat.html')

def manage_catView(request):
    post=Category.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context={'users':users}
    return  render(request ,'shop/pages/manage_cat.html',context)

def edit_catView(request,id):
    if request.method =='POST':
        cat_name = request.POST.get('cat_name')
        Category.objects.filter(id=id).update(cat_name=cat_name)
        messages.success(request, 'category  Update SucessFully')
        return redirect('/shop/manage_cat')
    else:
      post = Category.objects.filter(id=id)[0]
      context = {'post': post}
      return render(request, 'shop/pages/edit_cat.html', context)


def delete_catView(request,id):
   Category.objects.filter(id=id).delete()
   messages.success(request, 'category  Delete SucessFully')
   return redirect('/shop/manage_cat')
