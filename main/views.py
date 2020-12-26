from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import participant
from .forms import partiform
from django.contrib import messages
# Create your views here.
#landing page home page
def home(request):
	return render(request,'home.html')
#/sign un path

def sign_up(request):
	if request.method == "POST":
		form = partiform(request.POST or None)
		if form.is_valid():
			form.save()
			#print('hello')
		return render(request,'home.html',{})
	else:
		form = partiform()
		return render(request,'indexform.html',{'form':form} )