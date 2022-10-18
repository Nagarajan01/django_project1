
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class Student_form(ModelForm):
	class Meta:
		model = Student_detail
		fields = ['name', 'roll_number', 'email', 'upload']

class Add_mark_form(ModelForm):
	class Meta:
		model = Mark
		fields = ['roll_no', 'subject', 'mark']
		






	