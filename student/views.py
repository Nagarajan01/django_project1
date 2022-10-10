from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import *
import json


def loginPage(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(request.user)
            return redirect('lists')
        else:
            form = AuthenticationForm()
            messages.info(request, 'username or password is incorrect')
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required()
def registerPage(request):
    # if request.user.is_authenticated:
    #	return redirect('home')
    # else:
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@login_required()
def student_details(request):
    form = Student_detail.objects.all()
    # print(form)
    return render(request, 'accounts/show_details.html', {'form': form})


@login_required()
def add_form(request):
    form = Student_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'accounts/add_student.html', {'data': form})


@login_required()
def show_mark(request, id):
    mar = Mark.objects.filter(roll_no=id).values()
    return render(request, 'accounts/show_mark.html', {'mar': mar})


@login_required()
def update_marks(request, id):

    my_val = Mark.objects.get(id=id)
    mark = Add_mark_form(request.POST or None,
                         request.FILES or None, instance=my_val)
    if mark.is_valid():
        mark = mark.save(commit=False)
        mark.updated_by = (request.user).username
        mark.save()
        return redirect('/')
    return render(request, 'accounts/add_mark.html', {'data': mark})


@login_required()
def add_marks(request):
    form = Add_mark_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        if form.is_valid():
            form = form.save(commit=False)
            form.created_by = (request.user).username
            form.save()
    return render(request, 'accounts/add_mark.html', {'data': form})


@login_required()
def update_student(request, id):
    mar = Student_detail.objects.get(id=id)
    form = Student_form(request.POST or None,
                        request.FILES or None, instance=mar)
    if form.is_valid():
        form.save()
    return render(request, 'accounts/add_mark.html', {'data': form})


def json_view(request):
    student_json = Mark.objects.all().values()
    student_data = list(student_json)
    data = json.dumps(student_data, default=str, indent=1)
    print(type(data))
    return HttpResponse(data, content_type="application/json")
