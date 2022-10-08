from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('lists/', views.student_details, name="student_details"),
	path('lists/add_form/', views.add_form, name="student_details"),
	]