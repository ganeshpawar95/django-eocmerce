from django.shortcuts import render
from .models import Image
from django.http import HttpResponse  
from .form import ImgForm  
# Create your views here.
def imageView(request):
	if request.method=='POST':
		image = request.FILES.get('image')
		post=Image(image=image)
		post.save()
		return HttpResponse('image insert')
	else:
		post=Image.objects.all()
		return render(request, 'web/image.html', {'post': post})

def editview(request,id):
	if request.method=='POST':
		print(request.POST)
		image=request.FILES.get('image')
		image=Image(image=request.FILES['image'])
		post=Image(id=id,image=image)
		post.save()
		return HttpResponse('image update')
	else:
		form = ImgForm()  
		post=Image.objects.filter(id=id)[0]
		return render(request, 'web/edit_image.html',{'post': post,'form':form})