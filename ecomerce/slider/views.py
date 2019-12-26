from django.shortcuts import render
from .models import Slider
from django.http import HttpResponse  
from .form import sliderForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def sliderView(request):
	if request.method=='POST':
		slider_title = request.POST.get('slider_title')
		slider_dsc = request.POST.get('slider_dsc')
		slider_image =request.FILES.get('slider_image')
		post=Slider(slider_title=slider_title,slider_dsc=slider_dsc,slider_image=slider_image)
		post.save()
		return HttpResponse('add slider')
	else:
		form = sliderForm()
		return render(request, 'slider/add_slider.html', {'form': form})


def manage_sliderview(request):
    post=Slider.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 6)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {'users': users}
    
    return render(request,'slider/manage_slider.html',context)

def delete_sliderview(request,id):
	Slider.objects.filter(id=id).delete()
	return HttpResponse('delete slider')
 