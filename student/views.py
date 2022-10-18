from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core import serializers


from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count

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


def json_view(request, id):

    detail_Mark_json = Mark.objects.filter(
        roll_no__roll_number=id).annotate().values()
    #student_json = Student_detail.objects.all().values()
    student_json = Student_detail.objects.filter(id=id).values()
    Mark_json = Mark.objects.filter(
        roll_no__roll_number=id).aggregate(Sum('mark')).values()
    mydict = {}
    mydict['Total_Mark'] = tuple(Mark_json)
    my_json = json.dumps(list(mydict))
    print(mydict)
    all_json = list(student_json) + list(detail_Mark_json) + list([mydict])
    #all_json = list([Mark_json] , [student_json])
    print(all_json)
    data = json.dumps(all_json, default=str, indent=1)
    print(type(data))
    return HttpResponse(data, content_type="application/json")


def json_view(request, id):
    detail_Mark_json = Mark.objects.filter(
        roll_no__roll_number=id).annotate().values()
    student_json = Student_detail.objects.filter(id=id).values()
    Mark_json = Mark.objects.filter(
        roll_no__roll_number=id).aggregate(Sum('mark')).values()
    mydict = {}
    mydict['Total_Mark'] = tuple(Mark_json)
    print(mydict)
    all_json = list(student_json) + list(detail_Mark_json) + list([mydict])
    print(all_json)
    data = json.dumps(all_json, default=str, indent=1)
    print(type(data))
    return HttpResponse(data, content_type="application/json")


class api_list(ListView):
    model = Student_detail  
    def render_to_response(self, context, *args, **kwargs):
        detail_Mark_json = Mark.objects.filter(roll_no__roll_number=1).annotate().values()
        student_json = Student_detail.objects.filter(id=1).values()
        Mark_json = Mark.objects.filter(roll_no__roll_number=1).aggregate(Sum('mark'))
        all_json = list(student_json) + list(detail_Mark_json) + list([Mark_json])
        print(type(all_json))
        data = json.dumps(all_json, default=str, indent=1)
        print(type(data))
        print(context)
        #queryset = Student_detail.objects.all()
        #data = serializers.serialize('json', all_json , indent=4)
        #return HttpResponse(context)
        return HttpResponse(data, content_type='application/json')

'''
class api_list(ListView):

    model = Student_detail

    def get(self, request, id,  *args, **kwargs):
        detail_Mark_json = Mark.objects.filter(
            roll_no__roll_number=1).annotate().values()
        student_json = Student_detail.objects.filter(id=1).values()
        Mark_json = Mark.objects.filter(
            roll_no__roll_number=1).aggregate(Sum('mark'))
        all_json = list(student_json) + \
            list(detail_Mark_json) + list([Mark_json])
        print(type(all_json))
        data = json.dumps(all_json, default=str, indent=1)
        print(type(data))
        # print(context)
        #queryset = Student_detail.objects.all()
        #data = serializers.serialize('json', all_json , indent=4)
        # return HttpResponse(context)
        return HttpResponse(data, content_type='application/json')


class api_list(ListView):
    model = Student_detail

    def get_context_data(self, *args, **kwargs):
        context = super(api_list, self).get_context_data(**kwargs)
        context.update({
            'character_universe_list': 'dsafa',
            'more_context': 'bsdgfs',
        })
        print(context)
        return HttpResponse(context, content_type='application/json')
'''