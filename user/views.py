from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm,UserRregisterForm

# Create your views here.
@login_required
def home(request):

	return render(request,"user/home.html",{})
def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		user = authenticate(username=username,password=password)
		login(request,user)
		if next :
			return redirect(next)
		return redirect('home')
	return render(request , 'user/login.html',{'form':form})


def register_view(request):
	next = request.GET.get('next')
	form = UserRregisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		login(request,user)
		if next :
			return redirect(next)
		return redirect('home')
	context = {
	'form':form ,
	}




	return render(request,'user/register.html',context)
