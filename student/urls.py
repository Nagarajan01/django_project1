from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('lists/logout/', views.logoutUser, name="logout"),
    path('lists/', views.student_details, name="lists"),
    path('lists/update_student/<int:id>',
         views.update_student, name="update_student"),
    path('lists/add_form/', views.add_form, name="add_form"),
    path('lists/show_marks/<int:id>', views.show_mark, name="show_marks"),
    path('lists/show_marks/update_marks/<int:id>',
         views.update_marks, name='update_marks'),
    path('lists/add_marks/', views.add_marks, name='add_marks'),
    path('all_mark_json/<int:id>', views.json_view, name='all_mark_json'),
    path('api_list/', views.api_list.as_view(), name='api_list'),
]
#path('api_list/<int:id>',views.api_list.as_view(), name = 'api_list'),
