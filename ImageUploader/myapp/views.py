from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ImageForm
from .models import Image

# Create your views here.

def index(request):
	if request.method=='POST':
		form=ImageForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	form=ImageForm()
	img=Image.objects.all()
	return render(request,'index.html',{'img':img,'form':form})

def download_file(request,f_id):
	uploaded_file=Image.objects.get(pk=f_id)
	response=HttpResponse(uploaded_file.photo,content_type='application/force-download')
	response['Content-Disposition']=f'attachment;filename="{uploaded_file.photo.name}"'
	return response