from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils import timezone
from .models import Brand
from  shop.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def brnadadminView(request):
    if request.method == 'POST':
        cat_name=request.POST.get('cat_name')
        bran_name=request.POST.get('bran_name')
        post= Brand(cat_name=cat_name,bran_name=bran_name)
        post.save()
        messages.success(request, 'Brand add successfully')
        return redirect('/brand/manage_brnad')
    else:
     post=Category.objects.all()
     conetext={'post':post}
     return render(request,'shop/pages/add_brand.html',conetext)


def manage_brnadView(request):
    post=Brand.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {'users': users}
    return render(request ,'shop/pages/manage_brand.html',context)

def edit_brnadView(request,id):
    if request.method == 'POST':
        cat_name=request.POST.get('cat_name')
        bran_name=request.POST.get('bran_name')
        Brand.objects.filter(id=id).update(cat_name=cat_name,bran_name=bran_name)
        messages.success(request, 'Brand edit successfully')
        return redirect('/brand/manage_brnad')
    else:
     post=Category.objects.all()
     posts=Brand.objects.filter(id=id)[0]
     conetext={'post':post,
               'post1':posts}
     return render(request,'shop/pages/edit_brand.html',conetext)

def delete_brnadView(request,id):
    Brand.objects.filter(id=id).delete()
    messages.success(request, 'Brand delete successfully')
    return redirect('/brand/manage_brnad')