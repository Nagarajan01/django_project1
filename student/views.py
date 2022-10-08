from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import *

def registerPage(request):
	#if request.user.is_authenticated:
	#	return redirect('home')
	#else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:	
			login(request, user)
			return redirect('home')
		else:
			form = AuthenticationForm()
			messages.info(request, 'Username OR password is incorrect')
			return render(request,'accounts/login.html',{'form':form})
	else:
		form = AuthenticationForm()
		return render(request, 'accounts/login.html', {'form':form})

def logoutUser(request):
	logout(request)
	return redirect('login')

def student_details(request):
    form = student_detail.objects.all()
	#print(form)
    return render(request, 'accounts/show_details.html', {'form': form})

def add_form(request):

    form = Student_form(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
    return render(request, 'accounts/add_student.html', {'data':form})

