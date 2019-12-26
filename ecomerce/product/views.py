from django.shortcuts import render,redirect
from shop.models import Category
from brand.models import Brand
from .models import Product
import json
from .form import ImgForm
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def productadminView(request):
     post=Category.objects.all()
     context={'post':post}
     return render(request,'shop/pages/add_product.html',context)

def add_productView(request):
    if request.method == 'POST':
        print(request.POST)
        pro_title = request.POST.get('pro_title')
        product_desc = request.POST.get('product_desc')
        cat_name = request.POST.get('cat_name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        bran_name = request.POST.get('bran_name')
        status = request.POST.get('status')
        image = request.FILES.get('image')
        Product.objects.create(pro_title=pro_title, product_desc=product_desc, cat_name=cat_name, bran_name=bran_name,
                       price=price, quantity=quantity
                       , status=status, image=image)
        messages.success(request, 'product  add successfully')
        return redirect('/product/manage_product')
    else:
        post = Category.objects.all()
        context = {'post': post}
        return render(request, 'shop/pages/add_product.html', context)

def load_brandView(request):
    cat_name = request.GET.get('cat_name')
    product = Brand.objects.filter(cat_name=cat_name)
    product_list = []
    for data in product:
        products = {
            'id': data.id,
            'bran_name': data.bran_name
        }
        product_list.append(products)
    return HttpResponse(json.dumps(product_list), content_type="application/json")

def manage_productView(request):
    post=Product.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 6)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {'users': users}
    return render(request,'shop/pages/manage_product.html',context)


def edit_productView(request,id):
    if request.method == 'POST':
        print(request.FILES)
        pro_title = request.POST.get('pro_title')
        product_desc = request.POST.get('product_desc')
        cat_name = request.POST.get('cat_name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        bran_name = request.POST.get('bran_name')
        status = request.POST.get('status')
        image = request.FILES.get('image')
        print(image)
        post= Product(id=id,pro_title=pro_title, product_desc=product_desc, cat_name=cat_name, bran_name=bran_name,
                       price=price, quantity=quantity
                       , status=status, image=image)
        post.save()
        messages.success(request, 'product update successfully')
        return redirect('/product/manage_product')
    else:
      form=ImgForm()
      post1=Category.objects.all()
      post=Product.objects.filter(id=id)[0]
      context={'post':post,'post1':post1,'form':form}
      return render(request,'shop/pages/edit_product.html',context)

def delete_proView(request,id):
    Product.objects.filter(id=id).delete()
    messages.success(request,'product delete successfully')
    return redirect('/product/manage_product')